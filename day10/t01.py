#!/usr/bin/python3

"""
基于tkinter模块的GUI

Python默认的GUI开发模块是tkinter（在Python 3以前的版本中名为Tkinter），从这个名字就可以看出它是基于Tk的，
Tk是一个工具包，最初是为Tcl设计的，后来被移植到很多其他的脚本语言中，它提供了跨平台的GUI控件。

基本上使用tkinter来开发GUI应用需要以下5个步骤：

1. 导入tkinter模块中我们需要的东西。
2. 创建一个顶层窗口对象并用它来承载整个GUI应用。
3. 在顶层窗口对象上添加GUI组件。
4. 通过代码将这些GUI组件的功能组织起来。
5. 进入主事件循环(main loop)。

version: 0.1
author: icro
"""


import tkinter
import tkinter.messagebox


def main():
    flag = True

    # 修改标签上的文字
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ("red", "Hello world!")\
            if flag else ("blue", "Goobye, world!")
        label.config(text=msg, fg=color)

    # 确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel("温馨提示", "确认要退出吗?"):
            top.quit()

    # 确认退出
    top = tkinter.Tk()
    # 设置窗口大小
    top.geometry("240x160")
    # 设置窗口标题
    top.title("小游戏")
    # 创建标签对象并添加到顶层窗口
    label = tkinter.Label(top, text="Hello, world!",
                          font="Arial -32", fg="red")
    label.pack(expand=1)
    # 创建一个装按钮的容器
    panel = tkinter.Frame(top)
    # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
    button1 = tkinter.Button(panel, text="修改", command=change_label_text)
    button1.pack(side="left")
    button2 = tkinter.Button(panel, text="退出", command=confirm_to_quit)
    button2.pack(side="right")
    panel.pack(side="bottom")
    # 开启主事件
    tkinter.mainloop()


if __name__ == "__main__":
    main()
