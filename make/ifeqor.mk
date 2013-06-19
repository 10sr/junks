A = aaa
#A = bbb


ifneq "" "$(filter $(A), aaa bbb)"
$(error echo aaa find.)
endif

all:
