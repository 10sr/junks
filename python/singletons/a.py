#!/usr/bin/env python3

from __future__ import annotations

from typing import Optional

# https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm
class SingletonCheckInInit:
    __singleton_instance: Optinal[SingletonCheckInInit] = None

    @classmethod
    def get_instance(cls) -> SingletonCheckInInit:
        if cls.__singleton_instance is None:
            cls.__singleton_instance = cls()
        return cls.__singleton_instance

    def __init__(self):
        if self.__singleton_instance is not None:
            raise RuntimeError("Singleton!")
        return

print(SingletonCheckInInit.get_instance())
print(SingletonCheckInInit.get_instance())

try:
    SingletonCheckInInit()
except Exception as e:
    print(e)


# https://blanktar.jp/blog/2016/07/python-singleton.html
class SingletonHackNew:
    __singleton_instance = None

    def __init__(self):
        print('init')
        return

    def __new__(cls):
        if cls.__singleton_instance is None:
            cls.__singleton_instance = super(SingletonHackNew, cls).__new__(cls)

        return cls.__singleton_instance

print(SingletonHackNew())
print(SingletonHackNew())


# http://www.denzow.me/entry/2018/01/28/171416
class SingletonAnotherNew:
    __singleton_instance = None

    def __new__(cls):
        raise RuntimeError('Cannot initialize via Constructor')

    def __init__(self):
        print("init")
        return

    @classmethod
    def __internal_new__(cls):
        return super(SingletonAnotherNew, cls).__new__(cls)

    @classmethod
    def get_instance(cls):
        if not cls.__singleton_instance:
            cls.__singleton_instance = cls.__internal_new__()  # 変更

        return cls.__singleton_instance

print(SingletonAnotherNew.get_instance())
print(SingletonAnotherNew.get_instance())

try:
    SingletonAnotherNew()
except Exception as e:
    print(e)


class SingletonDisallowInit:
    __singleton_instance = None

    def __init__(self):
        raise RuntimeError('Cannot initialize via Constructor')

    @classmethod
    def get_instance(cls):
        print(super(SingletonDisallowInit, cls))
        if not cls.__singleton_instance:
            cls.__singleton_instance = super(SingletonDisallowInit, cls).__new__(cls)

        return cls.__singleton_instance


print(SingletonDisallowInit.get_instance())
print(SingletonDisallowInit.get_instance())
try:
    SingletonDisallowInit()
except Exception as e:
    print(e)


class SingletonDisallowNew:
    __singleton_instance = None

    def __new__(self):
        raise RuntimeError('Cannot initialize via Constructor')

    @classmethod
    def the(cls):
        print(super(SingletonDisallowNew, cls))
        if not cls.__singleton_instance:
            cls.__singleton_instance = super(SingletonDisallowNew, cls).__new__(cls)

        return cls.__singleton_instance

print(SingletonDisallowNew.the())
print(SingletonDisallowNew.the())
try:
    SingletonDisallowNew()
except Exception as e:
    print(e)
