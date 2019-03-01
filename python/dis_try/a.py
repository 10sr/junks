#!/usr/bin/env python3
def testF(strAg="abc"):
    strAt = strAg + "xyz"
    print(strAt)


import dis

dis.dis(testF)
