#!/usr/bin/env ruby1.9

# pretty print
p "abc"
p 1
p [1, 3, 4]
p :abc
p({:a => 1, :b => 2})

# toplevel method definition
def met(a, b)
  p [a, b]
  p self
end

met(1,3)
# call without parens
met 1, 2

def met2()
  p "met2"
  raise RuntimeError.new("test error")
rescue RuntimeError, SyntaxError => evar
  # error handle
  # these two are same
  p evar
  p $!
end

met2

class AClass
  def initialize(a1, a2)
    @m1, @m2 = a1, a2
  end

  def met1()
    p "met1 of AClass"
    p "m1: " + @m1
  end
end

o1 = AClass.new("abc", 2)
o1.met1()

# inherit
class BClass < AClass
  def met2()
    p "calling met1 two times"
    # call met1 of AClass two times
    met1
    self.met1
    p "done"
  end
end

o2 = BClass.new("def", 3)
o2.met2

# try to call nonexisting method
begin
  o2.met3("ghi")
rescue NoMethodError => evar
  p evar
  p "nonexisting method called."
end

# add method to existing class
class BClass
  def met3(a)
    @m1 = a
    p "set m1 and calling met1"
    met1
    p "done"
  end
end

o2.met3("ghi")
o2.met1
