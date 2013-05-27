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

const int SENDER_CPU = 0;
const int RECVER_CPU = 1;

struct main_arg {
    /* input */
    int num_send;
    int len_send;
    /* output */
    double time_r;
    double time_s;
};

int OneTry(struct main_arg *arg);
int Try(int num_send);
double GetAvg(double *a, int len);

double GetAvg(double *a, int len)
{
    int i;
    double sum = 0.0;
    for (i = 0; i < len; i++) {
        sum += a[i];
    }
    return sum / len;
}

int main(int argc, char** argv)
{
    InitSeed();
    Try(1);
    Try(10);
    Try(100);
    return 0;
}

int Try(int num_send)
{
    struct main_arg arg;
    int i;
    int try = 10000;
    double time_r[try];
    double time_s[try];

    arg.len_send = LEN_SEND;
    arg.num_send = num_send;

    printf("LEN = %d\n", LEN_SEND * num_send);

    for (i = 0; i < try; i++) {
        OneTry(&arg);
        time_r[i] = arg.time_r;
        time_s[i] = arg.time_s;
    }

    printf("Recv Agv: %f\n", GetAvg(time_r, try));
    printf("Send Agv: %f\n", GetAvg(time_s, try));
    return 0;
}

int OneTry(struct main_arg *arg)
{
    int fildes[2];
    pthread_t th;
    int len_all = arg->len_send * arg->num_send;
    unsigned char buf_r[len_all];
    unsigned char buf_s[len_all];

    /* 0 for receiver, 1 for sender */
    struct comm_arg comm_args[2];

    comm_args[0].buf = buf_r;
    comm_args[1].buf = buf_s;
    comm_args[0].len_send = arg->len_send;
    comm_args[1].len_send = arg->len_send;
    comm_args[0].num_send = arg->num_send;
    comm_args[1].num_send = arg->num_send;

    comm_args[0].cpuid = RECVER_CPU;
    comm_args[1].cpuid = SENDER_CPU;

    pipe(fildes);
    /* fcntl(fildes[1], F_SETFL, O_NONBLOCK); */
    comm_args[0].fd = fildes[0];
    comm_args[1].fd = fildes[1];

    if (pthread_create(&th, NULL, SendData, &(comm_args[1])) < 0) {
        perror("pthread_create");
        exit(1);
    }

    ReceiveData(&(comm_args[0]));

    pthread_join(th, NULL);

    arg->time_r = comm_args[0].time;
    arg->time_s = comm_args[1].time;
    /* printf("Receiver: time: %f\n", comm_args[0].time); */
    /* PrintArray(buf_r, len_all); */
    /* printf("Sender: time: %f\n", comm_args[1].time); */
    /* PrintArray(buf_s, len_all); */

    /* CheckArray(buf_r, buf_s, len_all); */

    return 0;
}
