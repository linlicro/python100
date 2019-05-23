#!/usr/bin/python3

"""
类的使用

version: 0.1
author: icro
"""


class Student(object):

    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print("%s正常学习%s." % (self.name, course_name))

    def watch_tv(self):
        if self.age < 18:
            print("%s只能看动画片" % self.name)
        else:
            print("%s可以看美国大片" % self.name)


def main():
    student1 = Student("jack", 35)
    student1.study("Python")
    student1.watch_tv()
    student2 = Student("icro", 10)
    student2.study("任正非思想")
    student2.watch_tv()


if __name__ == "__main__":
    main()
