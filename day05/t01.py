#!/usr/bin/python3

"""
寻找“水仙花数”

version: 0.1
author: icro
"""


def narcissistic_number(num):
    length = len(str(num))
    count = length
    num_sum = 0
    while count:
        num_sum += ((num // 10 ** (count - 1)) % 10) ** length
        count -= 1
    else:
        if num_sum == num:
            print("%d is %d bit narcissistic_number" % (num, length))
        else:
            print("%d is not a narcissistic_number" % num)
    return 0


num = int(input("num = "))
res = int(0)
temp = num
while temp > 0:
    x = temp % 10
    res += x * x * x
    temp //= 10
is_narcissistic_number = False
if res == num:
    is_narcissistic_number = True
print("%d是否为水仙花数字? %r" % (num, is_narcissistic_number))
narcissistic_number(num)
