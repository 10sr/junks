a := aaa bbb

result := abc def

# what i want: result == abc-aaa abc-bbb def-aaa def-bbb

result_a := $(foreach elem,$(a),$(result:%=%-$(elem)))
result += $(result_a)

default:
	 echo $(result)
