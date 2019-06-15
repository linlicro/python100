#!/usr/bin/python3

"""
读写文本文件

version: 0.1
author: icro
"""

import time
from math import sqrt


def open1():
    f = open('/Users/Lin/Documents/python100/day11/test.txt',
             'r', encoding='utf-8')
    print(f.read())
    f.close()


def open2():
    """
    使用Python的异常机制对可能在运行时发生状况的代码进行适当的处理
    """
    f = None
    try:
        f = open('test1.txt', 'r', encoding='utf-8')
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()


def open3():
    """
    通过with关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源
    """
    try:
        with open('test2.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')


def open4():
    """
    使用for-in循环逐行读取或者用readlines方法将文件按行读取到一个列表容器中
    """
    # 一次性读取整个文件内容
    with open('./day11/test.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open('./day11/test.txt', 'r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open('./day11/test.txt') as f:
        lines = f.readlines()
    print(lines)


def is_prime(n):
    """判断素数的函数
    """
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n & factor == 0:
            return False
    return True if n != 1 else False


def open5():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写文件时发生错误！')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成！')


def open6():
    """读写二进制文件
    """
    try:
        with open('./res/pikachu-01.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))
        with open('./res/pikachu-01tmp.jpg', 'wb') as fs2:
            fs2.write(fs1)
    except FileNotFoundError as e:
        print(e)
        print('指定文件无法打开')
    print('执行完成')


if __name__ == "__main__":
    open1()
    # open2()
    # open3()
    # open4()
    # open5()
    # TypeError: a bytes-like object is required, not '_io.BufferedReader'
    # open6()
