project_name := $(shell basename $(CURDIR))

build:
	docker build . -t local/$(project_name)

run:
	docker run -it local/$(project_name)
