#!/usr/bin/python3

"""
使用字符串

version: 0.1
author: icro
"""


def main():
    # 定义字符串
    str = "Hello String!"
    # 计算长度
    print(len(str))
    # 首字母大写
    print(str.capitalize())
    # 大写
    print(str.upper())
    # 子串的位置
    print(str.find('llo'))
    print(str.find('Python'))
    # index与find类似，但找不到会报错
    print(str.index('llo'))
    # print(str.index('Python'))
    # 检查字符串开头
    print(str.startswith('He'))
    print(str.startswith('Hl'))
    # 检查字符串结尾
    print(str.endswith('!'))
    # 在两侧填充指定字符
    print(str.center(50, '*'))
    # 左侧填充
    print(str.rjust(50, '*'))
    
    str2 = 'abc123456'
    # 下标取字符
    print(str2[2])
    # 切片
    print(str2[2:5])
    print(str2[2:])
    print(str2[2::2])
    print(str2[::2])
    print(str2[::-1])
    print(str2[-3:-1])
    # 判断是否是数字
    print(str2.isdigit())
    # 判断是否字母
    print(str2.isalpha())
    # 判断是否数字+字母
    print(str2.isalnum())
    str3 = '  jackfrued@126.com '
    # 修剪两侧空格
    print(str3.strip())


if __name__ == '__main__':
    main()
