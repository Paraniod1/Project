# -*- codeing = utf-8 -*-
# @Time : 2021/8/8 19:52
# @Author : chao
# @File : 图像绘制.py
# @Software : PyCharm

import pygame
import sys

pygame.init()  # pygame 初始化

size = width, height = 300, 300
pygame.display.set_caption("图形绘制")             # 窗口的名称
screen = pygame.display.set_mode(size)           # 创建一个窗口对象 设置参数以元组传入

# 定义颜色变量
WHITE = pygame.color.Color(255, 255, 255)        # 定义白色常量
BLACK = pygame.color.Color(0, 0, 0, a=255)       # 定义黑色常量 alpha通道默认255，不透明
RED = "#FF0000"                                  # 定义红色        十六进制
GREEN = "0x00FF00"                               # 定义绿色
BLUE = (0, 0, 255)                               # 定义蓝色 也可以是列表[0, 0, 255]

screen.fill(WHITE)                               # 窗口填充白色


while True:
    # 画线 蓝色 起点(150,130) 终点(130,170)
    pygame.draw.line(screen, BLUE, (150, 130), (130, 170))
    # 画线 蓝色 起点(150,130) 终点(170,170)
    pygame.draw.line(screen, BLUE, (150, 130), (170, 170))
    # 画线 蓝色 起点(130,170) 终点(170,170)
    pygame.draw.line(screen, GREEN, (130, 170), (170, 170))
    # 画圆 黑色 圆心：(100,50) ,半径 30
    pygame.draw.circle(screen, BLACK, (100, 50), 30)
    # 画圆 黑色 圆心：(200,50) ,半径 30
    pygame.draw.circle(screen, BLACK, (200, 50), 30)
    # 画正方形 红色 左上方（100，200） 宽 100 高50 边框宽度为2的空心矩形
    pygame.draw.rect(screen, RED, (100, 200, 100, 50), 2)

    for event in pygame.event.get():              # 从pygame的事件队列中获取事件对象
        if event.type == pygame.QUIT:             # pygame.QUIT是一个常量，数值为256，表示事件类型为退出pygame
            pygame.quit()                         # pygame退出，和pygame.init()对应
            sys.exit()                            # 如果系统在pygame.quit()前终止，IDLE会挂起，一般最后调用sys.exit()
    pygame.display.update()                       # 不断重新刷新界面