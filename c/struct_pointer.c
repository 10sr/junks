#include<stdio.h>
#include<assert.h>
#include<malloc.h>

struct point{
    int x;
    int y;
};

int main(void)
{
    struct point *p;
    p = malloc(sizeof(struct point));
    assert(p);
    printf("%p\n", p);
    /* &p->x means pointer to p->x, and same as p */
    printf("%p\n", &p->x);
    printf("%p\n", &p->y);
    return 0;
}
