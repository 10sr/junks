CFLAGS = -Wall -g
LDFLAGS = -lpthread
CC = gcc

TARGET = pipe
RESULT = result.txt

OBJS = array.o main.o getcpu.o timer.o

all : $(TARGET)

pipe : $(OBJS) comm_pipe.o

mpi : $(OBJS) comm_mpi.o

run : $(RESULT)

$(RESULT) : $(TARGET)
	./$(TARGET) | tee $(RESULT)

clean :
	$(RM) $(OBJS) $(TARGET) $(RESULT) comm_pipe.o comm_mpi.o
