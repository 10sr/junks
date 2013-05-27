#include<errno.h>
#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

#include"getcpu.h"
#include"timer.h"
#include"array.h"

#include"comm.h"

/* TODO: make sure all data sent and received */

void *ReceiveData(void* _arg)
{
    struct comm_arg *arg = _arg;
    int len_rest = arg->len_send * arg->num_send;
    unsigned char *data = arg->buf;
    unsigned char *start_recv = data;
    int len_recv;               /* len of data received by one read */
    int cpu;

    struct timeval t_start, t_end;

    SetCPUID(arg->cpuid);
    cpu = GetCPUID();
    if (cpu < 0) {
        perror("getcpu");
        exit(1);
    }

    GetCurrentTime(&t_start);

    while (1) {
        len_recv = read(arg->fd, start_recv, len_rest * sizeof(char));
        if (len_recv < 0) {
            if (errno == EAGAIN) {
                continue;
            } else {
                perror("read");
                exit(1);
            }
        } else {
            len_rest -= len_recv;
            start_recv = &(start_recv[len_recv]);
        }
        if (len_rest <= 0) {
            break;
        }
    }

    GetCurrentTime(&t_end);

    arg->time = GetElapsedTime(&t_start, &t_end);

    return NULL;
}

void *SendData(void *_arg){
    struct comm_arg *arg = _arg;
    unsigned char *data = arg->buf;
    unsigned char *start_send = data;
    int i;
    int cpu;
    int len_sent;
    unsigned int all_sent = 0;

    struct timeval t_start, t_end;

    SetCPUID(arg->cpuid);
    cpu = GetCPUID();
    if (cpu < 0) {
        perror("getcpu");
        exit(1);
    }

    InitArray(data, arg->num_send * arg->len_send);

    GetCurrentTime(&t_start);

    for (i = 0; i < arg->num_send;) {
        len_sent = write(arg->fd, start_send, arg->len_send * sizeof(char));
        if (len_sent < 0){
            if (errno == EAGAIN) { /* Resource temporarily unavailable */
                continue;
            } else {
                perror("write");
                exit(1);
            }
        } else {
            all_sent += len_sent;
            start_send = &(start_send[len_sent]);
            i++;
        }
    }

    GetCurrentTime(&t_end);

    arg->time = GetElapsedTime(&t_start, &t_end);

    return NULL;
}
