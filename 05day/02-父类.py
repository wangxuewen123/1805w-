#!/usr/bin/env python
# coding=utf-8
class A(object):
    def __init__(self):
        self.__name = "ww"
    def getname(self):
        return self.__name
class b(A):
    pass
aa = A()
print(aa.getname())
cc = b()
print(cc.getname())
