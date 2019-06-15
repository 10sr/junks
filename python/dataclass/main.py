#!/usr/bin/env python3

from __future__ import annotations

from typing import Optional
import dataclasses
from pprint import pprint
import typing


@dataclasses.dataclass
class AClass:
    aattr: str
    battr: int = 2
    list_attr: list = dataclasses.field(default_factory=list)
    # o_p_t: Optional[int] = None

    normal_attr = "hoehoe"

    def __post_init__(self) -> None:
        # self.battr = self.aattr
        pprint(self)
        pprint(dataclasses.fields(self))
        pprint(dataclasses.asdict(self))
        pprint(dataclasses.astuple(self))

        # We need explicit type check
        # When from __future__ import annotations, field.type is a str
        types = typing.get_type_hints(self)
        for field in dataclasses.fields(self):
            assert isinstance(
                getattr(self, field.name), types[field.name]
            ), f"Type check fail: {field.name}"
        return

    @classmethod
    def from_dict(cls, dict_):
        # types = typing.get_type_hints(cls)
        # pprint(types)
        # for field in dataclasses.fields(cls):
        #     if field.name in dict_:
        #         assert isinstance(dict_[field.name], types[field.name])
        return cls(**dict_)


a = AClass("aaa")
b = AClass.from_dict(
    {
        "aattr": "momomo",
        "battr": "mememe",  # This need explicit type check to fail
        # "o_p_t": "m",
        # "a": True  # This raises error
    }
)
# print(a)
