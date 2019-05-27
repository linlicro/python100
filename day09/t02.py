#!/usr/bin/python3

"""
__slots__魔法

Python是一门动态语言
动态语言允许我们在程序运行时给对象绑定新的属性或方法，当然也可以对已经绑定的属性和方法进行解绑定。
如果我们需要限定自定义类型的对象只能绑定某些属性，可以通过在类中定义__slots__变量来进行限定。
需要注意的是__slots__的限定只对当前类的对象生效，对子类并不起任何作用。

version: 0.1
author: icro
"""


class Person(object):

    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ("_name", "_age", "_gender")

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def watch_tv(self):
        if self.age < 18:
            print("%s只能看动画片" % self.name)
        else:
            print("%s可以看美国大片" % self.name)


def main():
    person = Person("icro", 12)
    person.watch_tv()
    person.age = 22
    person._gender = "男"
    person.watch_tv()
    # AttributeError: 'Person' object has no attribute '_is_gay'
    # person._is_gay = True


if __name__ == "__main__":
    main()
