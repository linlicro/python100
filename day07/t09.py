#!/usr/bin/python3

"""
使用集合:
    使用字典

version: 0.1
author: icro
"""


def main():
    scores = {"icro": 95, "jack": 88, "rose": 70}
    # 获取数据
    print(scores["icro"])
    print(scores["jack"])
    # 遍历
    for elem in scores:
        print("%s\t-->\t%s" % (elem, scores[elem]))
    # 更新
    scores["icro"] = 60
    scores["todde"] = 99
    scores.update(susan=10, jjlin=0)
    print(scores)
    if "icro" in scores:
        print(scores["icro"])
    print(scores.get("icro"))
    # get方法也是通过键获取对应的值但是可以设置默认值
    print(scores.get("icro", 100))
    # 删除
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop("jack", 100))
    # 清空
    scores.clear()
    print(scores)


if __name__ == "__main__":
    main()
