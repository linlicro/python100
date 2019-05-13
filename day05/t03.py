#!/usr/bin/python3

"""
百鸡百钱问题。ref: https://baike.baidu.com/item/%E7%99%BE%E9%B8%A1%E7%99%BE%E9%92%B1/5857320

version: 0.1
author: icro
"""


for x in range(0, 21):
    y = 0
    while True:
        if 5 * x + 3 * y + (100 - x - y) / 3 == 100:
            print('公鸡%d只，母鸡%d只，小鸡%d只' % (x, y, (100 - x - y)))
        y += 1
        if 5 * x + 3 * y > 100:
            break
