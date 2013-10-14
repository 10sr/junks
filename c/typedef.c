#include<stdio.h>

typedef char char2[2];

int main(int argc, char **argv)
{
    char2 a;
    printf("%d\n", sizeof(a));
    return 0;
}
