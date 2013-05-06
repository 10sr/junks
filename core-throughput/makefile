CFLAGS = -Wall -g
LDFLAGS = -lpthread
CC = gcc

TARGET = main
RESULT = result.txt

OBJS = array.o main.o getcpu.o timer.o

all : $(TARGET)

run : $(RESULT)

$(RESULT) : $(TARGET)
	./$(TARGET) | tee result.txt

$(TARGET) : $(OBJS)

clean :
	$(RM) $(OBJS)
