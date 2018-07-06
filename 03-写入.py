#!/usr/bin/env python
# coding=utf-8
import os
f = open("test.txt","w")
f.write("python java c++ c+ c web html html5\n")
f.close()
os.remove("testback.txt")

