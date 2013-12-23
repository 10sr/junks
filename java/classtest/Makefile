target = Test AClass BClass ABSClass DerivClass

all : $(target)

$(target) : % : %.class

%.class : %.java
	LC_ALL=C javac $<
