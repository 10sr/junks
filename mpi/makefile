default: all

all: mpi_hello

clean:
	$(RM) mpi_hello

mpi_hello : mpi_hello.c
	mpicc -g -Wall -o mpi_hello mpi_hello.c
