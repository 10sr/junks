H2P = wkhtmltopdf
ifeq ($(shell uname),Darwin)
	H2P = /Applications/wkhtmltopdf.app/Contents/MacOS/wkhtmltopdf
endif

.PHONY : default clean

default : main.pdf

clean :
	$(RM) main.pdf main.html

main.pdf : main.html style.css slide.css makefile \
	footer.html header.html slidevars.js
	$(H2P) --page-size A4 --orientation Landscape \
		--margin-top 100pt --margin-right 0pt \
		--margin-left 0pt --margin-bottom 40pt \
		--footer-html footer.html --header-html header.html \
		$< $@
#		--footer-right '[page] / [topage]' \

main.html : main.md makefile
	./md2html.sh $< >$@ || ( rm $@; false )
