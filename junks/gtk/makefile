OBJS = helloworld helloworld2 eventbox frame rangewidgets notebook \
	tree-hello scrolledwin manualmenu upgraded_helloworld

CFLAGS = -Wall -g `pkg-config gtk+-2.0 --cflags`
LDFLAGS = `pkg-config gtk+-2.0 --libs`

default : all

all : ${OBJS}

gitignore :
	(for f in ${OBJS}; \
		do \
			grep "^$$f$$" .gitignore >/dev/null || echo "$$f"; \
			grep "^$${f}.dSYM$$" .gitignore >/dev/null || echo "$${f}.dSYM"; \
		done\
	) >>.gitignore

.c :
	gcc $< -o $@ ${CFLAGS} ${LDFLAGS}
