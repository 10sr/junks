j/scala
=======


Study Scala.


sbt
----

[始める sbt — 始める sbt](http://www.scala-sbt.org/0.13/tutorial/ja/index.html)

* Simple Build Tool の略。
  * scala 特化のツールにこの名前はどうなの
* *Typesafe Activator は activator ui と activator new という 2つのコマンドを追加するカスタム版の sbt だ。 つまり、activator は sbt のスーパーセットであると言える*
  * http://www.scala-sbt.org/0.13/tutorial/ja/Activator-Installation.html

* なるほど！
  * Maven と同じディレクトリ構造らしい

> sbt は以下のものを自動的に検知する:

> * ベースディレクトリにあるソースファイル　
> * src/main/scala か src/main/java 内のソースファイル
> * src/test/scala か src/test/java 内のテストソースファイル
> * src/main/resources か src/test/resources 内のデータファイル
> * lib 内の jar ファイル


* build.sbt はビルドファイルというよりコンフィグファイルっぽい
  * node での `package.json` みたいな感じ
    * 依存とかを書く場所
  * 大文字で始まってない
* *sbt は [Apache Ivy] を使ってマネージ依存性を実装している*
  * へー
  * % とかつかうやつ
    * *% メソッドは、文字列から ModuleID オブジェクトを作る*
      * ふーん？
