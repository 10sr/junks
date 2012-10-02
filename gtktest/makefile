OBJS = helloworld helloworld2 eventbox frame tree-hello scrolledwin

CFLAGS = -Wall -g `pkg-config gtk+-2.0 --cflags`
LDFLAGS = `pkg-config gtk+-2.0 --libs`

default : all

all : ${OBJS}

.c :
	gcc $< -o $@ ${CFLAGS} ${LDFLAGS}
