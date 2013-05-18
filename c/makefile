CFLAGS = -Wall -g
CC = gcc
OBJS = debug deadlock forever alloc readline sizeof env
ALLOBJS = $(OBJS) catstr invheader

default : all

all : $(OBJS)

clean :
	$(RM) $(ALLOBJS)

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
	$(CC) $(CFLAGS) -o $@ -pthread $<
