CFLAGS = -Wall -g -O3
LDFLAGS = -lpthread
CC = gcc

TARGET = main main2
RESULT = result.txt

OBJS = getcpu.o

all : $(TARGET)

main : $(OBJS) main.o

main2 : $(OBJS) main2.o

asm : main.s

%.s : %.c
	$(CC) $(CFLAGS) -S $^

run : $(RESULT)

# $(RESULT) : $(TARGET)
# 	./ | tee $(RESULT)

clean :
	$(RM) $(TARGET) $(OBJS) $(RESULT) *.s
