#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<pthread.h>

const int LEN = 50;

void* receiver(void* arg){
  char data[LEN];
  int fd = (int) arg;

  printf("Im receiver!\n");
  if (read(fd, data, LEN) < 0) {
    perror("read");
    exit(1);
  }
  print_array(data, LEN);
  return NULL;
}

void print_array(char* data, int len){
  int i;
  printf("|");
  for (i = 0; i < len; i++) {
    printf("%d|", data[i]);
  }
  printf("\n");
  return;
}

void init_array(char* data, int len){
  char num;
  int i = 0;

  for (i = 0; i < len - 1; i++) {
    num = random() % 256;
    data[i] = num;
    /* printf("%d ", num); */
  }
  data[len-1] = '\0';
  return;
}

int main(int argc, char** argv){
  int fildes[2];
  char data[LEN];
  pthread_t th;

  pipe(fildes);
  init_array(data, LEN);

  if (pthread_create(&th, NULL, receiver, (void*) fildes[0]) < 0) {
    perror("pthread_create");
    exit(1);
  }


  printf("Im sender!\n");
  if (write(fildes[1], data, LEN * sizeof(char)) < 0) {
    perror("write");
    exit(1);
  }
  print_array(data, LEN);
  pthread_join(th, NULL);
  return 0;
}
