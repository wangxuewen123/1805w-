#!/usr/bin/env python
# coding=utf-8
import pygame
import random
pygame.init()
#创建游戏窗口
screen = pygame.display.set_mode((500,800))
#把图片加载进来
bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))#绘制在屏幕的0,0位置
hero = pygame.image.load("./images/plane.png")#自己的飞机显示出来
screen.blit(hero,(200,500))#自己飞机的位置
pygame.display.update()
clock = pygame.time.Clock()
hero_rect = pygame.Rect(200,500,102,126)
#===================================================
"""游戏精灵基类"""
class GameSprite(pygame.sprite.Sprite):
    def __init__(self,image_name,speed=1):
        super().__init__()#调用父类的初始化方法
        #加载图像
        self.image = pygame.image.load(image_name)
        #设置尺寸
        self.rect = self.image.get_rect()
        #记录速度
        self.speed = speed
    def update(self,*args):
        self.rect.y += self.speed#默认垂直方向移动
class Background(GameSprite):
    def update(self):
        super().update()
        '''判断是否移出屏幕,如果移出屏幕,将图像设置到屏幕上方'''
        if self.rect.y >= screen.height:
            self.rect.y = -self.rect.height
    def _create_sprite(self):
        #创建背景精灵和精灵组
        self.bg1 = Background("./images/background.png")
        self.bg2 = Background("./images/background.png")
        self.bg2.rect.y = -self.bg2.rect.height
        self.back_group = pygame.sprite.Group(self.bg1,self.bg2)
        self.back_group.update()
        self.back_group.draw(self.screen)
#===================================================
#创建敌机
enemy1 = GameSprite("./images/enemy1.png")
enemy2 = GameSprite("./images/enemy1.png")
wei = random.randint(100,400)
enemy2.rect.x = wei#改变敌机的位置
enemy_group = pygame.sprite.Group(enemy1,enemy2)
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("退出游戏")
            pygame.quit()
            exit()
    hero_rect.y -= 1
    screen.blit(bg,(0,0))#必须得重新绘制背景和飞机位置
    screen.blit(hero,hero_rect)
    #让精灵组调用update和draw方法
    enemy_group.update()
    enemy_group.draw(screen)
    #更新屏幕显示
    pygame.display.update()
    if hero_rect.bottom <= 0:
        hero_rect.y = 800
    pygame.display.update()
