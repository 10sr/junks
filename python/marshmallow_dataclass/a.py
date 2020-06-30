#!/usr/bin/env python3

from typing import ClassVar, List, Optional, Type

from marshmallow import Schema
from marshmallow.exceptions import ValidationError
from marshmallow_dataclass import dataclass

@dataclass
class AClass():
    a: str
    b: List[str]
    c: Optional[int]
    Schema: ClassVar[Type[Schema]] = Schema


schema = AClass.Schema()
print(schema)

a: AClass = schema.load({
    "a": "hoe",
    "b": ["a", "b"],
})
print(a)

try:
    _ = schema.load({
        "a": "hoe",
        "b": [1, 2],
    })
except ValidationError as e:
    print(e)
