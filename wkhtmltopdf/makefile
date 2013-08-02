H2P = wkhtmltopdf
ifeq ($(shell uname),Darwin)
	H2P = /Applications/wkhtmltopdf.app/Contents/MacOS/wkhtmltopdf
endif

default : main.pdf

main.pdf : main.html style.css makefile footer.html
	$(H2P) --page-size A4 --orientation Landscape \
		--margin-top 0 --margin-right 0 --margin-left 0 --margin-bottom 20 \
		--footer-html footer.html \
		$< $@
#		--footer-right '[page] / [topage]' \
