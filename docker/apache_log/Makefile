TAG := local/$(shell basename $(PWD))
NAME := $(shell basename $(PWD))01

.PHONY: rm run build

rm:
	docker stop $(NAME)
	docker rm $(NAME)

run: rm
	docker run --name $(NAME) -p 8880:80 $(TAG)

build:
	docker build -t $(TAG) .
