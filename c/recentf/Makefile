target = recentf.so

default: all

all: $(target)

$(target): %.so: %.c
	$(CC) -shared -fPIC -o $@ $<
