#!/usr/bin/python3
# -*- coding:utf-8 -*-

#-----------------程序准备-----------------
#功能获得cookie
import os
# CGI处理模块
import cgi,cgitb
#cookie处理模块
import http.cookies
#utf-8问题
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
#json
import json
from urllib.request import quote,unquote
import chardet
#-----------------程序处理-----------------

print ("""Content-Type:text""")
print()

#用户身份验证成功
if 1:
    ACCESSFILE="post_demo.json"
    with open(ACCESSFILE,"r") as fp:
        post_json=fp.read()
        print(f"{post_json}")



