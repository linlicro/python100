#!/usr/bin/python3

"""
练习1：在屏幕上显示跑马灯文字

version: 0.1
author: icro
"""

import os
import time


def main():
    content = "杭州欢迎你为你开天辟地......"
    while True:
        os.system("clear")
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == "__main__":
    main()
