#!/usr/bin/python3

"""
类的继承

version: 0.1
author: icro
"""


class Person(object):
    """
    人
    """

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print("%s正在愉快的玩耍", self._name)

    def watch_tv(self):
        if self.age < 18:
            print("%s只能看动画片" % self.name)
        else:
            print("%s可以看美国大片" % self.name)


class Student(Person):
    """学生"""

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print("%s的%s正在学习%s" % (self._grade, self._name, course))


class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self, title):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print("%s%s正在讲%s." % (self._name, self._title, course))


def main():
    stu = Student("icro", 15, "二年级")
    stu.study("数学")
    stu.watch_tv()
    t = Teacher("jack", 30, "叫兽")
    t.teach("数学")
    t.watch_tv()


if __name__ == "__main__":
    main()
