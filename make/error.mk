# error.mk
# Very simple error and warning function example.

AVAR = a

$(warning $(AVAR))

ifdef AVAR
$(error error in if)
endif

$(error myerror)
