#!/usr/bin/env python
# coding=utf-8
import time
class student():
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
    def aaa(self):
        print("我是 %s\t今年%s岁了"%(self.name,self.sex))
class Manager():#管理学生 增删改查
    def __init__(self):
        self.list = []#装学生
    def add(self,student):#添加学生
        self.list.append(student)
        print("添加信息成功".center(50,"="))
    def cha(self,zhao):#查找学生
        for i in self.list:
            if zhao == i["name"]:
                print("姓名 %s\n年龄 %s\n学号 %s"%(i["name"],i["age"],i["num"]))
            else:
                print("没有这个学生")
    def gai(self,gaim):#修改学生信息
        for i in self.list:
            if gaim == i["name"]:
                gai1 = int(input("请选择你要改得信息1--姓名 2--年龄 3--学号\n>>>>>>>>>>>>>>>  "))
                if gai1 == 1:
                    gaim1 = input("请输入新的名字\n>>>>>>>>>>>>>>>>  ")
                    i["name"] = gaim1
                elif gai1 == 2:
                    gainian = input("请输入新的年龄\n>>>>>>>>>>>>>>>>>  ")
                    i["age"] = gainian
                elif gai1 == 3:
                    gaihao = input("请输入新的学号\n>>>>>>>>>>>>>>>>>  ")
                    i["num"] = gaihao
                    print("修改成功".center(50,"="))
            else:
                print("没有这个学生")
    def shan(self,shande):#删除学生信息
        for i in self.list:
            if shande == i["name"]:
                i.pop("name")
                i.pop("age")
                i.pop("num")
                print("删除成功")
            else:
                print("没有这个学生")
class Menu():
    def __init__(self):
        self.manager = Manager()#让菜单持有管理类对象的引用
    def print_Menu(self):
        while True:
            xuan = int(input("请输入选项1--添加 2--查看 3--修改 4--删除 5--退出\n>>>>>>>>>>>>>>  "))
            print("★ "*25)
            if xuan == 1:
                name = input("请输入姓名： ")
                age = input("请输入年龄： ")
                num = input("请输入学号： ")
                dic = {"name":name,
                       "age":age,
                       "num":num}
                self.manager.add(dic)
            elif xuan == 2:
                ca = input("请输入你要查的姓名： ")
                self.manager.cha(ca)
            elif xuan == 3:
                gaiming = input("请输入你要修改的学生姓名： ")
                self.manager.gai(gaiming)
            elif xuan == 4:
                pop = input("请输入你要删除的学生姓名\n>>>>>>>>>>>>>>>>>  ")
                self.manager.shan(pop)
            elif xuan == 5:
                break
me = input("为这个系统起一个名字吧>>>>>>>>>>>>>  ")
time.sleep(3)
print("正在设置中.......")
time.sleep(3)
print("正在设置中.......")
time.sleep(3)
print("马上就要好了.......")
time.sleep(3)
print("哦了,体验愉快.......")
Jiqi_XiaoBin = student(me,2)
Jiqi_XiaoBin.aaa()
m = Menu()#建立一个菜单的对象
m.print_Menu()
