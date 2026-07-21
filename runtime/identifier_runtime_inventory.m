#import <Foundation/Foundation.h>
#import <objc/runtime.h>
#import <dlfcn.h>

static void printMethods(Class cls, BOOL classMethods) {
    Class target = classMethods ? object_getClass(cls) : cls;
    unsigned int count = 0;
    Method *methods = class_copyMethodList(target, &count);
    for (unsigned int i = 0; i < count; i++) {
        SEL selector = method_getName(methods[i]);
        const char *types = method_getTypeEncoding(methods[i]);
        printf("METHOD\t%s\t%c\t%s\t%s\n",
               class_getName(cls), classMethods ? '+' : '-',
               sel_getName(selector), types ?: "");
    }
    free(methods);
}

static void printProperties(Class cls) {
    unsigned int count = 0;
    objc_property_t *properties = class_copyPropertyList(cls, &count);
    for (unsigned int i = 0; i < count; i++) {
        printf("PROPERTY\t%s\t%s\t%s\n", class_getName(cls),
               property_getName(properties[i]),
               property_getAttributes(properties[i]) ?: "");
    }
    free(properties);
}

static void printIvars(Class cls) {
    unsigned int count = 0;
    Ivar *ivars = class_copyIvarList(cls, &count);
    for (unsigned int i = 0; i < count; i++) {
        printf("IVAR\t%s\t%s\t%s\n", class_getName(cls),
               ivar_getName(ivars[i]), ivar_getTypeEncoding(ivars[i]));
    }
    free(ivars);
}

static void printClass(const char *name) {
    Class cls = objc_getClass(name);
    printf("CLASS\t%s\t%s\n", name, cls ? "present" : "missing");
    if (!cls) return;
    printProperties(cls);
    printIvars(cls);
    printMethods(cls, NO);
    printMethods(cls, YES);
}

int main(void) {
    @autoreleasepool {
        const char *frameworks[] = {
            "/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/LaunchServices",
            "/System/Library/PrivateFrameworks/LinkServices.framework/LinkServices",
            "/System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient",
        };
        for (size_t i = 0; i < sizeof(frameworks) / sizeof(frameworks[0]); i++) {
            void *handle = dlopen(frameworks[i], RTLD_NOW | RTLD_LOCAL);
            printf("IMAGE\t%s\t%s\n", frameworks[i], handle ? "loaded" : dlerror());
        }

        const char *classes[] = {
            "LSPersistentIdentifier",
            "LSRecord",
            "LSApplicationRecord",
            "LSBundleRecord",
            "LNRegisteredBundleMetadata",
            "LNMetadataProvider",
        };
        for (size_t i = 0; i < sizeof(classes) / sizeof(classes[0]); i++) {
            printClass(classes[i]);
        }
    }
    return 0;
}
