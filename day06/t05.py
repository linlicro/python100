#!/usr/bin/python3

"""
判断输入的正整数是不是回文素数

version: 0.1
author: icro
"""


def foo():
    b = "hello"  # local variable

    def bar():  # Python中可以在函数内部再定义函数
        c = True
        print(a)
        print(b)  # 嵌套作用域
        print(c)

    bar()
    # print(c)  # NameError: name 'c' is not defined


if __name__ == "__main__":
    a = 100  # global variable
    # print(b)  # NameError: name 'b' is not defined
    foo()

# 标准代码格式 ==>
# def main():
#     # Todo: Add your code here
#     pass


# if __name__ == '__main__':
#     main()
