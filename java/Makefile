target = Test

#all: $(target)

run: $(target)
	java $<

$(target): %: %.class

%.class: %.java
	LC_ALL=C javac -J-Dfile.encoding=UTF8 -J-Duser.language=en $<
