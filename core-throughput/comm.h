/** Receiver function. Intended to be called by pthread_create().
 *
 * Args:
 * * arg: Pointer of struct comm_arg.
 *
 * Returns: NULL
 */
void* ReceiveData(void* _arg);

/* Make array and send data and print them. */
void* SendData(void* _arg);

struct comm_arg {
    int num_send;
    int len_send;
    int cpuid;
    int fd;
};
