#!/usr/bin/env python
# coding=utf-8
class father(object):
    __instance = None
    def __init__(self,name):
        self.name = name
    def __new__(cls,*args,**kwargs):
        print("new")#在__init__方法执行前执行
        print("想要继续执行下面的方法必须要 告诉一下父类")
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance#只在创建第一个对象的时候执行一次
son = father("haha")
print(id(son))
print(son.name)
son1 = father("aaa")
print(id(son1))
print(son1.name)
son2 = father("dddd")
print(id(son2))
print(son2.name)
