/*
 * sample program
 * data transfer with sigqueue() and sigwaitinfo().
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <pthread.h>
#include <signal.h>

#define BUFSIZE 256
typedef struct {
  int             cnt;
  char            buf[BUFSIZE];
}               input_t;

void           *output(void *);
int main(void)
{
  int             loop = 1, cnt = 0;
  pid_t           ownpid;
  pthread_t       thread_id = 0;
  input_t        *input_data;
  sigset_t        sigmask;

  printf("sample program(%s) start\n", __FILE__);
  ownpid = getpid();
  /* block SIGRTMIN+1 in all threads */
  sigemptyset(&sigmask);
  sigaddset(&sigmask, SIGRTMIN + 1);
  if (pthread_sigmask(SIG_BLOCK, &sigmask, NULL) != 0) {
    perror("pthread_sigmask error");
    exit(1);
  }

  /* create new thread */
  if (pthread_create(&thread_id, NULL, output, NULL) < 0) {
    perror("pthread_create error");
    exit(1);
  }

  while (loop) {
    input_data = calloc(1, sizeof(input_t));
    read(STDIN_FILENO, input_data->buf, BUFSIZE - 1);
    input_data->cnt = ++cnt;    /* send data to output()
                                 * thread */
    if (sigqueue(ownpid, SIGRTMIN + 1, (sigval_t) ((void *) input_data)) < 0) {
      perror("sigqueue error");
      exit(1);
    }
    if (strncmp(input_data->buf, "quit\n", 5) == 0) {
      loop = 0;
    }
  }

  if (pthread_join(thread_id, NULL) < 0) {
    perror("pthread_join error");
    exit(1);
  }
  printf("sample program end\n");
  return 0;
}

void         *output(void *arg) {
  int             loop = 1;
  sigset_t        sigmask;
  siginfo_t       siginfo;
  input_t        *input_data;

  printf("thread start\n");
  /* set sigmask for sigwaitinfo() */
  sigemptyset(&sigmask);
  sigaddset(&sigmask, SIGRTMIN + 1);

  while (loop) {
    /* waiting for signal and input data */
    if (sigwaitinfo(&sigmask, &siginfo) < 0) {
      if (errno != EINTR) {
        perror("sigwaitinfo error");
        exit(1);
      }
      continue;
    }
    input_data = (input_t *) siginfo.si_value.sival_ptr;
    if (input_data == NULL) {
      printf("no data\n");
      continue;
    }
    printf("%d:%s\n", input_data->cnt, input_data->buf);
    if (strncmp(input_data->buf, "quit\n", 5) == 0) {
      loop = 0;
    } free(input_data);
  }
  printf("thread end\n");
  pthread_exit(0);
}
