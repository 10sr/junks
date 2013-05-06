#include"timer.h"

double GetElapsedTime(struct timeval *t_start, struct timeval *t_end)
{
    double d_start, d_end;

    d_start = (double)t_start->tv_sec + (double)t_start->tv_usec * 1e-6;
    d_end = (double)t_end->tv_sec + (double)t_end->tv_usec * 1e-6;

    return d_end - d_start;
}
