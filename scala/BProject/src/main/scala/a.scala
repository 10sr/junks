import apackage.A

object AProject extends App {
  println("BProject 1")
  val a = new apackage.A("DDD")
  println("BProject 2")
  a.show
  println("BProject 3")
  val b = new apackage.A("EEE")
  println("BProject 4")
  b.show
}
