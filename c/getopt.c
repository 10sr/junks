#include<stdio.h>
#include<unistd.h>

static void usage(char *cmdname){
    fprintf(stderr,"%s: usage: %s [-a] [-b barg] arg1 arg2\n",
            cmdname, cmdname);
    return;
}

int main(int argc,char **argv){

    int option;
    int a = 0;
    char *barg = NULL;
    char *cmdname = argv[0];

#ifndef __CYGWIN__
    extern char *optarg;
    extern int optind, opterr;
#endif

    while (1) {
        option = getopt(argc, argv, "ab:");
        if (option == -1) {
            break;
        }

        switch (option) {
        case 'a':
            a = 1;
            break;
        case 'b':
            barg = optarg;
            break;
        /* default: */
            /* usage(cmdname); */
            /* return 1; */
        }
    }

    argc -= optind;
    argv += optind;

    if (argc != 2 ) {
        usage(cmdname);
        return 1;
    }

    printf("a: %d\n", a);
    printf("barg: %s\n", barg);
    printf("arg1: %s\n", argv[0]);
    printf("arg2: %s\n", argv[1]);

    return 0;
}
