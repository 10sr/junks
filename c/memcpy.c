#include<string.h>
#include<assert.h>
#include<stdio.h>
#include<alloca.h>

int main(void)
{
    char a[] = "#/usr/bin/env";
    char *buf;
    int i;
    size_t sz = sizeof(a);
    buf = alloca(sz);
    memcpy(buf,a,sz);
    assert(buf);
    for (i = 0; i < sz; i++) {
        printf("%o", buf[i]);
    }
    puts("");
    return 0;
}
