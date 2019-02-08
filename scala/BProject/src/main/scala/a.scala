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

  println(f(1))
  println(g(2))
  println(g(1))

  def f(x: Int): String = x match {
    case 1 => "one"
    case 2 => "two"
    case _ => "many"
  }

  // Cannot concat two match-case exp without the first `{' !!!!!
  def g(x: Int): String = {x match {
    case 1 => "one"
    case 2 => "two"
    case _ => "many"
  }} match {
    case "one" => "a"
    case _ => "many many"
  }
}
