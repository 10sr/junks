all:

V1 ?= a

$(warning $(V1))

V3 = $(shell echo v3)
V2 ?= $(V3) $(V4)  # -> "v3 v4"
V4 = $(shell echo v4)


$(warning $(V2))
