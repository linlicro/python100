#!/usr/bin/python3

"""
练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。

version: 0.1
author: icro
"""


def max2(arr_x):
    m1, m2 = (arr_x[0], arr_x[1]) if arr_x[0] > arr_x[1] else (arr_x[1], arr_x[0])
    for index in range(2, len(arr_x)):
        if arr_x[index] > m1:
            m2 = m1
            m1 = arr_x[index]
        elif arr_x[index] > m2:
            m2 = arr_x[index]
    return m1, m2


if __name__ == "__main__":
    print(max2([1, 2, 3, 4, 5, 6, 7]))
