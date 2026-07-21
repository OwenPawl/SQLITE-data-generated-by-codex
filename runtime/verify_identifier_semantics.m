#import <Foundation/Foundation.h>
#import <dlfcn.h>
#import <sqlite3.h>

@interface NSObject (IdentifierSemanticProbe)
- (instancetype)initWithPersistentIdentifier:(NSData *)persistentIdentifier;
- (instancetype)initWithBundleIdentifier:(NSString *)bundleIdentifier
                         allowPlaceholder:(BOOL)allowPlaceholder
                                    error:(NSError **)error;
- (NSData *)persistentIdentifier;
- (NSArray *)bundleRegistrationsWithError:(NSError **)error;
- (NSString *)bundleIdentifier;
- (NSData *)installIdentifier;
@end

static NSString *hexString(NSData *data) {
    const unsigned char *bytes = data.bytes;
    NSMutableString *result = [NSMutableString stringWithCapacity:data.length * 2];
    for (NSUInteger i = 0; i < data.length; i++) {
        [result appendFormat:@"%02x", bytes[i]];
    }
    return result;
}

static NSData *columnData(sqlite3_stmt *statement, int column) {
    const void *bytes = sqlite3_column_blob(statement, column);
    int length = sqlite3_column_bytes(statement, column);
    return [NSData dataWithBytes:bytes length:(NSUInteger)length];
}

static NSDictionary *verifyLaunchServices(sqlite3 *database) {
    sqlite3_stmt *statement = NULL;
    const char *sql = "SELECT bundleId, persistentIdentifier FROM LaunchServicesState ORDER BY bundleId";
    int prepare = sqlite3_prepare_v2(database, sql, -1, &statement, NULL);
    if (prepare != SQLITE_OK) {
        return @{ @"error": @(sqlite3_errmsg(database)) };
    }

    NSUInteger rows = 0, exact = 0, missing = 0, mismatched = 0;
    NSUInteger reconstructed = 0, reconstructedBundleMatches = 0;
    NSMutableArray *failures = [NSMutableArray array];
    while (sqlite3_step(statement) == SQLITE_ROW) {
        rows++;
        NSString *bundleIdentifier = @((const char *)sqlite3_column_text(statement, 0));
        NSData *stored = columnData(statement, 1);
        id reconstructedRecord = [[NSClassFromString(@"LSRecord") alloc]
            initWithPersistentIdentifier:stored];
        NSData *reconstructedIdentifier = [reconstructedRecord persistentIdentifier];
        NSString *reconstructedBundleIdentifier = [reconstructedRecord bundleIdentifier];
        if ([reconstructedIdentifier isEqualToData:stored]) reconstructed++;
        if ([reconstructedBundleIdentifier isEqualToString:bundleIdentifier]) {
            reconstructedBundleMatches++;
        }
        NSError *error = nil;
        id record = [[NSClassFromString(@"LSApplicationRecord") alloc]
            initWithBundleIdentifier:bundleIdentifier allowPlaceholder:YES error:&error];
        if (!record) {
            missing++;
            [failures addObject:@{ @"bundleIdentifier": bundleIdentifier,
                                   @"error": error.description ?: @"record unavailable" }];
            continue;
        }
        NSData *runtime = [record persistentIdentifier];
        if ([runtime isEqualToData:stored]) {
            exact++;
        } else {
            mismatched++;
            [failures addObject:@{ @"bundleIdentifier": bundleIdentifier,
                                   @"stored": hexString(stored),
                                   @"runtime": runtime ? hexString(runtime) : [NSNull null] }];
        }
    }
    sqlite3_finalize(statement);
    return @{ @"rows": @(rows), @"exactMatches": @(exact),
              @"missingRuntimeRecords": @(missing), @"mismatches": @(mismatched),
              @"reconstructedFromStoredIdentifier": @(reconstructed),
              @"reconstructedBundleIdentifierMatches": @(reconstructedBundleMatches),
              @"failures": failures };
}

