#!/usr/bin/python3

def main():
    fizzbuzz2(50)

def fizzbuzz(num):
    for i in range(1, num + 1):
        if(i % 3 == 0):
            print("Fizz", end="")
        if(i % 5 == 0):
            print("Buzz", end="")
        if(i % 3 != 0 and i % 5 != 0):
            print("%d" % i, end="")
        print("")

def fizzbuzz2(num):
    for i in range(1, num + 1):
        str = ""
        if(i % 3 == 0):
            str = str + "Fizz"
        if(i % 5 == 0):
            str = str + "buzz"
        if(str == ""):
            str = "%d" % i
        print(str)

main()
