#!/usr/bin/python3

"""
实现判断一个数是不是素数的函数

version: 0.1
author: icro
"""


def is_prime(num):
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False


if __name__ == "__main__":
    num = int(input("num = "))
    print(is_prime(num))
