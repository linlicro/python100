#!/usr/bin/python3

"""
读写JSON文件

json模块主要有四个比较重要的函数，分别是：

dump - 将Python对象按照JSON格式序列化到文件中
dumps - 将Python对象处理成JSON格式的字符串
load - 将文件中的JSON数据反序列化成对象
loads - 将字符串的内容反序列化成Python对象

version: 0.1
author: icro
"""

import json


def main():
    mydict = {
        'name': '李林',
        'age': 25,
        'qq': 123456,
        'friends': ['Jack', 'Tod'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 200},
            {'brand': 'Benz', 'max_speed': 260}
        ]
    }
    try:
        with open('./day11/data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as ex:
        print(ex)
    print('数据保存成功')


if __name__ == "__main__":
    main()
