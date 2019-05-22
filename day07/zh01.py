#!/usr/bin/python3

"""
案例1：双色球选号

version: 0.1
author: icro
"""

from random import randint, sample


def dispay(balls):
    """
    输出双色球号码
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print("|", end=" ")
        print("%02d" % ball, end=" ")
    print()


def select_random():
    """
    随机选一组号
    """
    red_balls = [x for x in range(1, 34)]
    select_balls = sample(red_balls, 6)
    select_balls.sort()
    select_balls.append(randint(1, 16))
    return select_balls


if __name__ == "__main__":
    n = int(input("机选几注: "))
    for _ in range(n):
        dispay(select_random())
