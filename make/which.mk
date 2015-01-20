echo=$(shell which echo)
echoo=$(shell which echoo 2>/dev/null)

# /usr/bin/echo
$(warning $(echo))
## empty string
$(warning $(echoo))
