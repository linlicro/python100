#!/usr/bin/python3

"""
使用正则表达式

从一段文字中提取出国内手机号码
电信号码: 133/153/180/181/189/177
联通号码: 130/131/132/155/156/185/186/145/176
移动号码: 134/135/136/137/138/139/150/151/152/157
            /158/159/182/183/184/187/188/147/178

version: 0.1
author: icro
"""
import re


def main():
    # 创建正则表达式对象
    # 使用了前瞻和回顾来保证手机号码前后不应该出现数字
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    # 查找所有匹配并保存到一个列表中
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print('--------华丽的分隔线--------')
    # 通过迭代器取出匹配对象并获得匹配的内容
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('--------华丽的分隔线--------')
    # 通过search函数指定搜索位置找出所有匹配
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())


if __name__ == "__main__":
    main()
