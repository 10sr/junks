j/scala/BProject
=================

Run:

    sbt run

And the output should be

```
[info] Running AProject
BProject 1
A toplevel println
BProject 2
A: DDD
BProject 3
A toplevel println
BProject 4
A: EEE
[success] Total time: 2 s, completed 2015/06/05 17:55:30
```


クラスの評価
-----------

例えば、

```scala
class A {
  println("ab")
  def show = println("A: show")
}
```

とすると、これはクラスがインスタンス化されれるとき（new が使われる時）に評価される。
特に定義のみ書かなければいけないという制限はない。
単に、クラスの {} の中で `def` が使われた場合、それはクラスにぶら下がったメソッドになるという程度の意味っぽい。
