#!/usr/bin/env python3

from timeit import Timer

setup = """
from random import random

def test_zip():
    l = gen_random_list()
    new = list(zip(l))[0]
    return new

def test_compre():
    l = gen_random_list()
    new = [i[0] for i in l]
    return new

def gen_random_list():
    l = []
    for i in range(10000):
        new = []
        i = random()
        new.append(i)
        i = random()
        new.append(i)
        l.append(new)
    return l
"""

def main():
    t_zip = Timer("test_zip()", setup)
    print(t_zip.timeit(10))
    t_compre = Timer("test_compre()", setup)
    print(t_compre.timeit(10))
    return

if __name__ == "__main__":
    main()
