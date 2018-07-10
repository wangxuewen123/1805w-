#!/usr/bin/env python
# coding=utf-8
class student():
    def __init__(self,name,age,phone):
        self.name = name
        self.age = age
        self.phone = phone
        self.lista = []
    def luru(self):
        f = open("1student.txt","w")
        f.write(self.name)
        f.write(self.age)
        f.write(self.phone)
        f.close()
    def ruxue(self):
        print("入学".center(50,"="))
        dic = {"name":self.name,
               "age":self.age,
               "phone":self.phone}
        self.lista.append(dic)
        for i in self.lista:
            print("入学成功\n姓名 %s\n年龄 %s\n电话 %s\n"%(i["name"],i["age"],i["phone"]))
    def chakan(self):
        print("查看当前学生资料".center(50,"="))
        print(self.lista)
        a = 0
        while a == 0:
            if len(self.lista) >= 1:
                for i in self.lista:
                    print("下面是所有学生资料")
                    print("姓名 %s\n年龄 %s\n联系方式 %s\n"%(i["name"],i["age"],i["phone"]))
                a = 1
            else:
                print("当前没有学生")
                a = 1
    def shan(self):
        pass
while True:
    xuan = input("请输入选项1--添加 2--查看 3--修改 4--删除 5--退出\n")
    if xuan == "1":
        name = input("姓名： ")
        age = input("年龄： ")
        phone = input("电话： ")
        wang = student(name,age,phone)
        wang.luru()
        wang.ruxue()
    elif xuan == "2":
        wang.chakan()
    elif xuan == "5":
        break

