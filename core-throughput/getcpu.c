#define _GNU_SOURCE
#include<stdio.h>
#include<stdlib.h>
#include<sched.h>

#include"getcpu.h"

/* or use thread_ */

/* [Manpage of SCHED_SETAFFINITY](http://surf.ml.seikei.ac.jp/~nakano/JMwww/html/LDP_man-pages/man2/sched_setaffinity.2.html)
 */

int GetCPUID(){
  /* cpu_set_t mask; */
  /* int r; */
  int i;

  /* CPU_ZERO(&mask); */
  /* /\* 0 for pid means me *\/ */
  /* r = sched_getaffinity(0, &mask, sizeof(cpu_set_t)); */
  /* if (! r){ */
  /*   perror("sched_getaffinity"); */
  /*   exit(1); */
  /* } */

  /* for (i = 0; i < CPU_SETSIZE; i++) { */
  /*   if (CPU_ISSET(i, &mask)) { */
  /*     return i; */
  /*   } */
  /* } */
  i = sched_getcpu();
  if (i < 0) {
    perror("sched_getcpu");
    exit(1);
  } else {
    return i;
  }
}

void SetCPUID(int cpu){
  cpu_set_t mask;
  int r;

  CPU_ZERO(&mask);
  CPU_SET(cpu, &mask);

  r = sched_setaffinity(0, sizeof(cpu_set_t), &mask);
  if (r < 0) {
    perror("sched_setaffinity");
    exit(1);
  }

  return;
}
