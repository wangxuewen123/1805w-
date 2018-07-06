#!/usr/bin/env python
# coding=utf-8
f = open("test.txt","r")
content = f.read()

a = open("1.txt","w")
a.write(content)
f.close()
a.close()
