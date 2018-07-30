#!/usr/bin/env python
# coding=utf-8
class ShowError(Exception):
    def __init__(self,name):
        self.name = name
def main():
    try:
        me = input("请输入名字： ")
        if me == "老王":
            raise ShowError("老王")
    except ShowError as result:
        print(result.name)
    else:
        print("哈哈哈哈")
main()

