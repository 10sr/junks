/**
 * Usage Example:
 *
 *************************************************
 *
 * #include<stdio.h> // for perror and printf
 * #include"timer.h"
 *
 * int main(void){
 *     struct timeval t_start, t_end;
 *     int r;
 *     double t_elapse;
 *
 *     r = gettimeofday(&t_start, NULL);
 *     if (r < 0) {
 *         perror("gettimeofday");
 *         exit(1);
 *     }
 *
 *     HeavyFunc();
 *
 *     r = gettimeofday(&t_end, NULL);
 *     if (r < 0) {
 *         perror("gettimeofday");
 *         exit(1);
 *     }
 *
 *     t_elapse = GetElapsedTime(&t_start, &t_end);
 *     printf("Elapsed: %f\n", t_elapse);
 *
 *     return 0;
 * }
 *
 *************************************************
 */

#include<sys/time.h>

/* Calculate the time interval between t_start and t_end. */
double GetElapsedTime(struct timeval *t_start, struct timeval *t_end);
