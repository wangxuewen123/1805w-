#!/usr/bin/env python
# coding=utf-8
import pygame
from GameSprite import *
CREATE_ENEMY_EVENT = pygame.USEREVENT#敌机的定时器时间常量
HERO_FIRE_EVENT = pygame.USEREVENT+1#定义发射子弹常量
class PlanMain():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)#敌机的速度/毫秒
        self.enemy_group = pygame.sprite.Group()#敌机精灵组

        #敌机销毁精灵组
        self.enemy1_down_group = pygame.sprite.Group()


        self.hero = HeroSprite()#英雄战机
        """英雄精灵组"""
        self.hero_group = pygame.sprite.Group(self.hero)
        pygame.time.set_timer(HERO_FIRE_EVENT,100)#子弹速度
        self.count = 0
        self.score = 0 #分数
    def start_game(self):
        """开始游戏"""
        print("开始游戏...")
        while True:
            # 1. 设置刷新帧率
            self.clock.tick(60)
            # 2. 事件监听
            self.__event_handler()
            # 3. 碰撞检测
            self.__check_collide()
            # 4. 更新精灵组
            self.__update_sprites()
            # 5. 更新屏幕显示
            pygame.display.update()
    def __event_handler(self):
        """事件监听"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                planmain.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = EnemySprite()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
    def __check_collide(self):
        """碰撞检测"""
        #检测两个精灵组中的精灵是否碰撞在一起 子弹和敌机
        enemy_down = pygame.sprite.groupcollide(self.enemy_group,self.hero.bullet_group,  True, True)
        self.enemy1_down_group.add(enemy_down)#加入到销毁组
        #检测一个精灵和一个精灵组 敌机和英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            self.hero.kill()
            PlanMain.__game_over()
    def __update_sprites(self):
        """更新精灵组"""
        self.back_ground.update()
        self.back_ground.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        #绘制分数
        self.drawText(str(self.score),SCREEN_RECT.width - 30,50)


        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)
        #敌机销毁精灵组
        for enemy1_down in self.enemy1_down_group:
            self.screen.blit(enemy1_down_surface[enemy1_down.down_index],enemy1_down.rect)
            if self.count % 15 == 0:
                enemy1_down.down_index += 1
                if enemy1_down.down_index == 3:
                    self.score +=5
                    self.enemy1_down_group.remove(enemy1_down)
                    print(self.score)
    def __create_sprites(self):
        '''背景创建精灵组'''
        bg1 = BackGroundSprite()
        bg2 = BackGroundSprite(True)
        bg2.rect.y = -bg2.rect.height
        self.back_ground = pygame.sprite.Group(bg1,bg2)
    @staticmethod
    def __game_over():
       """游戏结束"""
       print("游戏结束")
       pygame.quit()
       exit()

    def drawText(self,text,posx,posy,textHeight=48,fontColor=(0,0,0),backgroudColor=(255,255,255)):
        fontObj = pygame.font.Font(None, textHeight)  # 通过字体文件获得字体对象
        textSurfaceObj = fontObj.render(text, True,fontColor,backgroudColor)  # 配置要显示的文字
        textRectObj = textSurfaceObj.get_rect()  # 获得要显示的对象的rect
        textRectObj.center = (posx, posy)  # 设置显示对象的坐标
        self.screen.blit(textSurfaceObj, textRectObj)  # 绘制字	
planmain = PlanMain()
planmain.start_game()
