#!/usr/bin/python3

"""
面向对象进阶

version: 0.1
author: icro
"""


class Person(object):
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
    person.watch_tv()
    # person.name = '白元芳'  # AttributeError: can't set attribute


if __name__ == "__main__":
    main()
