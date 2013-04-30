#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* http://www9.plala.or.jp/sgwr-t/lib/realloc.html */

int main(void)
{
  char *ptr;
  char *tmp;

  /* メモリを割り当てる */
  if ((ptr = (char *)malloc(10)) == NULL) {
    printf("malloc時にメモリが確保できません\n");
    exit(EXIT_FAILURE);
  }
  strcpy(ptr,"computer");
  printf("文字列:%s アドレス:%p\n",ptr,ptr);
  /* メモリを再度割り当てる */
  if ((tmp = (char *)realloc(ptr,200)) == NULL) {
    printf("realloc時にメモリが確保できません\n");
    free(ptr); /* 元のptrを解放して終了 */
    exit(EXIT_FAILURE);
  }
  else {
    ptr = tmp;
    /* reallocの戻り値は一度別変数に取り、
       NULLでないことを確認してから元の変数に代入するのが定石 */
  }
  printf("文字列:%s 新アドレス:%p\n",ptr,ptr);

  /* メモリの解放 */
  free(ptr);

  return 0;
}
