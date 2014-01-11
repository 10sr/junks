#include<stdio.h>
#include<stdint.h>
#include<pthread.h>

#define THREAD_NUM 3

/* http://linuxgcc.sytes.net/sys020.php */

pthread_key_t g_key;

void _func_called_from_th(void)
{
    intptr_t i;
    i = (intptr_t) pthread_getspecific(g_key);
    printf("i am %ld.\n", (intptr_t) i);
    return;
}

void *_thread_func(void *_arg)
{
    pthread_setspecific(g_key, _arg);
    _func_called_from_th();
    return NULL;
}

int main(int argc, char **argv)
{
    pthread_t th[THREAD_NUM];
    intptr_t i;

    pthread_key_create(&g_key, NULL);

    for (i = 0; i < THREAD_NUM; i++) {
        pthread_create(&(th[i]), NULL, _thread_func, (void *)i);
    }

    for (i = 0; i < THREAD_NUM; i++) {
        pthread_join(th[i], NULL);
    }

    return 0;
}
