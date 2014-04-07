CFLAGS = -Wall -g
CC = gcc
TARGET = debug deadlock forever alloc readline sizeof env getopt atomic_add \
	typedef thread cas pthread_key freelist swapcontext swapcontext2 \
	struct_pointer
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

deadlock thread pthread_key : % : %.c
	$(CC) $(CFLAGS) -o $@ -lpthread $<
