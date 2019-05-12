#!/usr/bin/python3

"""
英制单位与公制单位互换掷骰子决定做什么

version: 0.1
author: icro
"""

score = float(input('请输入成绩: '))
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('E')