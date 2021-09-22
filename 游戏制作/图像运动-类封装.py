# -*- codeing = utf-8 -*-
# @Time : 2021/8/8 21:25
# @Author : chao
# @File : 图像运动-类封装.py
# @Software : PyCharm

import pygame
import sys

pygame.init()

size = width, height = (400, 600)

pygame.display.set_caption("图像绘制")
screen = pygame.display.set_mode(size)

# 对游戏角色封装
class Player():
    def __init__(self):
        x, y = (178, 504)                   # 屏幕的中心距离
        self.image = pygame.image.load("Player.png")   # 将图片素材加载到内存
        self.rect = self.image.get_rect(center = (x, y))  # 将rect对象的中心点，定位在(x,y)处
        #self.rect = self.image.get_rect(top = 200, left = 200)   # 默认是定位在(0,0),还可以结合其他rect的属性定位显示位置

    def move(self):
        #self.rect.y -= 1                               # 直接修改rect对象的y坐标
        #self.rect = self.rect.move(0, -1)              # 使用 rect对象的move方法，设定移动增长量，返回移动后的rect对象
        self.rect.move_ip(0, -2)                       # 直接对当前rect对象移动指定数值的位移 负数表示x向左，y向上

background = pygame.image.load("AnimatedStreet.png")   # 将图片保持在内存中 绘制背景图面

FPS = 30                                               # 设置每秒刷新的次数 图像的帧数率
clock = pygame.time.Clock()                            # 返回一个时钟对象

player = Player()                                      # 创建Player的对象，改变图像的所在的位置

while True:

    screen.blit(background, (0, 0))               # 将图片渲染在指定的位置
    screen.blit(player.image, player.rect)        # 将player对象的image 渲染到player中指定的rect区域
    player.move()                                 # 不断的调用move()方法，


    for event in pygame.event.get():              # 从pygame的事件队列中获取事件对象
        if event.type == pygame.QUIT:             # pygame.QUIT是一个常量，数值为256，表示事件类型为退出pygame
            pygame.quit()                         # pygame退出，和pygame.init()对应
            sys.exit()                            # 如果系统在pygame.quit()前终止，IDLE会挂起，一般最后调用sys.exit()
    pygame.display.update()                       # 不断重新刷新界面
    clock.tick(FPS)                               # 按照指定的更新速率来属性界面，没到时间就让它循环等待