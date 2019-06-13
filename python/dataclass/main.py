#!/usr/bin/env python3

# from __future__ import annotations

import dataclasses
from pprint import pprint
import typing


@dataclasses.dataclass
class AClass:
    aattr: str
    battr: int = 2
    list_attr: list = dataclasses.field(default_factory=list)

    normal_attr = "hoehoe"

    def __post_init__(self) -> None:
        #self.battr = self.aattr
        pprint(self)
        pprint(dataclasses.fields(self))
        pprint(dataclasses.asdict(self))
        pprint(dataclasses.astuple(self))
        return

    @classmethod
    def from_dict(cls, dict_):
        # We need explicit type check
        for field in dataclasses.fields(cls):
            if field.name in dict_:
                assert isinstance(dict_[field.name], field.type)
        return cls(**dict_)




a = AClass("aaa")
b = AClass.from_dict({
    "aattr": "momomo",
    # "battr": "mememe"  # This need explicit type check to fail
    # "a": True  # This raises error
})
#print(a)
