#!/usr/bin/python3

"""
实现计算求最大公约数和最小公倍数的函数

version: 0.1
author: icro
"""


def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    return x * y // gcd(x, y)


if __name__ == '__main__':
    x = int(input('x = '))
    y = int(input('y = '))
    print('%d, %d的最大公约数是%d' % (x, y, gcd(x, y)))
    print('%d, %d的最小公倍数是%d' % (x, y, lcm(x, y)))
