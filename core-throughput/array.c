#include"array.h"

#include<unistd.h>
#include<stdio.h>
#include<stdlib.h>

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
        printf("...");
        for (i = len - 5; i < len; i++){
            printf("%d|", data[i]);
        }
    }
    printf("\n");
    return;
}

void InitArray(unsigned char* data, int len)
{
    char num;
    int i = 0;

    srandom(getpid());
    for (i = 0; i < len - 1; i++) {
        num = random() % 256;
        data[i] = num;
        /* printf("%d ", num); */
    }
    data[len-1] = '\0';
    return;
}
