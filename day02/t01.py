#!/usr/bin/python3

"""
华氏温度转摄氏温度

version: 0.1
author: icro
"""

fahrenheit = float(input('fahrenheit = '))
celsius = (fahrenheit - 32) / 1.8
print('%.2f华氏度 = %.2f摄氏度' % (fahrenheit, celsius))