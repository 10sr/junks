#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<pthread.h>

const int LEN = 50000;

void print_array(unsigned char* data, int len){
  int i;
  if (len < 10) {
    printf("|");
    for (i = 0; i < len; i++) {
      printf("%d|", data[i]);
    }
  } else {
    for (i = 0; i < 5; i++) {
      printf("|%d", data[i]);
    }
    printf("...");
    for (i = len - 5; i < len; i++){
      printf("%d|", data[i]);
    }
  }
  printf("\n");
  return;
}

void init_array(unsigned char* data, int len){
  char num;
  int i = 0;

  srandom(4);
  for (i = 0; i < len - 1; i++) {
    num = random() % 256;
    data[i] = num;
    /* printf("%d ", num); */
  }
  data[len-1] = '\0';
  return;
}

void* receiver(void* arg){
  unsigned char data[LEN];
  int fd = (int) arg;
  int l;

  l = read(fd, data, LEN);
  if (l < 0) {
    perror("read");
    exit(1);
  }
  printf("Im receiver and received %d bytes!\n", l);
  print_array(data, LEN);
  return NULL;
}

int main(int argc, char** argv){
  int fildes[2];
  unsigned char data[LEN];
  int l;
  pthread_t th;

  pipe(fildes);
  init_array(data, LEN);

  if (pthread_create(&th, NULL, receiver, (void*) fildes[0]) < 0) {
    perror("pthread_create");
    exit(1);
  }


  l = write(fildes[1], data, LEN * sizeof(char));
  if (l < 0){
    perror("write");
    exit(1);
  }
  pthread_join(th, NULL);
  printf("Im sender and sent %d bytes!\n", l);
  print_array(data, LEN);
  return 0;
}
