#!/usr/bin/env python

class Class1() :
    # cannot use method as decorator
    def dec(func) :
        def wrapper(*args, **kargs) :
            print("Before Call")
            r = func(*args, **kargs)
            print("After Call")
            return r
        return wrapper

def dec(func) :
    def wrapper(*args, **kargs) :
        print("Before Call")
        r = func(*args, **kargs)
        print("After Call")
        return r
    return wrapper

class Class2() :
    def __init__(self) :
        self.cdec = Class1()
        return

    @dec
    def met(self, s) :
        print("str " + s)
        return

def main() :
    c = Class2()
    c.met("a")

if __name__ == "__main__" :
    main()
