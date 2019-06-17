#!/usr/bin/python3

"""
使用正则表达式

基础知识 参考: 《正则表达式30分钟入门教程》(https://deerchao.net/tutorials/regex/regex.htm)

Python提供了re模块来支持正则表达式相关操作

函数:

* compile(pattern, flags=0) % 编译正则表达式返回正则表达式对象
* match(pattern, string, flags=0) % 用正则表达式匹配字符串 成功返回匹配对象 否则返回None
* search(pattern, string, flags=0) % 搜索字符串中第一次出现正则表达式的模式 成功返回匹配对象 否则返回None
* split(pattern, string, maxsplit=0, flags=0) % 用正则表达式指定的模式分隔符拆分字符串 返回列表
* sub(pattern, repl, string, count=0, flags=0) %
用指定的字符串替换原字符串中与正则表达式匹配的模式 可以用count指定替换的次数
* fullmatch(pattern, string, flags=0) % match函数的完全匹配（从字符串开头到结尾）版本
* findall(pattern, string, flags=0) % 查找字符串所有与正则表达式匹配的模式 返回字符串的列表
* finditer(pattern, string, flags=0) % 查找字符串所有与正则表达式匹配的模式 返回一个迭代器
* purge() % 清除隐式编译的正则表达式的缓存
* re.I / re.IGNORECASE % 忽略大小写匹配标记
* re.M / re.MULTILINE % 多行匹配标记

version: 0.1
author: icro
"""
import re


def main():
    """验证输入用户名和QQ号是否有效并给出对应的提示信息
    """
    username = input('请输入用户名: ')
    qq = input('请输入QQ: ')
    # match函数的第一个参数是正则表达式字符串或正则表达式对象
    # 第二个参数是要跟正则表达式做匹配的字符串对象
    # 使用了“原始字符串”的写法（在字符串前面加上了r）
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    if not m1:
        print('请输入有效的用户名.')
    m2 = re.match(r'[1-9]\d{4,11}$', qq)
    if not m2:
        print('请输入有效的QQ号.')
    if m1 and m2:
        print('你输入的信息是有效的！')


if __name__ == "__main__":
    main()
