#!/usr/bin/python3

"""
实现TCP服务器: 服务器是能够同时接纳和处理多个用户请求的。

设计一个使用多线程技术处理多个用户请求的服务器，该服务器会向连接到服务器的客户端发送一张图片。

version: 0.1
author: icro
"""

from socket import socket
from base64 import b64encode
from json import dumps
from threading import Thread


def main():

    # 自定义线程类
    class FileTransferHandler(Thread):

        def __init__(self, cclient):
            super.__init__()
            self._cclient = cclient

        def run(self):
            my_dict = {}
            my_dict['filename'] = 'xxx.icon'
            # JSON是纯文本不能携带二进制数据
            # 所以图片的二进制数据要处理成base64编码
            my_dict['filedata'] = data
            # 通过dumps函数将字典处理成JSON字符串
            json_str = dumps(my_dict)
            # 发送JSON字符串
            self._cclient.send(json_str.encode('utf-8'))
            self._cclient.close()

    # 1. 创建套接字对象并指定使用哪种传输服务
    server = socket()
    # 2. 绑定IP地址和端口(区分不同的服务)
    server.bind('127.0.0.1', 5566)
    # 3. 开启监听 - 监听客户端连接到服务器
    server.listen(512)
    print('服务器启动开始监听...')
    with open('xxxx.icon', 'rb') as f:
        # 将二进制数据处理成base64在解码成字符串
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        # 启动一个线程来处理客服端请求
        FileTransferHandler(client).start()


if __name__ == "__main__":
    main()
