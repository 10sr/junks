H2P = /Applications/wkhtmltopdf.app/Contents/MacOS/wkhtmltopdf

default : main.pdf

main.pdf : main.html style.css makefile footer.html
	$(H2P) --page-size A4 --orientation Landscape \
		--footer-html footer.html \
		$< $@
