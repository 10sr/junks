#include<stdio.h>

void concat(char* str)
{
  char* new = "aab" str;    /* error! */
  printf("%s\n", new);
  return;
}

int main(void)
{
  char* str = "aaa";
  concat(str);
  return 0;
}
