#!/usr/bin/python3

"""
斐波那契数列

version: 0.1
author: icro
"""


def fibonacci(i):
    if i == 1 or i == 2:
        return i
    return fibonacci(i - 1) + fibonacci(i - 2)


i = int(input("i = "))
print("i: %d f: %d" % (i, fibonacci(i)))
