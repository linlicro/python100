#!/usr/bin/python3

"""
实现两个进程间的通信:

我们启动两个进程，一个输出Ping，一个输出Pong，两个进程输出的Ping和Pong加起来一共10个。

# 子进程复制了父进程及其所有的数据结构，
# 每个子进程有自己独立的内存空间，
# 这也就意味着两个子进程中各有一个counter变量，所以结果也就可想而知了。
# def sub_task_notwork(string):
#     global counter
#     while counter < 10:
#         print(string, end='', flush=True)
#         counter += 1
#         sleep(0.01)

version: 0.1
author: icro
"""
from multiprocessing import Process, Queue
from time import sleep


def sub_task(q, string):
    counter = 0
    while counter < 5:
        q.put(string)
        counter += 1
        sleep(0.01)


def main():
    q = Queue()
    p1 = Process(target=sub_task, args=(q, 'Ping', ))
    p2 = Process(target=sub_task, args=(q, 'Pong', ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    while not q.empty():
        print(q.get(), end=' ', flush=True)


if __name__ == "__main__":
    main()
