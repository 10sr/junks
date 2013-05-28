/**
 * timer.h --- Measure execution time
 *
 * Usage Example:
 *
 *************************************************
 *
 * #include<stdio.h>
 *
 * #include"timer.h"
 *
 * int main(void){
 *     struct timeval t_start, t_end;
 *     int r;
 *     double t_elapsed;
 *
 *     GetCurrentTime(&t_start);
 *
 *     HeavyFunc();
 *
 *     GetCurrentTime(&t_end);
 *
 *     t_elapsed = GetElapsedTime(&t_start, &t_end);
 *     printf("Elapsed: %f\n", t_elapsed);
 *
 *     return 0;
 * }
 *
 *************************************************
 */

#include<sys/time.h>

/* Get current time. Die when gettimeofday failed. */
inline void GetCurrentTime(struct timeval *tv);

/* Calculate the time interval between t_start and t_end. */
double GetElapsedTime(struct timeval *t_start, struct timeval *t_end);
