# error.mk
# Very simple error function example.

AVAR = a

ifdef AVAR
$(error error in if)
endif

$(error myerror)
