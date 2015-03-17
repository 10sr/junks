#include<stdio.h>

int main(int argc, char **argv){
	int a = argc;
	printf("argc: %d\n", a);
	if (argc > 1) {
		printf("%s\n", argv[1]);
	}
	return 0;
}
