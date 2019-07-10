#!/usr/bin/python3

"""
使用 TCP套接字 实现了一个提供时间日期的服务器

我们通常将HTTP服务跟80端口绑定，而MySQL数据库服务默认绑定在3306端口，
这样当服务器收到用户请求时就可以根据端口号来确定到底用户请求的是HTTP服务器还是数据库服务器提供的服务。
端口的取值范围是0~65535，而1024以下的端口我们通常称之为“著名端口”
（留给像FTP、HTTP、SMTP等“著名服务”使用的端口，有的地方也称之为“周知端口”），
自定义的服务通常不使用这些端口，除非自定义的是HTTP或FTP这样的著名服务。

version: 0.1
author: icro
"""

from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime


def main():
    # 1. 创建套接字对象并指定使用哪种传输服务
    # family=AF_INET - IPv4地址
    # family=AF-INET6 - IPv6地址
    # type=SOCK_STREAM - TCP套接字
    # type=SOCK_DGRAM - UDP套接字
    # type=SOCK_RAW - 原始套接字
    server = socket(family=AF_INET, type=SOCK_STREAM)
    # 2. 绑定IP地址和端口(端口用于区分不同的服务)
    # 同一时间在同一个端口上只能绑定一个服务否则报错
    server.bind(('127.0.0.1', 6789))
    # 3. 开启监听 - 监听客户端连接到服务器
    # 参数512可以理解为连接队列的大小
    server.listen(512)
    print('服务器启动开始监听...')
    while True:
        # 4. 通过循环接收客户端的连接并作出相应的处理(提供服务)
        # accept方法是一个阻塞方法如果没有客户端连接到服务器代码不会向下执行
        # accept方法返回一个元组其中的第一个元素是客户端对象
        # 第二个元素是连接到服务器的客户端的地址(由IP和端口两部分构成)
        client, addr = server.accept()
        print(str(addr) + '连接到了服务器')
        # 5. 发送数据
        client.send(str(datetime.now()).encode('utf-8'))
        # 6. 断开连接
        client.close()


if __name__ == "__main__":
    main()
