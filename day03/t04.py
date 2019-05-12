#!/usr/bin/python3

"""
输入三条边长如果能构成三角形就计算周长和面积

version: 0.1
author: icro
"""

import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长: %f' % (a+b+c))
    p = (a+b+c)/2
    area = math.sqrt(p * (p-a) * (p-b) * (p-c))
    print('面积: %f' % area)
else:
    print('不能构成三角形')
