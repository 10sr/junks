OBJS = index.html test.html

default : all

all : ${OBJS}

.SUFFIXES : .md .html

.md.html :
	markdown $< >$*.html

