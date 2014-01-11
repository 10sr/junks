# ifeqor.mk
# Try to get OR in makefile

# If A is aaa or bbb, emit error.

A = aaa
#A = bbb


ifneq "" "$(filter $(A), aaa bbb)"
$(error aaa find.)
endif

all:
