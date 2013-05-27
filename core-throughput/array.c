#include"array.h"

#include<unistd.h>
#include<stdio.h>
#include<stdlib.h>

int CheckArray(unsigned char *a1, unsigned char *a2, int len)
{
    int i;
    for (i = 0; i < len; i++) {
        if (a1[i] != a2[i]) {
            printf("Two arrays are not identical!\n");
            exit(1);
            return 1;
        }
    }
    /* printf("Tow arrays are identical.\n"); */
    return 0;
}

void PrintArray(unsigned char* data, int len)
{
    int i;
    if (len < 10) {
        printf("|");
        for (i = 0; i < len; i++) {
            printf("%d|", data[i]);
        }
    } else {
        for (i = 0; i < 5; i++) {
            printf("|%d", data[i]);
        }
        printf("|...|");
        for (i = len - 5; i < len; i++){
            printf("%d|", data[i]);
        }
    }
    printf("\n");
    return;
}

void InitSeed(void)
{
    srandom(getpid());
}

void InitArray(unsigned char* data, int len)
{
    char num;
    int i = 0;

    for (i = 0; i < len - 1; i++) {
        num = random() % 256;
        data[i] = num;
        /* printf("%d ", num); */
    }
    data[len-1] = '\0';
    return;
}
