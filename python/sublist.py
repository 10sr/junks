#!/usr/bin/env python3

a = [1,2]
b = [0,1,2,3]

if a in [b[i:i+len(a)] for i in range(len(b))]:
    print(True)


for i in range(len(a)):
    if a == b[i:i+len(a)]:
        print("Matched from {}".format(i))
