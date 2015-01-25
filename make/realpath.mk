path = ../

realpath = $(shell cd $(path) && pwd)

$(warning realpath: $(realpath))
$(warning pwd: $(shell pwd))

all:
