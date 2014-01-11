#include<pthread.h>
#include<stdio.h>
#include<stdint.h>

#define THREAD_NUM 2

void *_thread_func(void *_arg)
{
    printf("i am %ld.\n", (intptr_t) _arg);
    return NULL;
}

int main(int argc, char **argv)
{
    pthread_t th[THREAD_NUM];
    intptr_t i;

    /* int pthread_create(pthread_t *thread, const pthread_attr_t *attr, void */
    /*                    *(*start_routine)(void *), void *arg) */
    for (i = 0; i < THREAD_NUM; i++) {
        pthread_create(&(th[i]), NULL, _thread_func, (void *)i);
    }
    /* int pthread_join(pthread_t thread, void **value_ptr) */
    for (i = 0; i < THREAD_NUM; i++) {
        pthread_join(th[i], NULL);
    }
    return 0;
}
