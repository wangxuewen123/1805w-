#!/usr/bin/env python
# coding=utf-8
class people():#人类
    def __init__(self,name):#默认属性
        self.name = name
        self.hp = 100
    def __str__(self):
        return "敌人姓名 %s 血量 %s"%(self.name,self.hp)
    def zhuangzidan(self,danjia,zidan):#往弹夹中按子弹
        Danjia.lista.append(zidan)
    def zhuangdanjia(self,ak47,Danjia):#换弹夹
        ak47.Danjia = Danjia
    def naqiang(self,ak47):#老王拿起枪
        laowang.ak47 = ak47
    def kaiqiang(self,diren):#开枪
        zidan = self.ak47.Danjia.shezidan()
        zidan.kill(diren)
    def diaoxue(self,shanghai):#掉血
        self.hp = self.hp-shanghai
        print("还剩 %d"%self.hp)
        if self.hp <= 0:
            print("死了")
            return
class gun():#枪类
    def __init__(self,name):
        self.name = name
        self.Danjia = None
class danjia():#弹夹类
    def __init__(self,name,danshu):
        self.name = name
        self.danshu = danshu
        self.lista = []
    def shezidan(self):
        zidan = self.lista.pop()
        return zidan
class zidan():#子弹类
    def __init__(self,name,shanghai):
        self.name = name
        self.shanghai = shanghai
    def kill(self,diren):
        diren.diaoxue(self.shanghai)
laowang = people("老王")#创建一个老王对象
aaa = input("请选择枪1--ak47 2--m4a1")
ak47 = gun(aaa)#创建枪的对象
Danjia = danjia("快扩",30)#创建弹夹对象
laowang.naqiang(ak47)#老王拿起枪
for i in range(30):
    zd = zidan("7.62mm",10)#创建子弹对象
    laowang.zhuangzidan(Danjia,zd)
laowang.zhuangdanjia(ak47,Danjia)
laoson = people("老宋")#创建一个敌人
print(laoson)
for i in range(10):
    boom = input("开枪按q键: ")
    if boom == "q":
        laowang.kaiqiang(laoson)
