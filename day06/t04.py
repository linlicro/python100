#!/usr/bin/python3

"""
判断输入的正整数是不是回文素数

version: 0.1
author: icro
"""

from t02 import is_palindrome
from t03 import is_prime

if __name__ == "__main__":
    num = int(input("num = "))
    print(is_prime(num) and is_palindrome(num))
