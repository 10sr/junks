#include<stdio.h>
#include<stdint.h>
#include<pthread.h>

#define THREAD_NUM 4


/*********************************************
 utils
*********************************************/

#define cas __sync_val_compare_and_swap

/* http://locklessinc.com/articles/locks/ */
/* Atomic exchange (of various sizes) */
static inline void *xchg_64(void *ptr, void *x)
{
    __asm__ __volatile__("xchgq %0,%1"
                         :"=r" ((unsigned long long) x)
                         :"m" (*(volatile long long *)ptr),
                          "0" ((unsigned long long) x)
                         :"memory");

    return x;
}


/* rdtsc */
/* https://github.com/shinh/test/blob/2a7a2bf7dbffae14851725154e187a636bb269ff/rdtsc.c */
#define RDTSC(X)                                \
    do {                                        \
        unsigned int eax, edx;                                      \
        __asm__ __volatile__ ("cpuid"::: "eax", "ebx", "ecx", "edx");   \
        __asm__ __volatile__ ("rdtsc": "=a"(eax), "=d"(edx));           \
        X = ((unsigned long long)edx << 32) | eax;                      \
    } while (0);

unsigned long long rdtsc() {
    unsigned long long r;
    RDTSC(r);
    return r;
}


/*********************************************
 MCS Lock
*********************************************/


struct _mcs_lock_t {
    struct _mcs_lock_t *next;
    int lock;                   /* 1: got lock */
};
typedef struct _mcs_lock_t mcs_lock_t;

mcs_lock_t *last = NULL;

mcs_lock_t *mcs_aquire(mcs_lock_t *me)
{
    mcs_lock_t *prev;
    me->next = NULL;
    prev = xchg_64(&last, me);
    if (! prev) {
        /* no one locked previously */
        me->lock = 1;
        return me;
    }
    me->lock = 0;
    prev->next = me;
    while (me->lock == 0) {
        /* wait until prev set lock to 1 */
        continue;
    }
    return me;
}

mcs_lock_t *mcs_release(mcs_lock_t *me)
{
    if (! me->next) {
        /* if last and me are same, set last to NULL and return */
        if (cas(&last, me, NULL) == me) {
            me->lock = 0;
            return me;
        }
        while (! me->next) {
            /* wait until me->next is set */
            continue;
        }
    }

    me->lock = 0;
    /* unlock next */
    me->next->lock = 1;
    return me;
}

int mcs_test()
{
    uint64_t start, end;
    int i;
    mcs_lock_t l;

    start = rdtsc();
    for (i = 0; i < 10; i++) {
        mcs_aquire(&l);
        mcs_release(&l);
    }
    end = rdtsc();

    return end - start;
}


void *_thread_func(void *_arg){
    int i;
    intptr_t myidx = (intptr_t) _arg;
    int totalcycle = 0;
    for (i = 2; i >= THREAD_NUM; i++) {
        pthread_barrier_waitls
            ();
        if (myidx < i) {
            totalcycle += syscall(701);
        }
    }
    printf("%ld: %d\n", myidx, totalcycle);
    return NULL;
}

void mcs_main(){
    pthread_t th[THREAD_NUM];
    intptr_t i;

    for (i = 0; i < THREAD_NUM; i++) {
        pthread_create(&(th[i]), NULL, _thread_func, (void *)i);
    }

    for (i = 0; i < THREAD_NUM; i++){
        pthread_join(th[i], NULL);
    }
    return;
}

int main(int argc, char **argv)
{
    mcs_main();
    /* printf("%d\n", r); */
    return 0;
}
