CFLAGS = -Wall -g
CC = gcc
TARGET = debug deadlock forever alloc readline sizeof env getopt atomic_add \
	typedef thread
ALLTARGET = $(TARGET) catstr invheader

default : all

all : $(TARGET)

clean :
	$(RM) $(ALLTARGET)

gitignore :
	(for f in ${ALLTARGET}; \
		do \
			grep "^$$f$$" .gitignore >/dev/null || echo "$$f"; \
			grep "^$${f}.dSYM$$" .gitignore >/dev/null || echo "$${f}.dSYM"; \
		done\
	) >>.gitignore

catstr : catstr.o

invheader : invheader.o

deadlock : deadlock.c
	$(CC) $(CFLAGS) -o $@ -pthread $<
