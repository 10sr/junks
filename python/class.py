#!/usr/bin/env python3

class MyClass:

    @staticmethod
    def func(s):
        print(s)

    def met(self):
        print("MyClass.met")
        self.func("Call MyClass.func from MyClass.met")

print("bc")
c = MyClass()
c.met()


# Add method lately

class MyClass2:
    def met1(self):
        print("MyClass2.meth1")


def met_outside(self, s):
    print("met_outside")
    print(s)
    print(self)


c2 = MyClass2()

MyClass2.met_outside = met_outside

c2.met_outside("ab")
