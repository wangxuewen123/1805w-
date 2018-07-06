#!/usr/bin/env python
# coding=utf-8
import random
class tools():
    def __init__(self):
        self.lista = []
    def num(self):
        a = 0
        while a <= 10:
            number = random.randint(1,100)
            if self.lista.count(number) > 1:
                continue
            else:
                self.lista.append(number)
                a+=1
        print(self.lista)
aa = tools()
aa.num()
