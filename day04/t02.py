#!/usr/bin/python3

"""
输入两个正整数，计算最大公约数和最小公倍数。

version: 0.1
author: icro
"""

x = int(input('x = '))
y = int(input('y = '))
if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d最大公约数是%d' % (x, y, factor))
        # `//` ==> 整除
        print('%d和%d最小公倍数是%d' % (x, y, x * y // factor))
        break
