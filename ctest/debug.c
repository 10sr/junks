/* [printfデバッグに便利なファイル行数表示マクロ - 風と宇宙とプログラム](http://d.hatena.ne.jp/mindcat/20090523/1243045233) */

#include<stdio.h>

#define _STR(x)      #x
#define _STR2(x)     _STR(x)
#define __SLINE__    _STR2(__LINE__)
#define HERE         __FILE__ "(" __SLINE__ ")"

int main(int argc, char** argv){
  printf(HERE);
  return 0;
}
