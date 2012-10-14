CFLAGS = -Wall

default : all

all : debug deadlock

catstr : catstr.o

invheader : invheader.o

deadlock : deadlock.c
	gcc -Wall -g -o deadlock -pthread deadlock.c
