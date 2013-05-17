#include<errno.h>

#include"getcpu.h"
#include"timer.h"
#include"array.h"

#include"comm.h"

void *ReceiveData(void* _arg)
{
    struct comm_arg *arg = _arg;
    unsigned char data[arg->len_send * arg->num_send;
    unsigned char *start_recv = data;
    int i;
    int fd = arg->fd;
    int len_recv;
    int all_recv = 0;
    int cpu;

    struct timeval t_start, t_end;
    double t_elapse;

    SetCPUID(arg->cpuid);
    cpu = GetCPUID();
    if (cpu < 0) {
        perror("getcpu");
        exit(1);
    }

    GetCurrentTime(&t_start);

    for (i = 0; i < arg->num_send; i++) {
        len_recv = read(arg->fd, start_recv, arg->len_send * sizeof(char));
        if (len_recv < 0) {
            if (errno == EAGAIN) {
                continue;
            } else {
                perror("read");
                exit(1);
            }
        } else {
            all_recv += len_recv;
            start_recv = &(start_recv[len_recv]);
        }
    }

    GetCurrentTime(&t_end);

    printf("Im receiver on %d and received %d bytes!\n", cpu, all_recv);
    PrintArray(data, arg->num_send * arg->len_send);

    t_elapse = GetElapsedTime(&t_start, &t_end);
    printf("Elapsed: %f\n", t_elapse);

    return NULL;
}

void *SendData(void *_arg){
    struct comm_arg *arg = _arg;
    unsigned char data[arg->len_send * arg->num_send];
    unsigned char *start_send = data;
    int cpu;

    struct timeval t_start, t_end;
    double t_elapse;

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


    printf("Im sender on %d and sent %d bytes!\n", cpu, all_sent);
    PrintArray(data, arg->num_send * arg->len_send);

    t_elapse = GetElapsedTime(&t_start, &t_end);
    printf("Elapsed: %f\n", t_elapse);

    return NULL;
}
