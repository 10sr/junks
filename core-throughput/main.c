#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<pthread.h>
#include<limits.h>
#include<fcntl.h>

#include"array.h"
#include"getcpu.h"

/* data less than PIPE_BUF must be atomic
 for details see pipe(7)*/
const unsigned int LEN = PIPE_BUF;

void* receiver(void* arg){
unsigned char data[LEN];
 int fd = (int) arg;
 int l;
 int cpu;

 setcpuid(1);
 cpu = getcpuid();
 if (cpu < 0) {
     perror("getcpu");
     exit(1);
 }

 l = read(fd, data, LEN);
 if (l < 0) {
   perror("read");
   exit(1);
 }
 printf("Im receiver on %d and received %d bytes!\n", cpu, l);
 print_array(data, LEN);
 return NULL;
}

int main(int argc, char** argv){
  int fildes[2];
  unsigned char data[LEN];
  int l;
  int cpu;
  pthread_t th;

  pipe(fildes);
  fcntl(fildes[1], F_SETFD, O_NONBLOCK);
  init_array(data, LEN);

  if (pthread_create(&th, NULL, receiver, (void*) fildes[0]) < 0) {
    perror("pthread_create");
    exit(1);
  }

  setcpuid(0);
  cpu = getcpuid();
  if (cpu < 0) {
    perror("getcpu");
    exit(1);
  }

  l = write(fildes[1], data, LEN * sizeof(char));
  if (l < 0){
    perror("write");
    exit(1);
  }
  pthread_join(th, NULL);
  printf("Im sender on %d and sent %d bytes!\n", cpu, l);
  print_array(data, LEN);
  return 0;
}
