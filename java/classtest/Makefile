target = Test AClass BClass ABSClass DerivClass MultiInitClass

all : $(target)

.PHONY : $(target)

$(target) : % : %.class

%.class : %.java
	LC_ALL=C javac $<
