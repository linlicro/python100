#!/usr/bin/python3

"""
列表的排序操作

version: 0.1
author: icro
"""


def main():
    list1 = ["orange", "apple", "zoo", "internationalization", "blueberry"]
    # sorted函数返回列表排序后的拷贝不会修改传入的列表 btw, 函数的设计就应该像sorted函数一样尽可能不产生副作用
    list2 = sorted(list1)
    print(list2)
    list3 = sorted(list1, reverse=True)
    print(list3)
    # 通过key关键字指定通过长度排序
    list4 = sorted(list1, key=len)
    print(list4)
    # 给列表对象发出排序消息直接在列表对象上进行排序
    list1.sort(reverse=True)
    print(list1)


if __name__ == "__main__":
    main()
