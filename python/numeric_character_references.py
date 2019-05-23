#!/usr/bin/env python3

"""http://blog.liris.org/2010/12/pythonhtml.html"""

import sys
import re

pattern = re.compile('([\u00ff-\uffff])')



for l in sys.stdin:
    new = pattern.sub(lambda x: "&#x" + hex(ord(x.group(1)))[2:] + ";", l)
    print(new, end="")
