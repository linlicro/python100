#!/usr/bin/python3

"""
寻找“完美数”。ref: https://baike.baidu.com/item/%E5%AE%8C%E5%85%A8%E6%95%B0/370913

version: 0.1
author: icro
"""


def perfectNumber(num):
    num_sum = 0
    for i in range(num - 1, 0, -1):
        if num % i == 0:
            num_sum += i
    if num_sum == num:
        print('%d是完美数.' % num)
    else:
        print('%d不是完美数' % num)


x = int(input('x = '))
perfectNumber(x)
