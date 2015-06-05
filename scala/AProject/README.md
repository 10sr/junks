j/scala/AProject
=================

Run:

    sbt run


Notes about package & import
-----------------------------

* `a.scala` において、
  * `import apackage` みたいなのはダメらしい
  * `import apackage.A` なら良い
    * なんで？
  * `apackage/A.scala` 内に定義した `B` クラスを使う時は `import apackage.B` とする
    * ファイル名は完無視ぽい
  * `A.scala` のディレクトリを `apackage` から `bpackage` に変えても、相変わらず `import apackage.B` とする
    * ディレクトリ名は完無視っぽい
  * ようするに、参照してるのはファイル内に書かれたパッケージ名のみで、ディレクトリ構造とかファイル名とかはあんまり気にしていない？
