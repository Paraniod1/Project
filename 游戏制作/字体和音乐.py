# @Time: 2020/11/26 11:48
# @Author: 李 巍
# @File :事件处理_键盘.py
# @Software: PyCharm

import pygame
import sys
from pygame.locals import *
import time
import random

pygame.init()

size = width,height = (400,600)

pygame.display.set_caption("逆行飙车")
screen = pygame.display.set_mode(size)


#定义颜色
BLACK = (0,0,0)
RED = "#FF0000"

SCORE = 0


#设置图像的帧速率
FPS = 60
clock = pygame.time.Clock()

#设置字体和文字
font_big = pygame.font.SysFont("华文彩云",60)                # 定义字体类型和大小
font_small = pygame.font.SysFont("Verdana",20)             # 定义字体类型和大小
game_over = font_big.render("游戏结束",True,BLACK)           # 将文字内容和字体内容绑定


#播放背景音乐
pygame.mixer.Sound("background.wav").play(-1)     #背景音乐默认执行1遍，参数loop默认为0，-1表示无限循环



class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super(Enemy, self).__init__()       #调用父类的__init__方法初始化对象
        self.image =  pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect(left=100,top = 0)

    def move(self):
        global SCORE                              # 引用全局变量
        self.rect.move_ip(0,5)
        if self.rect.top > height:                # 躲过小车加一分
            SCORE += 1
            self.rect = self.image.get_rect(left = random.randint(20, 360), top = 0)    # 超出边界重头开始 利用随机数，位置不定



#定义玩家类
class Player(pygame.sprite.Sprite):

    def __init__(self):
        #super(Player, self).__init__()       #调用父类的__init__方法初始化对象
        super().__init__()
        x,y = (200, 540)
        self.image =  pygame.image.load("Player.png")
        self.rect = self.image.get_rect(center = (x,y))

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)

        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)


#加载背景图片
background = pygame.image.load("AnimatedStreet.png")

#定义玩家对象
player = Player()
enemy = Enemy()

#定义敌人精灵组
enemies = pygame.sprite.Group()
enemies.add(enemy)

#将所有精灵放到一个组中
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)

if __name__ == "__main__":
    while True:
        #绘制图像
        screen.blit(background,(0,0))
        scores  = font_small.render(str(SCORE),True,BLACK)
        screen.blit(scores,(10,10))                    # 将分数显示出来


        # 统一对所有的精灵进行图像绘制，角色移动的方法调用
        for sprite in all_sprites:
            screen.blit(sprite.image, sprite.rect)
            sprite.move()


        #从事件队列中取出事件对象，根据类型进行事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        #撞击后，游戏结束
        if pygame.sprite.spritecollideany(player,enemies):

            pygame.mixer.Sound("crash.wav").play()             # 播放一次
            time.sleep(0.01)

            screen.fill(RED)                                   # 红色填充
            screen.blit(game_over, (80,150))


            pygame.display.update()
            time.sleep(2)

            pygame.quit()
            sys.exit()

        pygame.display.update()
        clock.tick(FPS)         # 按照指定的更新速率CLOCK来刷新画面，没到时间就让循环等待