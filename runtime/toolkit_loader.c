#include <dlfcn.h>
#include <stdio.h>
#include <unistd.h>

__attribute__((noinline)) static void toolkit_probe_ready(void *handle) {
    __asm__ volatile("" : : "r"(handle) : "memory");
}

int main(void) {
    const char *path = "/System/Library/PrivateFrameworks/ToolKit.framework/ToolKit";
    void *handle = dlopen(path, RTLD_NOW | RTLD_LOCAL);
    if (handle == NULL) {
        fprintf(stderr, "dlopen failed: %s\n", dlerror());
        return 1;
    }
    printf("TOOLKIT_LOADED pid=%d handle=%p\n", getpid(), handle);
    fflush(stdout);
    toolkit_probe_ready(handle);
    sleep(300);
    return 0;
}