static NSDictionary *verifyLink(sqlite3 *database) {
    sqlite3_stmt *statement = NULL;
    const char *sql = "SELECT containerId, installIdentifier FROM LinkState ORDER BY containerId";
    int prepare = sqlite3_prepare_v2(database, sql, -1, &statement, NULL);
    if (prepare != SQLITE_OK) {
        return @{ @"error": @(sqlite3_errmsg(database)) };
    }

    NSMutableDictionary<NSString *, NSData *> *storedByBundle = [NSMutableDictionary dictionary];
    while (sqlite3_step(statement) == SQLITE_ROW) {
        NSString *bundleIdentifier = @((const char *)sqlite3_column_text(statement, 0));
        storedByBundle[bundleIdentifier] = columnData(statement, 1);
    }
    sqlite3_finalize(statement);

    NSError *error = nil;
    id provider = [[NSClassFromString(@"LNMetadataProvider") alloc] init];
    NSArray *registrations = [provider bundleRegistrationsWithError:&error];
    if (!registrations) {
        return @{ @"rows": @(storedByBundle.count),
                  @"error": error.description ?: @"bundle registrations unavailable" };
    }

    NSUInteger exact = 0, mismatched = 0;
    NSMutableSet *seen = [NSMutableSet set];
    NSMutableArray *failures = [NSMutableArray array];
    NSMutableDictionary *runtimeClasses = [NSMutableDictionary dictionary];
    for (id registration in registrations) {
        NSString *className = NSStringFromClass([registration class]);
        runtimeClasses[className] = @([runtimeClasses[className] unsignedIntegerValue] + 1);
        if (![registration respondsToSelector:@selector(bundleIdentifier)] ||
            ![registration respondsToSelector:@selector(installIdentifier)]) continue;
        id metadata = registration;
        NSString *bundleIdentifier = [metadata bundleIdentifier];
        NSData *installIdentifier = [metadata installIdentifier];
        NSData *stored = storedByBundle[bundleIdentifier];
        if (!stored) continue;
        [seen addObject:bundleIdentifier];
        if ([stored isEqualToData:installIdentifier]) {
            exact++;
        } else {
            mismatched++;
            [failures addObject:@{ @"bundleIdentifier": bundleIdentifier,
                                   @"stored": hexString(stored),
                                   @"runtime": installIdentifier ? hexString(installIdentifier) : [NSNull null] }];
        }
    }
    NSMutableArray *missing = [NSMutableArray array];
    for (NSString *bundleIdentifier in storedByBundle) {
        if (![seen containsObject:bundleIdentifier]) [missing addObject:bundleIdentifier];
    }
    [missing sortUsingSelector:@selector(compare:)];
    return @{ @"rows": @(storedByBundle.count), @"runtimeRegistrationCount": @(registrations.count),
              @"runtimeClasses": runtimeClasses, @"exactMatches": @(exact),
              @"mismatches": @(mismatched), @"missingRuntimeRegistrations": missing,
              @"failures": failures };
}

int main(int argc, const char *argv[]) {
    @autoreleasepool {
        if (argc != 2) {
            fprintf(stderr, "usage: verify_identifier_semantics SNAPSHOT.sqlite\n");
            return 2;
        }
        dlopen("/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/LaunchServices", RTLD_NOW | RTLD_LOCAL);
        dlopen("/System/Library/PrivateFrameworks/LinkServices.framework/LinkServices", RTLD_NOW | RTLD_LOCAL);

        sqlite3 *database = NULL;
        int status = sqlite3_open_v2(argv[1], &database, SQLITE_OPEN_READONLY, NULL);
        if (status != SQLITE_OK) {
            fprintf(stderr, "sqlite open failed: %s\n", sqlite3_errmsg(database));
            return 1;
        }
        NSDictionary *result = @{
            @"databasePath": @(argv[1]),
            @"launchServicesPersistentIdentifier": verifyLaunchServices(database),
            @"linkInstallIdentifier": verifyLink(database),
        };
        sqlite3_close(database);
        NSData *json = [NSJSONSerialization dataWithJSONObject:result options:NSJSONWritingPrettyPrinted | NSJSONWritingSortedKeys error:nil];
        fwrite(json.bytes, 1, json.length, stdout);
        fputc('\n', stdout);
    }
    return 0;
}
