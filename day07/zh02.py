#!/usr/bin/python3

"""
综合案例2：约瑟夫环问题

version: 0.1
author: icro
"""


def main():
    persons = [True] * 30
    out_count, index, count = 0, 0, 0
    while out_count < 15:
        if persons[index]:
            count += 1
            if count == 9:
                persons[index] = False
                out_count += 1
                count = 0
        index += 1
        index %= 30
    for person in persons:
        print("Y" if person else "N", end=" ")
    print()


if __name__ == "__main__":
    main()
