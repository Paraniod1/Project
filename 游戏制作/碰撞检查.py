# -*- codeing = utf-8 -*-
# @Time : 2021/8/9 14:07
# @Author : chao
# @File : 事件处理--键盘.py
# @Software : PyCharm


import pygame
import sys
from pygame.locals import*

pygame.init()

size = width, height = (400, 600)

pygame.display.set_caption("逆行飙车")
screen = pygame.display.set_mode(size)
background = pygame.image.load("AnimatedStreet.png")   # 将图片保持在内存中 绘制背景图面
FPS = 30                                               # 设置每秒刷新的次数 图像的帧数率
clock = pygame.time.Clock()                            # 返回一个时钟对象

# 1.角色类继承Sprite
# 2.应用父类__init__方法初始化对象
# 3.定义精灵组
# 4.碰撞检测及处理

# 定义敌人类
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()          # 调用父类的初始化对象
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect(left = width/2 - 22, top = 0)

    def move(self):
        self.rect.move_ip(0, 5)

# 定义玩家类
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()                    # 调用父类的初始化对象
        x, y = (width/2, height/2)                   # 屏幕的中心距离
        self.image = pygame.image.load("Player.png")   # 将图片素材加载到内存
        self.rect = self.image.get_rect(center = (x, y))  # 将rect对象的中心点，定位在(x,y)处


    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)

        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)

        if pressed_keys[K_LEFT]:
            self.rect.move_ip((-5), 0)

        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)


# 定义玩家对象
player = Player()                                      # 创建Player的对象，改变图像的所在的位置
enemy = Enemy()

# 定义敌人组对象
enemies = pygame.sprite.Group()
enemies.add(enemy)

# 将所有精灵放到一个组
all_sprites = pygame.sprite.Group()
all_sprites.add(enemy)
all_sprites.add(player)

while True:

    # 绘制图像
    screen.blit(background, (0, 0))               # 将图片渲染在指定的位置

    # 统一对所有精灵进行图像绘制，和角色移动的方法调用
    for sprite in all_sprites:
        screen.blit(sprite.image, sprite.rect)
        sprite.move()


    for event in pygame.event.get():              # 从pygame的事件队列中获取事件对象
        if event.type == pygame.QUIT:             # pygame.QUIT是一个常量，数值为256，表示事件类型为退出pygame
            pygame.quit()                         # pygame退出，和pygame.init()对应
            sys.exit()                            # 如果系统在pygame.quit()前终止，IDLE会挂起，一般最后调用sys.exit()

    # 敌人和玩家都存在
   # if pygame.sprite.spritecollide(player, enemies, False):
   #     print("撞车了......")


    # 敌人消失
    # if pygame.sprite.spritecollide(player, enemies, True):   # True表示将敌人从精灵组中删除
    #     print("撞车了")

    # 玩家和敌人消失
    # if pygame.sprite.spritecollide(player, enemies, True):
    #     player.kill()                                            # 单独控制某个精灵 是从精灵组中删除 还存在内存中
    #     print("都死光了...")


    # 玩家消失
    if pygame.sprite.spritecollideany(player, enemies):  # 该方法只有俩个参数
        player.kill()
        #enemy.kill()
        print("游戏结束")

    # 从每个组中删除精灵。不影响精灵的状态，还可以重新添加到Group中。
    if player not in all_sprites:
        all_sprites.add(player)

    pygame.display.update()                       # 不断重新刷新界面
    clock.tick(FPS)                               # 按照指定的更新速率来属性界面，没到时间就让它循环等待