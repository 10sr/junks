/* #define __USE_GNU */
#define _GNU_SOURCE
#include<stdio.h>
#include<dlfcn.h>

int (*g_func)(int) = NULL;

int func1(int a)
{
    puts("func1");
    return a;
}

int func2(int a)
{
    puts("func2 called");
    return a + 1;
}

void set_func(char *fname)
{
    int (*f)(int);
    char *err;
    dlerror();
    f = dlsym(RTLD_DEFAULT, fname);
    err = dlerror();
    if (err) {
        /* dlsym error */
        printf("dlsym: %s\n", err);
    } else {
        g_func = f;
    }
    return;
}

int main(void)
{
    int r;
    set_func("func1");
    r = g_func(1);
    set_func("func2");
    r = g_func(2);
    return 0;
}
