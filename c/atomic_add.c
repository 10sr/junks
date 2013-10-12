#include<stdio.h>

/* Very basic usage of atomic fetch-and-add function without threads. */
/* http://hayamiz.com/~haya/blog/?p=97 */
/* http://en.wikipedia.org/wiki/Fetch-and-add#x86_implementation */

#define P(ivar) printf(#ivar " = %d\n", ivar)

int main(int argc, char **argv)
{
    int a = 1;
    int b = 2;
    P(a);
    P(b);
    __sync_fetch_and_add(&a, b);
    P(a);
    return 0;
}
