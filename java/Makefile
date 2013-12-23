target = Test

all : $(target)

$(target) : % : %.class

%.class : %.java
	LC_ALL=C javac $<
