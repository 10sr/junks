# Test #2

all: abc.txt

abc.% : def.%
	cat $< | tr a c >$@

%.txt : %.dat
	cat $< | tr a b >$@
