#!/usr/bin/env ruby1.9

# pretty print
p "abc"
p 1
p [1, 3, 4]
p :abc
p({:a => 1, :b => 2})

str1 = "abc"
p "str1: #{str1}"

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
    p self
    p "met1 of AClass"
    p "m1: " + @m1
  end
end

o1 = AClass.new("abc", 2)
o1.met1()

# inherit
class BClass < AClass
  private :met1
  def met2()
    p "call met1"
    # call met1 of AClass two times
    met1
    # self.met1
    p "done"
  end
end

o2 = BClass.new("def", 3)
o2.met2
begin
  # try to call private method
  o2.met1
rescue NoMethodError => evar
  p evar
end

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

class CClass < BClass
  def met3()
    # call met3 of BClass
    super("jkl")
  end
end

o3 = CClass.new("mno", 2)
o3.met3()


i = 3

puts "while loop"
while i >= 0
  p i
  i -= 1
end

a = [1, 2, 3]

puts "for loop"
for i in a
  p i
end

puts "each loop"
a.each {|e|
  p e
}

puts "times loop"
3.times do |e|
  p e
end

def ymet(idx)
  puts "ymet start"
  idx.times do |a|
    yield a
  end
  puts "ymet end"
end

ymet(3) {|a1| p a1}

def ymet2(idx, arg="def", *rest, &blk)
  puts "ymet2 start"
  idx.times do |i|
    blk.call(arg + i.to_s + " " + rest.to_s)
  end
  puts "ymet2 end"
end

ymet2(3, "abc", 1, 2 ,3) {|a1| puts a1}

# proc object can be passed with &
proc1 = proc {|b| puts "proc1:" + b}
ymet2(3, &proc1)

# pass multiple blocks
def ymet3(arg, blk1, blk2)
  blk1.call(arg)
  blk2.call(arg)
end

ymet3("abc", proc1, proc {|b| puts "proc2: " + b})
