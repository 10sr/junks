#include<stdio.h>

/* print_struct.c --- try to dump the data in a struct */

struct st{
    int a[2];
};

int main(void)
{
    struct st a;
    *(a.a) = 500;
    *(a.a + 1) = 2;
    int sz = sizeof(a);
    char *p = (char *)&a;
    int i;
    for (i = 0; i < sz; i++) {
        printf("%X", p[i]);
    }
    printf("\n");
    return 0;
}
