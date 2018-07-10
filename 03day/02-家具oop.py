#!/usr/bin/env python
# coding=utf-8
import time
class hourse():
    def __init__(self,address,area):
        self.address = address
        self.area = area
        self.lista = []
    def __str__(self):
        return "地址是 %s 面积是 %d"%(self.address,self.area)
    def zjiaju(self,aaa):
        if self.area < bed.size:
            print("装不下了")
        else:
            self.lista.append(aaa)
            self.area = self.area-bed.size
            print("="*50)
            print("正在装.......")
            time.sleep(2)
            print("哈哈，装好了")
            time.sleep(2)
class jiaju():
    def __init__(self,name,size):
        self.name = name
        self.size = size
    def __str__(self):
        return "床名是 %s 面积是 %d"%(self.name,self.size) 
laowang = hourse("老王家",100)
print(laowang)
bed = jiaju("席梦思",20)
print(bed)
bb = int(input("你要装几个床： "))
for i in range(bb):
    laowang.zjiaju(bed)


