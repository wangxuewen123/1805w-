#!/usr/bin/env python
# coding=utf-8
class father():
    def __init__(self):
        self.name = "王"
    def chong(self):
        self.money = 200
class me(father):
    def __init__(self,name1):
        self.name1 = name1
    def chong(self,money):
        self.money = money
        print(self.money)
aaa = me("王学文")
aaa.chong(500)
