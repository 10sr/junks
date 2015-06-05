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

* Maven と同じディレクトリ構造がつかえるらしい

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


定数とかクラスとか
-------

* 中身がなさそうなやつ
  * None
    * Option クラスの子クラス（？）
      * よく使いそう
  * Nil
    * 長さゼロのリスト
  * null
    * Null クラスのオブジェクト
      * AnyRef の 子クラス全ての子クラス
      * AnyRef の変数にいれられる
    * http://www.ne.jp/asahi/hishidama/home/tech/scala/any.html
  * Nothing クラス
    * 値が*本当に*ない
    * プロセス自体が終了したり、例外を投げるようなメソッドで使われる
  * Unit クラス
    * 値を返す必要のないメソッドとかで使われる
    * 唯一の値 `()` を持つ
      * 空のタプルらしい



関数、メソッド
-----
[Scala 関数メモ(Hishidama's Scala Function Memo)](http://www.ne.jp/asahi/hishidama/home/tech/scala/function.html) [Scalaメソッド定義メモ(Hishidama's Scala def Memo)](http://www.ne.jp/asahi/hishidama/home/tech/scala/def.html) [Scalaのメソッドと関数は違うもの？ - Togetterまとめ](http://togetter.com/li/154007)

* 関数
  * `FunctionN` トレイトの無名サブクラスのインスタンス
  * `apply()` メソッドに手続きは存在
  * 関数リテラルは、関数オブジェクトのインスタンス化（？）へのシンタックスシュガーとかんがえればよい？
  * `(_: Int) + 1` とかやると一つ引数とる関数が作れる
  * `(_: Int) + (_: Int)` とやると二引数
    * 一つの引数を2回使う関数ではない

* メソッド
  * クラスにぶら下がってるやつ
  * `method _` とやると関数オブジェクトに変換できる
  * オブジェクトとメソッドの間の `.` は省略できる
    * 正気とは思えない
    * この時、引数が一つならカッコも省略できる
      * `str eq "abc"`
      * 中置記法に見せかける感じ
      * この時、メソッドが `:` で終わるなら前後を反転させる
        * `"aa" +: list`
        * まじかよ

  * 関数の部分適用
    * `add(_, 1): Int => Int`
    * 引数を一つ取る関数になる
    * 便利さげ
 
* メソッドを関数に変換できる
  * `println _` 後ろにアンスコをつける
  * これは実際には部分適用と同じ記法ぽい？

* Pimp My Library, implicit class
  * http://kmizu.hatenablog.com/entry/20120506/1336302407 
  * なんで引数に自オブジェクトを取るような書き方をしてるのかよくわかってない


Misc
-----

* implicit parameter
  * implicit val とやっておくと、必要な時に関数呼び出しの引数に勝手につっこんでくれるやつ
  * 型が違えば複数置ける
  * スコープはその変数内でよさげ
* case class
  * ただの便利機能ぽい？
  * http://www.ne.jp/asahi/hishidama/home/tech/scala/class.html#h_case_class

型
----

* むつかしい


パッケージ
-------------

* いまいちわかんないんよな
* 重要なのはファイル内に記述したパッケージ名で、ディレクトリ名は無関係？
  * 試そう
  * [AProject](AProject)
* ここも見る http://www.ne.jp/asahi/hishidama/home/tech/scala/package.html



Java バイトコード・逆コンパイル・逆アセンブル
------------------

* 逆コンパイル
  * http://www.ne.jp/asahi/hishidama/home/tech/java/application.html#class_file
  * `javap <classname>`
    * クラスを逆コンパイルした結果が*出力*される
    * java で表現されたクラス定義が見れる
      * scala で実装したものであっても！

```java
:: 2015/06/05 15:45  $$$$ javap apackage.B
Compiled from "A.scala"
public class apackage.B {
  public void show();
  public apackage.B(java.lang.String);
}
```

* 逆アセンブル
  * http://www.ne.jp/asahi/hishidama/home/tech/java/bytecode.html
  * `javap -c <classname>`
  * バイトコード（インストラクションコード？）が読める
    * アセンブリ言語のようなもの
 
```java
:: 2015/06/05 15:45  $$$$ javap -c apackage.B
Compiled from "A.scala"
public class apackage.B {
  public void show();
    Code:
       0: getstatic     #18                 // Field scala/Predef$.MODULE$:Lsca
la/Predef$;                                                                   
       3: new           #20                 // class scala/collection/mutable/S
tringBuilder                                                                  
       6: dup
       7: invokespecial #23                 // Method scala/collection/mutable/
StringBuilder."<init>":()V                                                    
      10: ldc           #25                 // String B:
      12: invokevirtual #29                 // Method scala/collection/mutable/
StringBuilder.append:(Ljava/lang/Object;)Lscala/collection/mutable/StringBuilde
r;                                                                            
      15: aload_0
      16: getfield      #31                 // Field str:Ljava/lang/String;
      19: invokevirtual #29                 // Method scala/collection/mutable/
StringBuilder.append:(Ljava/lang/Object;)Lscala/collection/mutable/StringBuilde
r;                                                                            
      22: invokevirtual #35                 // Method scala/collection/mutable/
StringBuilder.toString:()Ljava/lang/String;                                   
      25: invokevirtual #39                 // Method scala/Predef$.println:(Lj
ava/lang/Object;)V                                                            
      28: return

  public apackage.B(java.lang.String);
    Code:
       0: aload_0
       1: aload_1
       2: putfield      #31                 // Field str:Ljava/lang/String;
       5: aload_0
       6: invokespecial #43                 // Method java/lang/Object."<init>"
:()V                                                                          
       9: return
}
```
