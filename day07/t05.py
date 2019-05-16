#!/usr/bin/python3

"""
使用列表的生成式语法来创建列

version: 0.1
author: icro
"""

import sys


def main():
    f = [x for x in range(0, 10)]
    print(f)
    f = [x + y for x in "ABCDE" for y in "12345"]
    print(f)
    # 用列表的生成表达式语法创建列表容器
    # 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
    f = [x ** 2 for x in range(0, 1000)]
    print(sys.getsizeof(f))
    # print(f)
    # 请注意下面的代码创建的不是一个列表而是一个生成器对象
    # 通过生成器可以获取到数据但它不占用额外的空间存储数据
    # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
    f = (x ** 2 for x in range(0, 1000))
    print(sys.getsizeof(f))
    # for val in f:
    #     print(val)


if __name__ == "__main__":
    main()
