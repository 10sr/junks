#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<pthread.h>
#include<limits.h>
#include<fcntl.h>

#include"array.h"
#include"getcpu.h"
#include"timer.h"

/* data whose size is same or less than PIPE_BUF is always sent atomicly
   for details see pipe(7)*/
const unsigned int LEN_SEND = PIPE_BUF;
const unsigned int NUM_SEND = 100;
/* const unsigned int LEN = LEN_SEND * NUM_SEND; */


/** Receiver function. Intended to be called by pthread_create().
 *
 * Args:
 * * arg: File Descriptor for read. Before use must be casted to int.
 *
 * Returns: NULL
 */
void* ReceiveData(void* arg)
{
    unsigned char data[LEN_SEND * NUM_SEND];
    unsigned char *start_recv = data;
    int i;
    int fd = (int) arg;
    int len_recv;
    int all_recv = 0;
    int cpu;

    struct timeval t_start, t_end;
    double t_elapse;

    SetCPUID(1);
    cpu = GetCPUID();
    if (cpu < 0) {
        perror("getcpu");
        exit(1);
    }

    GetCurrentTime(&t_start);

    for (i = 0; i < NUM_SEND; i++) {
        len_recv = read(fd, data, LEN_SEND * sizeof(char));
        if (len_recv < 0) {
            perror("read");
            exit(1);
        }
        all_recv += len_recv;
        start_recv = &(start_recv[len_recv]);
    }

    GetCurrentTime(&t_end);

    printf("Im receiver on %d and received %d bytes!\n", cpu, all_recv);
    PrintArray(data, LEN_SEND * NUM_SEND);

    t_elapse = GetElapsedTime(&t_start, &t_end);
    printf("Elapsed: %f\n", t_elapse);

    return NULL;
}

int main(int argc, char** argv)
{
    int fildes[2];
    unsigned char data[LEN_SEND * NUM_SEND];
    unsigned char *start_send = data;
    int i;
    int len_sent;
    int all_sent = 0;

    int cpu;
    pthread_t th;

    struct timeval t_start, t_end;
    double t_elapse;

    pipe(fildes);
    fcntl(fildes[1], F_SETFL, O_NONBLOCK);
    InitArray(data, LEN_SEND * NUM_SEND);

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

    GetCurrentTime(&t_start);

    for (i = 0; i < NUM_SEND; i++) {
        len_sent = write(fildes[1], start_send, LEN_SEND * sizeof(char));
        if (len_sent < 0){
            perror("write");
            exit(1);
        }
        all_sent += len_sent;
        start_send = &(start_send[len_sent]);
    }

    GetCurrentTime(&t_end);

    pthread_join(th, NULL);

    printf("Im sender on %d and sent %d bytes!\n", cpu, all_sent);
    PrintArray(data, LEN_SEND * NUM_SEND);

    t_elapse = GetElapsedTime(&t_start, &t_end);
    printf("Elapsed: %f\n", t_elapse);
    return 0;
}
