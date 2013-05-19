#include<stdio.h>

#include<stdlib.h>

int main(int argc, char **argv, char **envp)
{
    int i;
    char *homedir;


    printf("Get env by 3rd argument of main.\n");
    for (i = 0; envp[i]; i++) {
        printf("%s\n", envp[i]);
    }

    printf("Get env by getenv().\n");
    homedir = getenv("HOME");
    printf("HOME : %s\n", homedir);

    return 0;
}
