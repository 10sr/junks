anotherdir
==========

Test how rules are applyed.


Test #1 (Makefile)
------------------

1. Put Makefile into `a/` and Add a rule like `%.txt: %.dat` in it.
2. Add a rule that depends on `../b/e.txt` and see how this file is created.


### Result

The rules are successfully applyed to `../b/e.txt`.



Test #2 (Makefile2)
-------------------

1. Put Makefile2 and add rules like `%.txt: %.dat` and `abc.%: def.%`.
2. Add a rule that depends on `abc.txt` and see how this file is created.


### Result

The first rule is always used.
