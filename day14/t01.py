#!/usr/bin/python3

"""
requests的使用姿势

version: 0.1
author: icro
"""

from threading import Thread


import requests


# 继承Thread类创建自定义的线程类
class DownloadHandler(Thread):

    def __init__(self, url):
        super().__init__()
        self._url = url

    def run(self):
        filename = self._url[self._url.rfind('/') + 1:]
        resp = requests.get(self._url)
        with open('/Users/Lin/Downloads' + filename, 'wb') as f:
            f.write(resp.content)


def main():
    # 通过requests模块的get函数获取网络资源
    # 下面的代码中使用了天行数据接口提供的网络API
    # 要使用该数据接口需要再天行数据的网站上注册
    # 然后用自己的Key替换掉下面代码中APIKey
    resp = requests.get('http://api.tianapi.com/meinv/?key=APIKey&num=10')
    # 将服务器返回的JSON格式的数据解析为字典
    data_model = resp.json()
    for mm_dict in data_model['newlist']:
        url = mm_dict['picUrl']
        # 通过多线程的方式实现图片下载
        DownloadHandler(url).start()


if __name__ == "__main__":
    main()
