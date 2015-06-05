package apackage

class A(str: String){
  // Evaluated each time when A is instanciated (new is used)
  println("A toplevel println")
  def show = {
    println("A: " + str)
  }
}
