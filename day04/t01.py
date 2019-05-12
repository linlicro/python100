#!/usr/bin/python3

"""
输入一个数判断是不是素数。

version: 0.1
author: icro
"""

from math import sqrt

num = int(input('请输入一个整数: '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)
