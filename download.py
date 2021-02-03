#!/usr/bin/python3
# -*- coding:utf-8 -*-
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
# HTTP 头部
print ("Content-Disposition: attachment; filename=\"data.txt\"")
print ()
# 打开文件
fo = open("./tmp/aa.txt", "rb")
str = fo.read()
print (str)
# 关闭文件
fo.close()
