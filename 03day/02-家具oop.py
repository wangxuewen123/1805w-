#!/usr/bin/env python
# coding=utf-8
class hourse():
    def __init__(self,address,area):
        self.address = address
        self.area = area
        self.lista = []
    def __str__(self):
        return "地址是 %s 面积是 %d"%(self.address,self.area)
    def zjiaju(self,aaa):
        if self.area < self.size:
            print("装不下了")
        else:
            self.lista.append(aaa)
            self.area = self.area-self.size
class jiaju():
    def __init__(self,name,size):
        self.name = name
        self.size = size
    def __str__(self):
        return "品牌是 %s 大小是 %d"%(self.name,self.size)
laowang = hourse("老王家",100)
print(laowang)
bed = jiaju("席梦思",5)
print(bed)
for i in range(400):
    laowang.zjiaju(bed)


