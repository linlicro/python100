#!/usr/bin/python3

"""
打印各种三角形图案

version: 0.1
author: icro
"""

row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('x', end='')
    print()

print()

for i in range(row):
    for j in range(row):
        if j >= row - 1 - i:
            print('x', end='')
        else:
            print(' ', end='')
    print()

print()

for i in range(row):
    for j in range(row - i - 1):
        print(' ', end='')
    for j in range(i * 2 + 1):
        print('x', end='')
    print()
