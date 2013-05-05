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

/* Receiver function. Intended to be called by pthread_create().

   Args:
   * arg: File Descriptor for read. Before use must be casted to int.

   Returns: NULL
*/
void* ReceiveData(void* arg){
  unsigned char data[LEN];
  int fd = (int) arg;
  int l;
  int cpu;

  SetCPUID(1);
  cpu = GetCPUID();
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
  PrintArray(data, LEN);
  return NULL;
}

int main(int argc, char** argv){
  int fildes[2];
  unsigned char data[LEN];
  int l;
  int cpu;
  pthread_t th;

  pipe(fildes);                 /* fildes[0] => read, fildes[1] => write */
  fcntl(fildes[1], F_SETFL, O_NONBLOCK);
  InitArray(data, LEN);

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

  l = write(fildes[1], data, LEN * sizeof(char));
  if (l < 0){
    perror("write");
    exit(1);
  }
  pthread_join(th, NULL);
  printf("Im sender on %d and sent %d bytes!\n", cpu, l);
  PrintArray(data, LEN);
  return 0;
}
