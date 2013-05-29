CFLAGS = -Wall -g -O3
LDFLAGS = -lpthread
CC = gcc

TARGET = main
RESULT = result.txt

OBJS = getcpu.o main.o

all : $(TARGET)

$(TARGET) : $(OBJS)

asm : main.s

%.s : %.c
	$(CC) $(CFLAGS) -S $^

run : $(RESULT)

# $(RESULT) : $(TARGET)
# 	./ | tee $(RESULT)

clean :
	$(RM) $(TARGET) $(OBJS) $(RESULT) *.s
