###########################
# patsubpst

# Replace strings

foo = a.o b.o
bar = $(foo:%.o=%.c)

.PHONY : patsubst

patsubst :
	true foo = $(foo)
	true bar = $(bar)
