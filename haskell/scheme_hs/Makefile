targets = main

ghc = ghc
flags = -package parsec --make

all: $(targets)

$(targets): %: %.hs
	$(ghc) $(flags) -o $@ --make $<
