#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<stdint.h>
#include<assert.h>
#include<pthread.h>

#include"time.h"
#include"getcpu.h"

const int CPU_FREQ_M = 2000;

struct pthread_arg {
    char *buf;
    int cpuid;
    int csize;
    int len;
    /* out */
    int e;
};

void *Reader(void *_arg)
{
    struct pthread_arg *arg;
    char *a;
    int cpuid;
    int csize;
    uint64_t start, end;
    int i;
    char d;

    arg = _arg;

    a = arg->buf;
    csize = arg->csize;

    cpuid = arg->cpuid;
    SetCPUID(cpuid);
    assert(GetCPUID() == cpuid);

    start = rdtsc();
    for (i = 0; i < arg->len; i+=(csize*4)) {
        d = a[i];
        d = a[i + csize];
        d = a[i + csize * 2];
        d = a[i + csize * 3];
    }
    end = rdtsc();

    arg->e = end - start;
    return NULL;
}

void *GetNearestEdge(void *ptr, int size)
{
    /* remainder */
    int rm;
    rm = (uintptr_t) ptr % size;
    if (rm) {
        return (void *) ((uintptr_t) ptr - rm + size);
    } else {
        return ptr;
    }
}

int GetCacheLineSize(void)
{
    return (int)sysconf(_SC_LEVEL1_DCACHE_LINESIZE);
}

int OneTry(int size, int cpuid)
{
    pthread_t th;
    char *abuf;
    int i;
    int csize;
    struct pthread_arg arg;

    csize = GetCacheLineSize();

    char buf[size * (csize + 1)];

    abuf = GetNearestEdge(buf, csize);

    for (i = 0; i < 16; i++) {
        buf[i] = (char) i;
    }

    arg.buf = abuf;
    arg.cpuid = cpuid;
    arg.csize = csize;
    arg.len = size * csize;
    arg.e = 0;

    /* printf("CacheLine Size: %dKB\n", csize); */
    /* printf("Addr: %p\n", buf); */
    /* printf("%p %% %d = %d\n", buf, csize, (int) ((uintptr_t) buf % csize)); */
    /* printf("AlignedAddr: %p\n", abuf); */
    /* printf("%p %% %d = %d\n", abuf, csize, (int) ((uintptr_t) abuf % csize)); */
    assert((int) ((uintptr_t) abuf % csize) == 0);

    if (pthread_create(&th, NULL, Reader, &arg) < 0) {
        perror("pthread_creat");
        exit(1);
    }

    pthread_join(th, NULL);

    /* printf("E: %d\n", arg.e); */
    return arg.e;
}

double GetAvg(int *a, int len)
{
    int i;
    int sum = 0;
    for (i = 0; i < len; i++) {
        sum += a[i];
    }
    return (double) sum / len;
}

int TryOnCPU(cpuid)
{
    int try = 1000;
    int size = 400;

    int result[try];
    int i;

    double avgnsec;
    double throuput;

    for (i = 0; i < try; i++) {
        result[i] = OneTry(size, cpuid);
    }

    avgnsec = GetAvg(result, try) / CPU_FREQ_M;
    /* 64 is cache line size. i should get this value from getconf. */
    throuput = 64 * size / avgnsec;
    /* printf("CPU: %d, Speed: %f[KByte/ns]\n", cpuid, throuput); */
    printf("%d, %f\n", cpuid, throuput);
    return 0;
}

int main(int argc, char **argv)
{
    int cpu;
    int num_cpu;
    int csize;

    if (argc < 2) {
        fprintf(stderr, "%s <cpunum>\n", argv[0]);
        exit(1);
    }

    csize = GetCacheLineSize();

    num_cpu = atoi(argv[1]);

    for (cpu = 0; cpu < num_cpu; cpu++) {
        TryOnCPU(cpu);
    }
    /* printf("CacheLine Size: %dKB\n", csize); */
    return 0;
}