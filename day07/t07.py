#!/usr/bin/python3

"""
使用元组

这里有一个非常值得探讨的问题，我们已经有了列表这种数据结构，为什么还需要元组这样的类型呢？
1. 元组中的元素是无法修改的
2. 元组在创建时间和占用的空间上面都优于列表。

version: 0.1
author: icro
"""


def main():
    # 定义元组
    t = ("大林", 30, True, "杭州")
    print(t)
    # 获取元组的元素
    print(t[0])
    print(t[3])
    # 遍历
    for each in t:
        print(each)
    # 元组不能修改
    # t[0] = 'CRO'
    # 重新赋值，老的元组将被垃圾回收
    t = ("CRO", 18, False, "新加坡")
    print(t)
    # 转换成list
    l = list(t)
    print(l)
    # 将列表转换成元组
    fruits = ["apple", "orange", "banana"]
    t2 = tuple(fruits)
    print(t2)


if __name__ == "__main__":
    main()
