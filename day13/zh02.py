#!/usr/bin/python3

"""
Python中的多线程

例子2：使用多进程对复杂任务进行“分而治之”。

我们来完成1~100000000求和的计算密集型任务

version: 0.1
author: icro
"""

from multiprocessing import Process, Queue
from time import time

# 单线程循环计算
# def main():
#     total = 0
#     number_list = [x for x in range(1, 100000000)]
#     start = time()
#     for number in number_list:
#         total += number
#     print(total)
#     end = time()
#     print('Execution time: %.3fs' % (end - start))


def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)


def main():
    processes = []
    number_list = [x for x in range(1, 100000000)]
    result_queue = Queue()
    index = 0
    # 启动8个进程将数据切片后进行运算
    for _ in range(8):
        p = Process(target=task_handler, args=(
            number_list[index:index + 12500000], result_queue))
        index += 12500000
        processes.append(p)
        p.start()
    # 开始记录所有进程执行完成花费的时间
    start = time()
    for p in processes:
        p.join()
    # 合并结果
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('Execution time: %.3fs' % (end - start))


if __name__ == "__main__":
    main()
