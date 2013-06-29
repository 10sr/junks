#include<stdio.h>
#include<unistd.h>
#include<getopt.h>

static void usage(char *cmdname){
    fprintf(stderr,"%s: usage: %s [-a|--aarg] [-b|--barg barg] arg1 arg2\n",
            cmdname, cmdname);
    return;
}

int main(int argc,char **argv){

    char *cmdname = argv[0];
    int option;
    int a = 0;
    char *barg = NULL;
    struct option long_options[] = {
        {"aarg", no_argument, NULL, 'a'},
        {"barg", required_argument, NULL, 'b'},
        {0, 0, 0, 0}
    };

#ifndef __CYGWIN__
    /* Without this guard errors like this happen on cygwin. */
    /* 'optarg' redeclared without dllimport attribute: previous dllimport ignored */
    extern char *optarg;
    extern int optind, opterr;
#endif

    while (1) {
        option = getopt_long(argc, argv, "ab:", long_options, NULL);
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
