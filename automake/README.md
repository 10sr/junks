j/automake
==========

A clean automake example with `src` subdirectory.



Files to edit
------

* `configure.ac`

  A Template can be obtained by cp `configure.scan`, which will be generated automatically by `autoscan`
  (Can be go with `configure.in` too, but using `configure.ac` seems to be a newer way).

  * Modify args of `AC_INIT`
  * Add line `AM_INIT_AUTOMAKE`
  * Add `AC_CONFIG_FILES([Makefile src/Makefile])`

* `Makefile.am` and `src/Makefile.am`
* `NEWS`, `README`, `AUTHORS` and `ChangeLog`


Generate Files for Distribution
-------------------------------

1. Issue `autoreconf -iv`
2. Index some files generated by this command
  * COPYING
  * INSTALL
  * Makefile.in
  * aclocal.m4
  * compile
  * configure
  * depcomp
  * install-sh
  * src/Makefile.in
  * src/config.h.in



Reference
----------

* [autoconfの使用方法- hippos-lab::net](http://homepage2.nifty.com/hippos/autoconf/index.html)
* [all](http://www.spa.is.uec.ac.jp/~kinuko/slidemaker/autotools/)
* [Autoconf](http://www.gnu.org/savannah-checkouts/gnu/autoconf/manual/autoconf-2.69/html_node/index.html)
* [Autoconf:](http://www.spa.is.uec.ac.jp/~kinuko/slidemaker/autotools/autoconf.html)
* [configureの作り方(autotoolsの使い方） - メモ。。メモ。。](http://nopipi.hatenablog.com/entry/2013/01/14/025509)
* [autoreconfを使って簡単にビルド環境を作る - にたまごほうれん草](http://d.hatena.ne.jp/emergent/20081106/1225896312)
* [autoconf & automake](http://www.jaist.ac.jp/~kiyoshiy/memo/autoconf.html)
* [初心者への GNU autoconf のススメ](http://sharl.haun.org/autoconf.html)
* [Automakeでmakeする](http://www.02.246.ne.jp/~torutk/cxx/automake/automake.html)
* [automake: `<TT>configure.ac</TT>'のスキャン](http://www.bookshelf.jp/texi/automake-ja/automake-ja_5.html)