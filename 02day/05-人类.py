#!/usr/bin/env python
# coding=utf-8
class people():
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight
    def play(self):
        print("玩游戏")
    def sleep(self):
        print("睡觉")
    def intraduce(self):
        print("我叫 %s 身高 %d 体重 %d"%(self.name,self.height,self.weight))
man = people("李四",80,120)
man.play()
man.sleep()
man.intraduce()
woumen = people("张三",90,180)
woumen.play()
woumen.sleep()
woumen.intraduce()
