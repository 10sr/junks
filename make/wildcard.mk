OBJS = $(wildcard *.mk)
OBJS2 = $(wildcard *.dat)

ifeq (,$(OBJS2))

default:
	true OBJS2 is ""

else

default:
	true OBJS: $(OBJS)
	true OBJS2: $(OBJS2)

endif
