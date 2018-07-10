#!/usr/bin/env python
# coding=utf-8
class Dog():
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return "我的名字是 %s"%self.name
    def __del__(self):
        print("我要死了")
    def work(self):
        print("往往叫")
tom = Dog("阿华")
tom1 = tom
tom2 = tom
del tom
print("dasasdsad")
