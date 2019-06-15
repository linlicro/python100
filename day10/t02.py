#!/usr/bin/python3

"""
使用Pygame进行游戏开发

Pygame是一个开源的Python模块，专门用于多媒体应用（如电子游戏）的开发，
其中包含对图像、声音、视频、事件、碰撞等的支持。

下面我们来完成一个简单的小游戏，游戏的名字叫“大球吃小球”，
当然完成这个游戏并不是重点，学会使用Pygame也不是重点，
最重要的我们要在这个过程中体会如何使用前面讲解的面向对象程序设计，
学会用这种编程思想去解决现实中的问题。

version: 0.1
author: icro
"""


import pygame


def main():
    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    # 定义变量来标识小球在屏幕上的位置
    x, y = 50, 50
    # 设置窗口的背景色(颜色是由红绿蓝三原色构成的元组)
    # screen.fill((242, 242, 242))
    # 通过指定的文件名加载图像
    # ball_image = pygame.image.load('./res/ball.png')
    # 绘制一个圆(参数分别是: 屏幕, 颜色, 圆心位置, 半径, 0表示填充圆)
    # pygame.draw.circle(screen, (255, 0, 0), (100, 100), 30, 0)
    # 在窗口上渲染图像
    # screen.blit(ball_image, (50, 50))
    # 刷新当前窗口(渲染窗口将绘制的图像呈现出来)
    # pygame.display.flip()
    running = True
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # 设置窗口的背景色(颜色是由红绿蓝三原色构成的元组)
        screen.fill((242, 242, 242))
        # 绘制一个圆(参数分别是: 屏幕, 颜色, 圆心位置, 半径, 0表示填充圆)
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 30, 0)
        pygame.display.flip()
        # 每隔50毫秒就改变小球的位置再刷新窗口
        pygame.time.delay(50)
        x, y = x + 5, y + 5


if __name__ == "__main__":
    main()
