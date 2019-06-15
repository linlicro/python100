#!/usr/bin/python3

"""
访问网络API获取国内新闻

前绝大多数网络数据服务（或称之为网络API）都是基于HTTP协议提供JSON格式的数据，
关于HTTP协议的相关知识，可以看看阮一峰老师的[《HTTP协议入门》](http://www.ruanyifeng.com/blog/2016/08/http.html)，
如果想了解国内的网络数据服务，可以看看[聚合数据](https://www.juhe.cn/)和[阿凡达数据](https://www.avatardata.cn/)等网站，
国外的可以看看[{API}Search](http://apis.io/)网站。

下面的例子演示了如何使用requests模块（封装得足够好的第三方网络访问模块）访问网络API获取国内新闻，
如何通过json模块解析JSON数据并显示新闻标题，这个例子使用了天行数据提供的国内新闻数据接口，
其中的APIKey需要自己到该网站申请。

要了解更多的关于Python异常机制的知识 >>>>
    segmentfault上面的文章[《总结：Python中的异常处理》](https://segmentfault.com/a/1190000007736783)

version: 0.1
author: icro
"""

import json
import requests


def main():
    resp = requests.get(
        'http://api.tianapi.com/guonei/?\
        key=APIKEY&num=10')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])


if __name__ == "__main__":
    main()
