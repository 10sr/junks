package apackage

class A(str: String){
  def show = {
    println("A: " + str)
  }
}

class B(str: String){
  def show = {
    println("B: " + str)
    val a = new A("B: " + str)
    a.show
  }
}
