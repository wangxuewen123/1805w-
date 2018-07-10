#!/usr/bin/env python
# coding=utf-8
#保护对象私有属性
class home():
    def __init__(self):
        self.__mima = 123456
    def getmima(self):
        return self.__mima
    def setmima(self,mim1a):
        self.__mima = mim1a
wangge = home()
#print(wangge.__mima)
wangge.setmima(5201314)
print(wangge.getmima())
#保护对象私有方法
class home2():
    def __mima(self):
        print("3333")
    def getmima(self):
        self.__mima()
o = home2()
o.getmima()
