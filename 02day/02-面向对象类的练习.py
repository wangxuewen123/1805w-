#!/usr/bin/env python
# coding=utf-8
class car:
    def fly(self):
        print("车飞了")
    def run(self):
        print("车跑了")
    def dao(self):
        print("倒车中")
#创建一个对象,类是创建对象的模板
msld = car()
print("劳斯莱斯")
msld.run()
print("="*50)
#继续创建对象,类是创建对象的模板
BWM = car()
print("宝马")
BWM.fly()
class people:
    def eat(self):
        print("吃东西")
    def cal(self):
        print("在上课")
    def run(self):
        print("跑步")
man = people()
man.eat()
man.cal()
man.run()
