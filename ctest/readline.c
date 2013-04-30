/* read strings from file by line */

#include <stdio.h>
#include <stdlib.h> /* exit( ) で必要 */
#include <string.h> /* strlen( ) で必要 */

#define MAX_LEN 256 /* １行の最大文字数 -1 */

/* http://www1.cts.ne.jp/~clab/hsample/File/File03/File03.html#fgets(%20%20) */
void main(void);

int main(void)
{
  FILE *fp;
  char string[MAX_LEN]; /* 文字列を読み込む配列 */
  int n = 1; /*行番号用カウンタ */
  /* ファイルを開けなかったら */
  if ((fp = fopen("makefile", "r")) == NULL) {
    fprintf(stderr, "ファイルを開けません!\n");
    exit (2); /* メッセージを表示して終了 */
  }

  /* ファイルから失敗するまで行単位で文字を読み込み */
  while ((fgets(string, MAX_LEN - 1, fp)) != NULL) {
    string[strlen(string) - 1] = '\0'; /* 余分な改行コードを削除 */
    printf("%d:", n++); /*行番号を表示し */
    puts(string); /*読み込んだ行を表示 */
  }
  fclose(fp); /* ファイルを閉じる */
}
