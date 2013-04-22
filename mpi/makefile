OBJS = mpi_hello
CFLAGS = -Wall -g
CC = mpicc

default: all

all: $(OBJS)

clean:
	$(RM) $(OBJS)

mpi_hello : mpi_hello.c
	$(CC) $(CFLAGS) $< -o $@
