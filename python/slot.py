#!/usr/bin/env python3


class AClass():
    __slots__ = ("aattr", "battr")

    # ValueError: 'aattr' in __slots__ conflicts with class variable
    # aattr = 1
    # battr = 2

    def __init__(self):
        self.aattr = 1
        self.battr = 2
        return

    def unkown(self):
        self.cattr = 3
        return self


a = AClass()
# AttributeError: 'AClass' object has no attribute 'cattr'
a.unkown()
