#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<pthread.h>
#include<limits.h>
#include<fcntl.h>

#include"comm.h"
#include"array.h"

/* data whose size is same or less than PIPE_BUF is always sent atomicly
   for details see pipe(7)*/
const unsigned int LEN_SEND = PIPE_BUF;
const unsigned int NUM_SEND = 1000;

const int SENDER_CPU = 0;
const int RECVER_CPU = 1;

int main(int argc, char** argv)
{
    int fildes[2];
    pthread_t th;
    unsigned char buf_r[LEN_SEND * NUM_SEND];
    unsigned char buf_s[LEN_SEND * NUM_SEND];

    /* 0 for receiver, 1 for sender */
    struct comm_arg comm_args[2];

    comm_args[0].buf = buf_r;
    comm_args[1].buf = buf_s;
    comm_args[0].len_send = LEN_SEND;
    comm_args[1].len_send = LEN_SEND;
    comm_args[0].num_send = NUM_SEND;
    comm_args[1].num_send = NUM_SEND;

    comm_args[0].cpuid = RECVER_CPU;
    comm_args[1].cpuid = SENDER_CPU;

    pipe(fildes);
    /* fcntl(fildes[1], F_SETFL, O_NONBLOCK); */
    comm_args[0].fd = fildes[0];
    comm_args[1].fd = fildes[1];

    printf("LEN_SEND = %d\n", LEN_SEND);
    printf("NUM_SEND = %d\n", NUM_SEND);
    printf("LEN = LEN_SEND * NUM_SEND = %d\n", LEN_SEND * NUM_SEND);

    if (pthread_create(&th, NULL, SendData, &(comm_args[1])) < 0) {
        perror("pthread_create");
        exit(1);
    }

    ReceiveData(&(comm_args[0]));

    pthread_join(th, NULL);

    printf("Receiver: time: %f\n", comm_args[0].time);
    PrintArray(buf_r, LEN_SEND * NUM_SEND);
    printf("Sender: time: %f\n", comm_args[1].time);
    PrintArray(buf_s, LEN_SEND * NUM_SEND);

    CheckArray(buf_r, buf_s, LEN_SEND * NUM_SEND);

    return 0;
}
