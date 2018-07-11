#!/usr/bin/env python
# coding=utf-8
class people():
    def eat(self):
        print("吃")
    def shui(self):
        print("睡")
    def shuo(self):
        print("说")
class man(people):
    def gong(self):
        print("刺激")
class woman(people):
    def shou(self):
        print("真给力啊")
nan = man()
nan.eat()
nan.shui()
nan.shuo()
nan.gong()
nv = woman()
nv.eat()
nv.shui()
nv.shuo()
nv.shou()
