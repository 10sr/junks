#!/usr/bin/env python3

class MyClass :

    @staticmethod
    def func(s) :
        print(s)

    def met(self) :
        print("bcd")
        self.func("aaab")

print("bc")
c = MyClass()
c.met()
