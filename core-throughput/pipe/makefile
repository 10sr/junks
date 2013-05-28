CFLAGS = -Wall -g -O3
LDFLAGS = -lpthread
CC = gcc

TARGET = pipe
RESULT = result.txt

OBJS = array.o main.o getcpu.o timer.o

all : $(TARGET)

pipe : main_pipe

main_pipe : $(OBJS) comm_pipe.o
	$(CC) $(LDFLAGS) $^ -o $@

mpi : main_mpi

main_mpi : $(OBJS) comm_mpi.o

run : $(RESULT)

# $(RESULT) : $(TARGET)
# 	./ | tee $(RESULT)

clean :
	$(RM) $(OBJS) main_pipe main_mpi $(RESULT) comm_pipe.o comm_mpi.o
