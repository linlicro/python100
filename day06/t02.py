#!/usr/bin/python3

"""
实现判断一个数是不是回文数的函数

version: 0.1
author: icro
"""


def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num


if __name__ == "__main__":
    num = int(input("num = "))
    print(is_palindrome(num))
