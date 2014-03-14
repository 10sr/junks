/* Swapping context example 2 from manpage makecontext(3) */

#include <ucontext.h>
#include <stdio.h>
#include <stdlib.h>

static ucontext_t uctx_main, uctx_func1;

#define handle_error(msg)                               \
    do { perror(msg); exit(EXIT_FAILURE); } while (0)

static void
func1(void)
{
    printf("func1: started\n");
    printf("func1: swapcontext(&uctx_func1, &uctx_main)\n");
    if (swapcontext(&uctx_func1, &uctx_main) == -1)
        handle_error("swapcontext");
    printf("func1: returning\n");
}

int
main(int argc, char *argv[])
{
    char func1_stack[16384];

    /* get current context */
    if (getcontext(&uctx_func1) == -1)
        handle_error("getcontext");
    uctx_func1.uc_stack.ss_sp = func1_stack;
    uctx_func1.uc_stack.ss_size = sizeof(func1_stack);
    uctx_func1.uc_link = &uctx_main;
    /* if comment out here, loop here */
    /* makecontext(&uctx_func1, func1, 0); */

    printf("main: swapcontext(&uctx_main, &uctx_func1)\n");
    if (swapcontext(&uctx_main, &uctx_func1) == -1)
        handle_error("swapcontext");

    printf("main: exiting\n");
    exit(EXIT_SUCCESS);
}
