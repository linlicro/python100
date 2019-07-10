#!/usr/bin/python3

"""
发送电子邮件

smptlib is part of
[python's standard library](https://docs.python.org/2/library/)

遇到问题:

* 错误反馈码: 554 DT:SPM

version: 0.1
author: icro
"""

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


def main():
    sender = 'test@126.com'  # 'what is your gmail address?'
    receivers = [
        'xxxx@qq.com']
    message = MIMEText('body', 'plain', 'utf-8')
    message['From'] = Header('xxxx@126.com', 'utf-8')
    message['To'] = Header('xxxxx@qq.com', 'utf-8')
    message['Subject'] = Header('示例', 'utf-8')
    smtper = SMTP('smtp.126.com')
    smtper.login(sender, 'secretpass')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送成功！')


if __name__ == "__main__":
    main()
