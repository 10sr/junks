#!/usr/bin/env python3
class _SingletonBase:
    """
    Raise error in __init__ and only use __new__ method.

    get_instance は単に __init__ を迂回して __new__ だけを呼ぶ。
    """
    __singleton_instance = None

    def __init__(self):
        raise RuntimeError('Cannot initialize via Constructor')

    @classmethod
    def get_instance(cls):
        print(super(_SingletonBase, cls))
        if not cls.__singleton_instance:
            cls.__singleton_instance = cls.__new__(cls)

        return cls.__singleton_instance


class SingletonA(_SingletonBase):
    a1 = 1

    def met1(self):
        print(a1)


print(SingletonA.get_instance())
print(SingletonA.get_instance())
try:
    SingletonA()
except Exception as e:
    print(e)
