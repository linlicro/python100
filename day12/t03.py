#!/usr/bin/python3

"""
替换字符串中的不良内容

version: 0.1
author: icro
"""
import re


def main():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
                      '*', sentence, flags=re.I)
    print(purified)


if __name__ == "__main__":
    main()