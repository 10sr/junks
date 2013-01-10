#!/usr/bin/env python2

# [Ordered Dictionary for Py2.4 « Python recipes « ActiveState Code]
# (http://code.activestate.com/recipes/576693/)

from collections import OrderedDict

od = OrderedDict()

od["a"] = 1
od["b"] = 2
od["c"] = 4
od["d"] = 5
del od["a"]
od["a"] = 3

for k, v in od.iteritems():
    print("{},{}".format(k,v))
print("")

# print:
# b,2
# c,4
# d,5
# a,3
# OrderedDict is FIFO

for k in reversed(od) :         # reversed is not destructive
    print("{},{}".format(k,od[k]))
print("")

# a,3
# d,5
# c,4
# b,2

for k, v in od.iteritems():
    print("{},{}".format(k,v))
print("")

# b,2
# c,4
# d,5
# a,3
