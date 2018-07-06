#!/usr/bin/env python
# coding=utf-8
import os
class my_file():
    def main(self):
        print("1.写")
        print("2.读")
        print("3.拷贝")
        print("4.批量重命名")
        print("5.退出")
    def Write(self):
        file = input("请输入文件名必须加后缀： ")
        f = open(file,"w")
        ww = input('请输入内容： ')
        f.write(ww)
        f.close()
    def Read(self):
        file1 = input("请输入文件名必须加后缀： ")
        a = open(file1,"r")
        while True:
            if len(a.read(1024)) == 0:
                break
            else:
                content = a.read(1024)
                print(content)
    def renname(self):
        cp = input("请输入备份的文件名： ")
        f = open(cp,"r")
        while True:
            content = f.read(1024)
            if content == "":
                break
            else:
                position = cp.find(".")
                name = input("请输入新的文件名： ")
                new_name = cp[:position]+name+cp[position:]
                f1 = open(new_name,"w")
                f1.write(content)
                f.close()
                f1.close()
    def pil(self):
        rename1 = input("请输入要批量命名的目录： ")
        ll = os.listdir(rename1)
        os.chdir(rename1)
        for old_name in ll:
            position1 = old_name.find(".")
            new = input('请输入新的文件名： ')
            new_name = old_name[:position1]+new+old_name[position1:]
            os.rename(old_name,new_name)
            print("批量重命名完成")
mefile = my_file()
#mefile.main()
#mefile.Write()
#mefile.Read()
#mefile.renname()
#mefile.pil()
while True:
    mefile.main()
    xuan = int(input("请输入选项： "))
    if xuan == 1:
        mefile.Write()
    elif xuan == 2:
        mefile.Read()
    elif xuan == 3:
        mefile.renname()
    elif xuan == 4:
        mefile.pil()
    elif xuan == 5:
        break
