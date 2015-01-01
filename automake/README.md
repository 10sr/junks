j/automake
==========

A clean automake example with `src` subdirectory.


Prepare
-------

* `configure.ac`

  Copy of `configure.scan`, which will be generated automatically by `autoscan`
  (Can be go with `configure.in` too, but `configure.ac` seems to be newer).

* `NEWS`, `README`, `AUTHORS` and `ChangeLog`

  These files must be created by hand.


Modify
------

* `configure.ac`

  * Modify args of `AC_INIT`
  * Add line `AM_INIT_AUTOMAKE`
  * Add `AC_CONFIG_FILES([Makefile src/Makefile])`

* `Makefile.am` and `src/Makefile.am`


Generate Files for Distribution
-------------------------------

1. `autoreconf -iv`
