a := aaa bbb

result := abc def

# what i want: result == abc-aaa abc-bbb def-aaa def-bbb

result := $(foreach elem,$(a),$(result:%=%-$(elem)))

default:
	 echo $(result)
