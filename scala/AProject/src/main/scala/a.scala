import apackage.B

object AProject {
  def main(args: Array[String]): Unit = {
    println("abc")
    val a = new B("DDD")
    a.show

    val m = Map("hoge" -> "fuga", "hoe" -> "fue")
    val s = Seq("mohe", "fuge")

    s.zipWithIndex.map {
      case (e, i) => println(s"e: ${e}, i: ${i}")
    }

    val m1 = s.zipWithIndex.foldLeft(m) {
      case (m, (e, i)) => {
        println(s"m: ${m}, e: ${e}, i: ${i}")
        m.updated(e, i.toString)
      }
    }
    println(m1)

    val r = "hoehoe_fuefue".split("_").toSeq match {
      case Seq(token0, token1) => {
        println(s"token0: ${token0}")
        println(s"token1: ${token1}")
        token0
      }
      case _ => "none"
    }
    println(r)
  }
}
