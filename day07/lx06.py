#!/usr/bin/python3

"""
练习6：打印杨辉三角。

version: 0.1
author: icro
"""


def main():
    row = int(input("number of rows: "))
    yh = [[]] * row
    for each_row in range(len(yh)):
        yh[each_row] = [None] * (each_row + 1)
        for each_col in range(len(yh[each_row])):
            if each_col == 0 or each_col == each_row:
                yh[each_row][each_col] = 1
            else:
                yh[each_row][each_col] = (
                    yh[each_row - 1][each_col] + yh[each_row - 1][each_col - 1]
                )
            print(yh[each_row][each_col], end="\t")
        print()


if __name__ == "__main__":
    main()
