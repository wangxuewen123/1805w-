#!/usr/bin/env python
# coding=utf-8
import os
aa = input("请输入批量重命名的文件夹的名字： ")
lie = os.listdir(aa)
os.chdir(aa)#改变默认目录
for filea in lie:
    position = filea.find(".")#查找下标
    new_name = filea[:position]+"爱wo"+filea[position:]
    os.rename(filea,new_name)
