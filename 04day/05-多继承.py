#!/usr/bin/env python
# coding=utf-8
class A():
    def shou(self):
        print('haha')
class B():
    def shou(self): 
        print('hehe')

class C(A,B):
    def shou(self):
        print('heihei')


c=C()
c.shou()
print(C.__mro__)


