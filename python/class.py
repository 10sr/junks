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


class MyClass3:
    def met1(self):
        print("MyClass3.met1")
        return

    def __getattr__(self, name):
        print("MyClass3.__getattr__: {} searched".format(name))
        def g(*args, **kargs):
            print("from g #1: {}, {}".format(args, kargs))
            print("from g #2: {}, {}".format(args, kargs))
            return 1
        if name == "f":
            return g
        return "__getattr__ non function return value"


c3 = MyClass3()

print(c3.eee)
print(c3.f(1))


class MyParent(object):
    def met1(self):
        print("MyParent")
        return


class MyChild1(MyParent):
    def met1(self):
        # Cause infinit loop in MyChild2.met1
        super(self.__class__, self).met1()
        return


class MyChild2(MyChild1):
    def met1(self):
        super(self.__class__, self).met1()
        return


o = MyChild2()
# o.met1()
