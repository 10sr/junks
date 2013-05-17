CFLAGS = -Wall -g
LDFLAGS = -lpthread
CC = gcc

TARGET = main
RESULT = result.txt

OBJS = array.o main.o getcpu.o timer.o comm_pipe.o

all : $(TARGET)

run : $(RESULT)

$(RESULT) : $(TARGET)
	./$(TARGET) | tee $(RESULT)

$(TARGET) : $(OBJS)

clean :
	$(RM) $(OBJS) $(TARGET) $(RESULT)
