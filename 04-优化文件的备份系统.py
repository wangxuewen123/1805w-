#!/usr/bin/env python
# coding=utf-8
name = input("请输入你要备份的文件名字： ")
f = open(name,"r")
#查找索引
qie = name.find(".")
#切片索引
while True:
    content = f.read(1024)
    if len(content) == 0 or content == "":#如果每次读取的内容等于0或者没有了，就跳出循环
        break
new_name = name[:qie]+"back"+name[qie:]
s = open(new_name,"w")
s.write(content)
f.close()
s.close()

