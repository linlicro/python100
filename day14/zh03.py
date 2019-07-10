#!/usr/bin/python3

"""
发送短信

使用了互亿无线(http://www.ihuyi.com/)短信平台

version: 0.1
author: icro
"""

import urllib.parse
import http.client
import json


host = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"

# 查看用户名 登录用户中心->验证码通知短信>产品总览->API接口信息->APIID
account = "用户名"
# 查看密码 登录用户中心->验证码通知短信>产品总览->API接口信息->APIKEY
password = "密码"


def main():
    params = urllib.urlencode({'account': account, 'password': password,
                               'content': 'text', 'mobile': 'mobile',
                               'format': 'json'})
    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/plain"}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    jsonstr = response_str.decode('utf-8')
    print(json.loads(jsonstr))
    conn.close()


if __name__ == "__main__":
    main()
