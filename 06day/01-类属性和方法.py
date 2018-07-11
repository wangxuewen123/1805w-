#!/usr/bin/env python
# coding=utf-8
class Tool():
    count = 0#类属性

    def __init__(self):
        Tool.count+=1
        self.name = "老王"#实例化对象属性

    def work(self):#实例化对象方法
        print(self.name)

    @classmethod   #声明下面的方法是类方法
    def get(cls,name):

        print("创建了%d个对象"%cls.count)#获取创建的对象个数

        print("用户名字: %s"%name)
    @staticmethod  #声明静态方法
    def print_menu():
        print("练习静态方法")
        print("与类和对象没有关系的时候用静态方法")
futou = Tool()
futou.print_menu()#对象调用静态方法
futou.get("老三")#对象调用类方法
caidao = Tool()
jiandao = Tool()
jiandao.get("老四")#对象调用类方法
chuzi = Tool()

#类方法要用类调
Tool.get("王学文")#调用类方法

Tool.print_menu()#类调用静态方法
