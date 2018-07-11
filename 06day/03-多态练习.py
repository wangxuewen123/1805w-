#!/usr/bin/env python
# coding=utf-8
class Dog():
    def __init__(self,name):
        self.name = name
    def wark(self):
        print("%s在地上"%self.name)
class XiaoTianDog(Dog):
    def __init__(self,name):
        self.name = name
    def wark(self):
        print("%s飞天了"%self.name)
class Person():
    def __init__(self,name):
        self.name = name
    def game_with_play(self,dog):
        print("%s和%s一起玩"%(self.name,dog.name))
        dog.wark()
bb = Dog("旺财")
xiaoming = Person("小明")
xiaoming.game_with_play(bb)
