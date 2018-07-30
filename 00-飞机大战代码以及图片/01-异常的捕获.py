#!/usr/bin/env python
# coding=utf-8
try:
    a = 23
    print(23,a)
except (NameError,FileNotFoundError):
    print("捕获知道的错误类型")
except Exception as ret:#捕获所有异常
    print(ret)
    print("捕获不知道的错误类型")
else:
    print("没有错误会执行")
finally:
    print("不管有没有错误都执行")
class cuowu():
    def pan(self):
        a = input("请输入一个数字： ")

