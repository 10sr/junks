#!/usr/bin/env python3

from __future__ import annotations

from typing import Optional

# https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm
class SingletonCheckInInit:
    """
    Raise error in __init__ when already instanciated.

    __new__ をハックしない。
    はじめの一度は普通のインスタンス化が成功する。
    ２度め以降は get_instance() を使用する必要がある。
    """
    __singleton_instance: Optinal[SingletonCheckInInit] = None

    @classmethod
    def get_instance(cls) -> SingletonCheckInInit:
        if cls.__singleton_instance is None:
            cls.__singleton_instance = cls()
        return cls.__singleton_instance

    def __init__(self):
        if self.__singleton_instance is not None:
            raise RuntimeError("SingletonCheckInInit Singleton!")
        return

print(SingletonCheckInInit.get_instance())
print(SingletonCheckInInit.get_instance())

try:
    SingletonCheckInInit()
except Exception as e:
    print(e)


# https://blanktar.jp/blog/2016/07/python-singleton.html
class SingletonHackNew:
    """
    Do not create new instance in __new__ method.

    通常のインスタンス化で必ず同一のオブジェクトを返す。
    get_instance のようなメソッドを使用しない。
    __init__ はオブジェクト取得時に毎回呼ばれる。
    """
    __singleton_instance = None

    def __init__(self):
        print('SingletonHackNew init')
        return

    def __new__(cls):
        if cls.__singleton_instance is None:
            cls.__singleton_instance = super(SingletonHackNew, cls).__new__(cls)

        return cls.__singleton_instance

print(SingletonHackNew())
print(SingletonHackNew())


# http://www.denzow.me/entry/2018/01/28/171416
class SingletonAnotherNew:
    """
    Raise error in __new__ method and define another new method.

    __internal_new__ メソッドを別に作って get_instance からはそちらを呼ぶ。
    別のメソッドを作らないで get_instance から直接 super 呼べばいい気がするので無駄な気がする。
    """
    __singleton_instance = None

    def __new__(cls):
        raise RuntimeError('SingletonAnotherNew Cannot initialize via Constructor')

    def __init__(self):
        print("SingletonAnotherNew init, This will not be called!!!!!")
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
    """
    Raise error in __init__ method.

    get_instance からは super.__new__ を呼ぶ。
    別に super でなく単に cls.__new__ を呼べばいいのでは？
    それをしたのが SingletonDisallowInit2 。
    """
    __singleton_instance = None

    def __init__(self):
        raise RuntimeError('SingletonDisallowInit Cannot initialize via Constructor')

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


class SingletonDisallowInit2:
    """
    Raise error in __init__ and only use __new__ method.

    get_instance は単に __init__ を迂回して __new__ だけを呼ぶ。
    """
    __singleton_instance = None

    def __init__(self):
        raise RuntimeError('SingletonDisallowInit2 Cannot initialize via Constructor')

    @classmethod
    def get_instance(cls):
        print(super(SingletonDisallowInit2, cls))
        if not cls.__singleton_instance:
            cls.__singleton_instance = cls.__new__(cls)

        return cls.__singleton_instance


print(SingletonDisallowInit2.get_instance())
print(SingletonDisallowInit2.get_instance())
try:
    SingletonDisallowInit2()
except Exception as e:
    print(e)


class SingletonDisallowNew:
    """Raise error in __new__ method.

    SingletonAnotherNew の改変版。
    the() からは super.__new__ を呼ぶ。
    ついでに __init__ も呼ばれなくなってるが直感に反する気がする。
    """
    __singleton_instance = None

    def __new__(self):
        raise RuntimeError('SingletonDisallowNew Cannot initialize via Constructor')

    def __init__(self):
        print("SingletonDisallowNew init, This will not be called!!!!!")
        return

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
