#!/usr/bin/env python
# coding=utf-8
#top上 bottom下 left坐 right右
#x飞机的横坐标 y飞机的纵坐标 height屏幕的长 width屏幕的宽
import pygame
import random
SCREEN_RECT = pygame.Rect(0,0,480,700)#常量屏幕的大小


#爆炸销毁图片
bg1 = pygame.image.load('./images/enemy0_down1.png')
bg2 = pygame.image.load('./images/enemy0_down2.png')
bg3 = pygame.image.load('./images/enemy0_down3.png')
bg4= pygame.image.load('./images/enemy0_down4.png')

#爆炸的精灵组
enemy1_down_group = pygame.sprite.Group()

#把爆炸图片放到列表中
enemy1_down_surface = []
enemy1_down_surface.append(bg1)
enemy1_down_surface.append(bg2)
enemy1_down_surface.append(bg3)
enemy1_down_surface.append(bg4)



class GameSprite(pygame.sprite.Sprite):#父类 大写
    def __init__(self,image,speed=1):
        super().__init__()#调用父类方法
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speed = speed
    def update(self):
        self.rect.y +=self.speed
class BackGroundSprite(GameSprite):#背景精灵类
    def __init__(self,is_alt=False):
        imagename = "./images/background.png"
        super().__init__(imagename)
        if is_alt:
            self.rect.y = -self.rect.height
    def update(self):
        super().update()#调用父类方法
        #把移出屏幕的背景放到屏幕上
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height
class EnemySprite(GameSprite):#创建一个敌机精灵类
    def __init__(self):
        imagename = "./images/enemy0.png"
        super().__init__(imagename)
        self.speed = random.randint(2,5)#敌机速度
        max = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max)#敌机出现的位置(随机的)
        self.rect.bottom = 0#敌机平滑出现
        self.down_index = 0 #敌机销毁图片索引

    def update(self):
        super().update()
        if self.rect.top >= SCREEN_RECT.height:
            self.kill()#销毁敌机
class HeroSprite(GameSprite):#英雄精灵类
    def __init__(self):
        imagename = "./images/hero1.png"
        super().__init__(imagename)
        self.bullet_group = pygame.sprite.Group()#创建子弹精灵组
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
    def fire(self):
        """设置精灵位置"""
        #中间子弹
        bullet = BulletSprite()
        bullet.rect.x = self.rect.centerx-9
        bullet.rect.bottom = self.rect.top
        #左边子弹
        bullet1 = BulletSprite2()
        bullet1.rect.x = self.rect.centerx-38
        bullet1.rect.bottom = self.rect.top+40

        bullet2 = BulletSprite2()
        bullet2.rect.x = self.rect.centerx+28
        bullet2.rect.bottom = self.rect.top+40
        self.bullet_group.add(bullet1)
        self.bullet_group.add(bullet2)
        self.bullet_group.add(bullet)
    def update(self):
        self.rect.x += self.speed
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_DOWN]:
            self.speed = -4
            print("向下移动%s"%self.rect)
        elif keys_pressed[pygame.K_UP]:
            self.speed = 4
            print("向上移动%s"%self.rect)
        else:
            self.speed = 0
        self.rect.y -= self.speed
        keys_pressed2 = pygame.key.get_pressed()
        if keys_pressed2[pygame.K_LEFT]:
            self.speed = -4
            print("向左移动%s"%self.rect)
        elif keys_pressed2[pygame.K_RIGHT]:
            self.speed = 4
            print("向右移动%s"%self.rect)
        else:
            self.speed = 0
        #判断屏幕边界
        self.rect.x += self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
class BulletSprite(GameSprite):
    def __init__(self):
        imagename = "./images/bullet.png"
        super().__init__(imagename,-30)
    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()
class BulletSprite2(GameSprite):
    def __init__(self):
        imagename = "./images/bullet1.png"
        super().__init__(imagename,-30)
    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()
