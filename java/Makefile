.PHONY: printflags

target := Try
javac := LC_ALL=C javac -J-Dfile.encoding=UTF8 -J-Duser.language=en
java := java

#all: $(target)

run: $(target)
	java $<

$(target): %: %.class

%.class: %.java
	$(javac) $<

printflags:
	$(java) -XX:+PrintFlagsFinal 2>/dev/null || true
