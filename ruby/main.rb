#!/usr/bin/env ruby1.9

# pretty print
p "abc"
p 1
p [1, 3, 4]
p({"a" => 1, "b" => 2})
p :abc

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
