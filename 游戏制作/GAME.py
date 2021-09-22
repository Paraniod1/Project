# @Time: 2020/11/26 11:48
# @Author: chao
# @File :事件处理_键盘.py
# @Software: PyCharm

import pygame
import sys
from pygame.locals import *
import time
import random



class Constant():
    # 定义窗口的大小
    SIZE = WIDTH, HEIGHT = (400, 600)
    # 定义颜色
    BLACK = (0, 0, 0)
    RED = "#FF0000"
    # 得分
    SCORE = 0
    # 设置图像的帧速率
    FPS = 60
    # 敌人的速度
    SPEED = 5




class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        x, y = (random.randint(25, 370), 0)
        super(Enemy, self).__init__()       # 调用父类的__init__方法初始化对象
        self.surf = pygame.Surface((42, 70))     # 自定义一个比物体小的Surface对象
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.surf.get_rect(center = (x, y))  # 根据自定义的surf创建rect

    def move(self):
        global SCORE                              # 引用全局变量
        self.rect.move_ip(0, Constant.SPEED)
        if self.rect.top > Constant.HEIGHT:                # 躲过小车加一分
            Constant.SCORE += 1
            self.rect = self.image.get_rect(top = 0, left =random.randint(22, 378))    # 超出边界重头开始 利用随机数，位置不定



#定义玩家类
class Player(pygame.sprite.Sprite):

    def __init__(self):
      #调用父类的__init__方法初始化对象
        super().__init__()
        self.image =  pygame.image.load("Player.png")
        self.surf = pygame.Surface((42, 70))  # 自定义一个比物体小的Surface对象
        self.rect = self.surf.get_rect(left =178, bottom = Constant.HEIGHT - 21)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP] and self.rect.top >= 0:      # 顶部不能超过y
            self.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_DOWN] and self.rect.bottom <= Constant.HEIGHT-21:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT] and self.rect.left >= 0:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT] and self.rect.right <= Constant.WIDTH-4:
            self.rect.move_ip(5, 0)



class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("逆行飙车")
        self.screen = pygame.display.set_mode(Constant.SIZE)
        # 加载背景图片
        self.background = pygame.image.load("AnimatedStreet.png")
        # 播放背景音乐
        pygame.mixer.Sound("background.wav").play(-1)         # 背景音乐默认执行1遍，参数loop默认为0，-1表示无限循环
        # 设置字体和文字
        self.font_big = pygame.font.SysFont("华文彩云", 60)         # 定义字体类型和大小
        self.font_small = pygame.font.SysFont("Verdana", 20)       # 定义字体类型和大小
        self.game_over = self.font_big.render("游戏结束", True, Constant.BLACK)   # 将文字内容和字体内容绑定
        # 用户自定义事件
        self.SPEED_UP = pygame.USEREVENT + 1
        pygame.time.set_timer(self.SPEED_UP, 1000)                 # 每隔1s将事件放在队列一次
        self.clock = pygame.time.Clock()

    def run(self):
        # 定义玩家对象
        player = Player()
        enemy = Enemy()

        #定义敌人精灵组
        enemies = pygame.sprite.Group()
        enemies.add(enemy)

        #将所有精灵放到一个组中
        all_sprites = pygame.sprite.Group()
        all_sprites.add(player)
        all_sprites.add(enemy)

        while True:
            # 绘制图像
            self.screen.blit(self.background, (0, 0))
            self.scores = self.font_small.render(str(Constant.SCORE), True, Constant.BLACK)
            self.screen.blit(self.scores, (10, 10))  # 将分数显示出来

            # 统一对所有的精灵进行图像绘制，角色移动的方法调用
            for sprite in all_sprites:
                self.screen.blit(sprite.image, sprite.rect)
                sprite.move()


            # 从事件队列中取出事件对象，根据类型进行事件处理
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == self.SPEED_UP:
                    Constant.SPEED += 0.5

            # 撞击后，游戏结束
            if pygame.sprite.spritecollideany(player, enemies):
                pygame.mixer.Sound("crash.wav").play()  # 播放一次
                time.sleep(1)

                self.screen.fill(Constant.RED)  # 红色填充
                self.screen.blit(self.game_over, (80, 150))

                pygame.display.update()
                time.sleep(2)

                pygame.quit()
                sys.exit()

            pygame.display.update()
            self.clock.tick(Constant.FPS)  # 按照指定的更新速率CLOCK来刷新画面，没到时间就让循环等待






if __name__ == "__main__":
    game = Game()
    game.run()