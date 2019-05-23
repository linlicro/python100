#!/usr/bin/python3

"""
访问可见性问题

在Python中，属性和方法的访问权限只有两种，也就是公开的和私有的，如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头，下面的代码可以验证这一点。

version: 0.1
author: icro
"""


class Test:
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print("__bar")


def main():
    test = Test("hello")
    # AttributeError: 'Test' object has no attribute '__bar'
    # test.__bar()
    # AttributeError: 'Test' object has no attribute '__foo'
    # print(test.__foo)
    """
    Python并没有从语法上严格保证私有属性或方法的私密性，
    它只是给私有的属性和方法换了一个名字来“妨碍”对它们的访问，
    事实上如果你知道更换名字的规则仍然可以访问到它们，
    下面的代码就可以验证这一点。之所以这样设定，
    可以用这样一句名言加以解释，
    就是“We are all consenting adults here”。
    因为绝大多数程序员都认为开放比封闭要好，而且程序员要自己为自己的行为负责。
    """
    test._Test__bar()
    print(test._Test__foo)


if __name__ == "__main__":
    main()
