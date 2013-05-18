OBJS = index.html test.html

default : all

all : ${OBJS}

%.html : %.md
	markdown $< >$@
