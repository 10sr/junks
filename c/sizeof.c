#include<stdio.h>

#define P(type) int s_##type = sizeof(type);  \
  printf(#type ": %d\n", s_##type)

int main(void){
  /* int s_pointer = sizeof(void*); */
  /* int s_int = sizeof(int); */
  /* int s_double = sizeof(double); */

  /* printf("int: %d, pointer: %d\n", s_int, s_pointer); */
  P(char);
  P(int);
  P(float);
  P(double);
  /* P(void*); */
  int s_pointer = sizeof(void*); printf("pointer: %d\n", s_pointer);
  return 0;
}
