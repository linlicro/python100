#!/usr/bin/python3

"""
Craps赌博游戏。

version: 0.1
author: icro
"""

from random import randint


def roll():
    total = 0
    total += randint(1, 6)
    total += randint(1, 6)
    return total


def craps():
    first = roll()
    if first == 7 or first == 12:
        print("玩家掷了 %d, WIN!" % first)
    elif first == 2 or first == 3 or first == 12:
        print("玩家掷了 %d, LOST!" % first)
    else:
        print("玩家掷了 %d, 游戏继续！" % first)
        game_over = False
    while not game_over:
        current = roll()
        if current == 7:
            print("玩家掷了 %d, LOST!" % current)
            break
        if current == first:
            print("玩家掷了 %d, WIN!" % current)
            break


craps()
