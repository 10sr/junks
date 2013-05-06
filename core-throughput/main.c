#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<pthread.h>
#include<limits.h>
#include<fcntl.h>

#include"array.h"
#include"getcpu.h"
#include"timer.h"

/* data less than PIPE_BUF is always atomic
   for details see pipe(7)*/
const unsigned int LEN = PIPE_BUF;

/** Receiver function. Intended to be called by pthread_create().
 *
 * Args:
 * * arg: File Descriptor for read. Before use must be casted to int.
 *
 * Returns: NULL
 */
void* ReceiveData(void* arg)
{
    unsigned char data[LEN];
    int fd = (int) arg;
    int len_written;
    int cpu;

    struct timeval t_start, t_end;
    int t_status;
    double t_elapse;

    SetCPUID(1);
    cpu = GetCPUID();
    if (cpu < 0) {
        perror("getcpu");
        exit(1);
    }

    t_status = gettimeofday(&t_start, NULL);
    if (t_status < 0) {
        perror("gettimeofday");
        exit(1);
    }

    len_written = read(fd, data, LEN);
    if (len_written < 0) {
        perror("read");
        exit(1);
    }

    t_status = gettimeofday(&t_end, NULL);
    if (t_status < 0) {
        perror("gettimeofday");
        exit(1);
    }

    printf("Im receiver on %d and received %d bytes!\n", cpu, len_written);
    PrintArray(data, LEN);

    t_elapse = GetElapsedTime(&t_start, &t_end);
    printf("Elapsed: %f\n", t_elapse);

    return NULL;
}

int main(int argc, char** argv)
{
    int fildes[2];
    unsigned char data[LEN];
    int len_written;

    int cpu;
    pthread_t th;

    struct timeval t_start, t_end;
    double t_elapse;
    int t_status;

    pipe(fildes);
    fcntl(fildes[1], F_SETFL, O_NONBLOCK);
    InitArray(data, LEN);

    if (pthread_create(&th, NULL, ReceiveData, (void*) fildes[0]) < 0) {
        perror("pthread_create");
        exit(1);
    }

    SetCPUID(0);
    cpu = GetCPUID();
    if (cpu < 0) {
        perror("getcpu");
        exit(1);
    }

    t_status = gettimeofday(&t_start, NULL);
    if (t_status < 0) {
        perror("gettimeofday");
        exit(1);
    }

    len_written = write(fildes[1], data, LEN * sizeof(char));
    if (len_written < 0){
        perror("write");
        exit(1);
    }

    t_status = gettimeofday(&t_end, NULL);
    if (t_status < 0) {
        perror("gettimeofday");
        exit(1);
    }

    pthread_join(th, NULL);

    printf("Im sender on %d and sent %d bytes!\n", cpu, len_written);
    PrintArray(data, LEN);

    t_elapse = GetElapsedTime(&t_start, &t_end);
    printf("Elapsed: %f\n", t_elapse);
    return 0;
}
