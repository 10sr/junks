#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>
#include<unistd.h>

pthread_mutex_t* lock_handles;

void *deadlock(void *rank)
{
  int my_rank = (int) rank;

  printf("I am thread %d and lock %d.\n", my_rank, my_rank);
  pthread_mutex_lock(&lock_handles[my_rank]);

  sleep(1);

  printf("I am thread %d and lock %d.\n", my_rank, 1 - my_rank);
  pthread_mutex_lock(&lock_handles[1 - my_rank]);

  printf("I am thread %d and unlock %d.\n", my_rank, my_rank);
  pthread_mutex_unlock(&lock_handles[my_rank]);
  printf("I am thread %d and unlock %d.\n", my_rank, 1 - my_rank);
  pthread_mutex_unlock(&lock_handles[1 - my_rank]);

  return NULL;
}

int main(int argc, char **argv)
{
  int thread;
  int thread_count = 2;
  pthread_t *thread_handles;

  int lock;
  int lock_count = 2;

  lock_handles = (pthread_mutex_t *)
    malloc(lock_count*sizeof(pthread_mutex_t));


  for (lock = 0; lock < lock_count; lock++){
    pthread_mutex_init(&lock_handles[lock], NULL);
  }

  thread_handles = (pthread_t *)malloc(thread_count*sizeof(pthread_t));

  for (thread = 0; thread < thread_count; thread++){
    pthread_create(&thread_handles[thread], NULL, deadlock, (void*)thread);
  }

  for(thread = 0; thread < thread_count; thread++){
    pthread_join(thread_handles[thread], NULL);
  }

  for (lock = 0; lock < lock_count; lock++){
    pthread_mutex_destroy(&lock_handles[lock]);
  }

  free(thread_handles);
  free(lock_handles);

  return 0;
}
