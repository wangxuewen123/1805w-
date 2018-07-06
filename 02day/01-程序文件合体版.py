#!/usr/bin/env python
# coding=utf-8
import os
fuction = input("请选择功能1--备份文件\t2--批量重命名\t3--写\t4--读： ")
if fuction == "1":
    cp = input("请输入要备份的文件名： ")
    f = open(cp,"r")
    content = f.read(1024)
    position = cp.find(".")
    new_name = cp[:position]+"back"+cp[position:]
    pause = open(new_name,"w")
    pause.write(content)
    f.close()
    pause.close()
elif fuction == "2":
    renname = input("请输入要文件的目录名： ")
    dira = os.listdir(renname)
    os.chdir(renname)
    for old_file in dira:
        position2 = old_file.find(".")
        new = input("请输入新的名字： ")
        new_name2 = old_file[:position2]+new+old_file[position2:]
        os.rename(old_file,new_name2)
        print("批量重命名完成")
elif fuction == "3":
    wri = input("请输入文件名： ")
    f = open(wri,"w")
    write = input("请输入你要写的内容： ")
    f.write(write)
    print("写入完成")
elif fuction == "4":
    red = input("请输入文件名： ")
    f1 = open(red,"r")
    content1 = f1.read(1024)
    print("读取完成")
    print(content1)
