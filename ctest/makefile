CFLAGS = -Wall
OBJS = debug deadlock
ALLOBJS = $(OBJS) catstr invheader

default : all

all : $(OBJS)

gitignore :
	(for f in ${ALLOBJS}; \
		do \
			grep "^$$f$$" .gitignore >/dev/null || echo "$$f"; \
			grep "^$${f}.dSYM$$" .gitignore >/dev/null || echo "$${f}.dSYM"; \
		done\
	) >>.gitignore

catstr : catstr.o

invheader : invheader.o

deadlock : deadlock.c
	gcc -Wall -g -o deadlock -pthread deadlock.c
