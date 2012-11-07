OBJS = helloworld helloworld2 eventbox frame rangewidgets notebook tree-hello \
scrolledwin manualmenu upgraded_helloworld

CFLAGS = -Wall -g `pkg-config gtk+-2.0 --cflags`
LDFLAGS = `pkg-config gtk+-2.0 --libs`

default : all

all : ${OBJS}

.c :
	gcc $< -o $@ ${CFLAGS} ${LDFLAGS}
