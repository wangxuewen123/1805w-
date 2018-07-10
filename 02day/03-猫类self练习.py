#!/usr/bin/env python
# coding=utf-8
#一个类里面必须要有属性和它自己的方法
class cat:
    def eat(self):
        print("吃猫粮我吃的是 %s"%self.eata)
    def sleep(self):
        print("睡觉了")
    def introduce(self):
        print("我是一只 %s猫 我的颜色是 %s 身高是 %d 大小是 %d"%(self.name,self.color,self.height,self.size))
jiafei = cat()
jiafei.eata = "国产猫粮"#定义默认属性
jiafei.eat()#用对象去调用上面的方法
jiafei.sleep()
shuru = input("让猫自己定义颜色： ")
jiafei.name = "加菲猫"
jiafei.color = shuru
jiafei.height = 50
jiafei.size = 20
jiafei.introduce()
print("*"*50)
#再创建一个猫的对象
bosi = cat()
bosi.eata = "进口猫粮"
bosi.eat()
bosi.sleep()
aa = input("让猫自己定义颜色： ")
bosi.name = "波斯猫"
bosi.color = aa
bosi.height = 60
bosi.size = 30
bosi.introduce()
