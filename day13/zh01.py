#!/usr/bin/python3

"""
Python中的多线程

例子1：将耗时间的任务放到线程中以获得更好的用户体验。

有“下载”和“关于”两个按钮，用休眠的方式模拟点击“下载”按钮会联网下载文件需要耗费10秒的时间，
如果不使用“多线程”，我们会发现，当点击“下载”按钮后整个程序的其他部分都被这个耗时间的任务阻塞而无法执行了，
这显然是非常糟糕的用户体验。

version: 0.1
author: icro
"""

import time
import tkinter
import tkinter.messagebox
from threading import Thread

# ===================
# def download():
#     # 模拟下载任务需要花费10秒时间
#     time.sleep(10)
#     tkinter.messagebox.showinfo('提示', '下载完成!')


# def show_about():
#     tkinter.messagebox.showinfo('关于', '作者: icro(v1.0)')


# def main():
#     top = tkinter.Tk()
#     top.title('单线程')
#     top.geometry('200x150')
#     top.wm_attributes('-topmost', True)

#     pannel = tkinter.Frame(top)
#     button1 = tkinter.Button(pannel, text='下载', command=download)
#     button1.pack(side='left')
#     button2 = tkinter.Button(pannel, text='关于', command=show_about)
#     button2.pack(side='right')
#     pannel.pack(side='bottom')

#     tkinter.mainloop()
# ===================

def main():

    class DownloadTaskHandler(Thread):

        def run(self):
            # 模拟下载任务需要花费10秒时间
            time.sleep(10)
            tkinter.messagebox.showinfo('提示', '下载完成!')
            # 启用下载按钮
            button1.config(state=tkinter.NORMAL)

    def download():
        # 禁用下载按钮
        button1.config(state=tkinter.DISABLED)
        # 通过daemon参数将线程设置为守护线程(主程序退出就不再保留执行)
        # 在线程中处理耗时间的下载任务
        DownloadTaskHandler(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('关于', '作者: icro(v1.0)')

    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    pannel = tkinter.Frame(top)
    button1 = tkinter.Button(pannel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(pannel, text='关于', command=show_about)
    button2.pack(side='right')
    pannel.pack(side='bottom')
    tkinter.mainloop()


if __name__ == "__main__":
    main()
