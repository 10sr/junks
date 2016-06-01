#!/usr/bin/env python3

def main():
    a = ("abc" +
         "def")
    print(a)
    b = "abc" + \
        "def"
    print(b)

    he = True
    if he:
        ge = "a"
    else:
        ge = "b"

    print(ge)

    # No error
    if False and hoge:
        print("abc")

main()
