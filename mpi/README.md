# Some MPI test programs

## error

This error occur when receved messages are longer than the value of 2nd argument
of MPI_Recv.

    [minnie:25464] *** An error occurred in MPI_Recv
    [minnie:25464] *** on communicator MPI_COMM_WORLD
    [minnie:25464] *** MPI_ERR_TRUNCATE: message truncated
    [minnie:25464] *** MPI_ERRORS_ARE_FATAL (your MPI job will now abort)
    --------------------------------------------------------------------------
    mpiexec has exited due to process rank 0 with PID 25464 on
    node minnie exiting without calling "finalize". This may
    phave caused other processes in the application to be
    terminated by signals sent by mpiexec (as reported here).
    --------------------------------------------------------------------------
