#!/usr/bin/env python3

import dataclasses
import inspect
import typing
from typing import get_type_hints, List

import typeguard


@dataclasses.dataclass
class AClass():
    a: str
    b: int


a = AClass("hoe", 3)
print(a)
b = AClass("hoe", "moe")
print(b)


class TAClass(AClass):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        types = get_type_hints(self, globals())  # type: ignore
        for field in dataclasses.fields(self):
            typeguard.check_type(
                field.name, getattr(self, field.name), types[field.name]
            )
        return


c = TAClass("hoe", 3)
print(c)
try:
    _ = TAClass("hoe", "moe")
except TypeError as e:
    print(e)


def _process_class(cls, caller_locals, caller_globals, *args, **kargs):
    dataclassed = dataclasses.dataclass(cls, *args, **kargs)
    dataclass_init = getattr(dataclassed, "__init__")
    setattr(dataclassed, "__dataclass_init__", dataclass_init)

    init_body = """def __init__(self, *args, **kargs):
    self.__dataclass_init__(*args, **kargs)
    print(f"Typeguarded! {args}, {kargs}")

    types = typing.get_type_hints(self, caller_globals, caller_locals)
    for field in dataclasses.fields(self):
        typeguard.check_type(
            field.name, getattr(self, field.name), types[field.name]
        )
    return
    """
    locals = {}
    globals = {
        "caller_locals": caller_locals,
        "caller_globals": caller_globals,
        "typing": typing,
        "dataclasses": dataclasses,
        "typeguard": typeguard,
    }
    exec(init_body, globals, locals)

    setattr(dataclassed, "__init__", locals["__init__"])
    return dataclassed


def typeguarded_dataclass(_cls=None, *args, **kargs):
    caller = inspect.stack()[1].frame;
    try:
        caller_locals = caller.f_locals
        caller_globals = caller.f_globals
    finally:
        del caller

    def wrap(cls):
        return _process_class(cls, caller_locals, caller_globals, *args, **kargs)

    # See if we're being called as @dataclass or @dataclass().
    if _cls is None:
        # We're called with parens.
        return wrap

    # We're called as @dataclass without parens.
    return wrap(_cls)


@typeguarded_dataclass
class T2AClass():
    a: str
    b: int
    c: List[int]


e = T2AClass("hoe", 2, [1, 2, 3])
print(e)
try:
    _ = T2AClass("hoe", "hoehoe", [1, 2])
except TypeError as e:
    print(e)
try:
    _ = T2AClass("hoe", 2, ["a", "meme"])
except TypeError as e:
    print(e)
