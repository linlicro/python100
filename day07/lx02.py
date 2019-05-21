#!/usr/bin/python3

"""
练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。

version: 0.1
author: icro
"""

import random
import string


def generate_code(code_len=4):
    """
    生成指定长度的验证码

    :param code_len: 验证码长度(默认是4个字符)

    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = string.ascii_letters
    for n in range(0, 10):
        all_chars += str(n)
    last_pos = len(all_chars) - 1
    code = ""
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


if __name__ == "__main__":
    print(generate_code())
