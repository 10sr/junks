#!/usr/bin/env python3

from __future__ import annotations

from typing import Optional
import dataclasses
from pprint import pprint
import typing


@dataclasses.dataclass
class BClass():
    aattr: str
    battr: int = 2

    def __init__(self):
        self.aattr = "hoe"
        return


b = BClass()
print(b)
