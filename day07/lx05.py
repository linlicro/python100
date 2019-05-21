#!/usr/bin/python3

"""
练习5：计算指定的年月日是这一年的第几天

version: 0.1
author: icro
"""


def is_leap_year(year):
    """
    判断指定的年份是不是闰年

    :param year: 年份
    :return: 闰年返回True平年返回False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, day):
    """
    计算传入的日期是这一年的第几天

    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第几天
    """
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    ][is_leap_year(year)]
    total = 0
    for m in range(month - 1):
        total += days_of_month[m]
    return total + day


def main():
    print(which_day(1990, 11, 30))
    print(which_day(1999, 10, 10))
    print(which_day(2010, 3, 1))


if __name__ == "__main__":
    main()
