#!/usr/bin/python3

"""
列表也可以做切片操作

version: 0.1
author: icro
"""


def main():
    fruits = ["grape", "apple", "strawbrery", "waxberry"]
    fruits += ["pitaya", "pear", "mango"]
    # 遍历循环
    for fruit in fruits:
        print(fruit.title(), end=" ")
    print()
    # 切片
    fruits2 = fruits[1:4]
    print(fruits2)
    # 不能复制列表，只能通过完整切片新创建
    fruits3 = fruits2[:]
    print(fruits3)
    fruits4 = fruits3[-3:-1]
    print(fruits4)
    # 倒转操作
    fruits5 = fruits4[::-1]
    print(fruits5)


if __name__ == "__main__":
    main()
