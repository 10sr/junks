var1 =

default: abc efg

abc def:
	true $(var1)

abc: var1 = aaa

efg: def
# definition will be 'inherited' to def
efg: var1 = bbb
