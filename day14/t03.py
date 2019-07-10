#!/usr/bin/python3

"""
实现TCP客户端的功能

需要注意的是，服务器并没有使用多线程或者异步I/O的处理方式，
这也就意味着当服务器与一个客户端处于通信状态时，其他的客户端只能排队等待。

version: 0.1
author: icro
"""

from socket import socket


def main():
    # 1.创建套接字对象默认使用IPv4和TCP协议
    client = socket()
    # 2.连接到服务器(需要制定IP地址和端口)
    client.connect(('127.0.0.1', 6789))
    # 3.从服务器接收数据
    print(client.recv(1024).decode('utf-8'))
    client.close()


if __name__ == "__main__":
    main()
