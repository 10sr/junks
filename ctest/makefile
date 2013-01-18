CFLAGS = -Wall
OBJS = debug deadlock
ALLOBJS = $(OBJS) catstr invheader

default : all

all : $(OBJS)

gitignore :
	(for f in ${ALLOBJS}; do echo $$f; echo $${f}.dSYM; done) >>.gitignore

catstr : catstr.o

invheader : invheader.o

deadlock : deadlock.c
	gcc -Wall -g -o deadlock -pthread deadlock.c
