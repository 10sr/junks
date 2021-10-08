#!/usr/bin/env python3

# https://docs.python.org/3/library/enum.html

from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(Color.RED)
print(Color.RED.name)
print(Color.RED.value)

print(Color(2))
print(Color["BLUE"])


# class XY(bool, Enum):
#     class _XTrue(bool, Enum):
#         YFalse = (False, "truefalse")
#         YTrue = (True, "truetrue")
#         def __new__(cls, flag, value):
#             obj = bytes.__new__(cls, [flag])
#             obj._value_ = value
#             obj.label = value
#             return obj
#     class _XFalse(bool, Enum):
#         YFalse = (False, "falsefalse")
#         YTrue = (True, "falsetrue")
#         def __new__(cls, flag, value):
#             obj = bytes.__new__(cls, [flag])
#             obj._value_ = value
#             obj.label = value
#             return obj
#     Xtrue = (True, _XTrue)
#     XFalse = (False, _XFalse)
#     def __new__(cls, flag, value):
#         obj = bytes.__new__(cls, [flag])
#         obj._value_ = value
#         # obj.label = value
#         return obj

# print(XY(True))
