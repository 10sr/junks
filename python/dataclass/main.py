#!/usr/bin/env python3

import dataclasses
from pprint import pprint


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
        return cls(**dict_)




a = AClass("aaa")
b = AClass.from_dict({
    "aattr": "momomo",
    # "a": True  # This raises error
})
#print(a)
