#!/usr/bin/python3

"""
输入圆的半径计算计算周长和面积

version: 0.1
author: icro
"""
import math

r = float(input('圆的半径 = '))
p = 2 * math.pi * r
a = math.pi * r * r
print('周长: %.2f' % p)
print('面积: %.2f' % a)