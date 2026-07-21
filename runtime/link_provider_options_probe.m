#import <Foundation/Foundation.h>
#import <dlfcn.h>

@interface NSObject (LinkProviderOptionsProbe)
- (instancetype)initWithOptions:(NSInteger)options;
- (NSArray *)bundleRegistrationsWithError:(NSError **)error;
@end

int main(void) {
    @autoreleasepool {
        dlopen("/System/Library/PrivateFrameworks/LinkServices.framework/LinkServices", RTLD_NOW | RTLD_LOCAL);
        for (NSInteger options = 0; options < 32; options++) {
            id provider = [[NSClassFromString(@"LNMetadataProvider") alloc] initWithOptions:options];
            id direct = nil, xpc = nil;
            @try {
                direct = [provider valueForKey:@"directProvider"];
                xpc = [provider valueForKey:@"xpcProvider"];
            } @catch (NSException *exception) {
                direct = exception.reason;
            }
            NSError *error = nil;
            NSArray *registrations = [provider bundleRegistrationsWithError:&error];
            printf("OPTION\t%ld\tdirect=%s\txpc=%s\tcount=%ld\terror=%s\n",
                   (long)options,
                   direct ? NSStringFromClass([direct class]).UTF8String : "nil",
                   xpc ? NSStringFromClass([xpc class]).UTF8String : "nil",
                   (long)registrations.count,
                   error ? error.description.UTF8String : "nil");
        }
    }
    return 0;
}
