#!/usr/bin/env python3

import sys

def eratosthenes(n):
    # array of flags
    # If a[n] == True, n is a prime number
    a = [True for e in range(n)]
    a[0] = a[1] = False

    for i in range(n//2+1):
        if a[i] == True:
            # i is prime
            # Set i*2, i*3, ... to False
            for j in range(2, n):
                try:
                    a[i*j] = False
                except IndexError:
                    break

    return (i for (i, e) in enumerate(a) if e == True)

def main(argv):
    # Print the biggest prime number
    print(list(eratosthenes(int(argv[1])))[-1])

if __name__ == "__main__":
    main(sys.argv)
