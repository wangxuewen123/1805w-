#!/usr/bin/env python
# coding=utf-8
import time
class tudou():
    def __init__(self):
        self.time = 0#刚开始是0分钟
        self.status = "生的"#刚开始是生的
        self.lista = []#放佐料的列表
    def cook(self):
        self.time = self.time+1
        if self.time < 3:
            self.status = "生的"
        elif self.time >= 3 and self.time < 8:
            self.status = "半生不熟"
        elif self.time >= 8 and self.time < 15:
            self.status = "熟了"
        elif self.time > 15:
            self.status = "糊了"
    def lookStatus(self):
        print(self.status)
        print("佐料有 %s"%str(self.lista))
    def addZuoLiao(self,s):
        self.lista.append(s)
digua = tudou()#创建一个地瓜对象
for i in range(15):
    digua.cook()#每运行一次显示一次烤的过程
    if i == 2:
        digua.addZuoLiao("刷辣椒将")
    elif i == 7:
        digua.addZuoLiao("架子然")
    elif i == 13:
        digua.addZuoLiao("加香菜")
    digua.lookStatus()
    time.sleep(1)
