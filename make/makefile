default : html

HTML_OBJS = index.html test.html

html : $(HTML_OBJS)

$(HTML_OBJS) : %.html : %.md
	markdown $< >$@

clean :
	$(RM) $(HTML_OBJS)
