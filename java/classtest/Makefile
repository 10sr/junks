target = Test AClass BClass

all : $(target)

$(target) : % : %.java
	LC_ALL=C javac $<
