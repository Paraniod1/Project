# -*- codeing = utf-8 -*-
# @Time : 2021/8/8 20:51
# @Author : chao
# @File : 运动实现.py
# @Software : PyCharm

import pygame
import sys

pygame.init()

size = width, height = (400, 600)

pygame.display.set_caption("图像绘制")
screen = pygame.display.set_mode(size)

background = pygame.image.load("AnimatedStreet.png")   # 将图片保持在内存中 绘制背景图面
player = pygame.image.load("Player.png")
x, y = 178, 504                                        # player的位置

FPS = 30                                               # 设置每秒刷新的次数 图像的帧数率
clock = pygame.time.Clock()                            # 返回一个时钟对象


while True:

    screen.blit(background, (0, 0))               # 将图片渲染在指定的位置
    screen.blit(player, (x, y))
    y -= 1


    for event in pygame.event.get():              # 从pygame的事件队列中获取事件对象
        if event.type == pygame.QUIT:             # pygame.QUIT是一个常量，数值为256，表示事件类型为退出pygame
            pygame.quit()                         # pygame退出，和pygame.init()对应
            sys.exit()                            # 如果系统在pygame.quit()前终止，IDLE会挂起，一般最后调用sys.exit()
    pygame.display.update()                       # 不断重新刷新界面
    clock.tick(FPS)                               # 按照指定的更新速率来属性界面，没到时间就让它循环等待