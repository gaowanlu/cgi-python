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
#-----------------功能:上传文件-----------------

form=cgi.FieldStorage()

#获取文件名
id=form.getvalue('id')
password=form.getvalue('password')
post_json=form.getvalue('Open_post_json')

#用户数据库文件名称
UserDataBaseName="UserData.kdb"
#加载用户数据库
with open(UserDataBaseName,"r") as fp:
    UserDataBase=json.load(fp)

#是否为用户的决策
def create_cookie(id,password):
    password_length=len(password)
    cookie=""
    for ch in password:
        if (ord(ch)-22>0):
            cookie+=chr(ord(ch)-7)
    for ch in id:
        if (ord(ch)-22>0):
            cookie+=chr(ord(ch)-2)
    return cookie

status=0
if id and (id in UserDataBase.keys()):
    if UserDataBase[id] == password:
        if 'HTTP_COOKIE' in os.environ:
            cookie_string=os.environ.get('HTTP_COOKIE')
            c= http.cookies.SimpleCookie()
            c.load(cookie_string)
            try:
                if c[id].value == create_cookie(id,password):
                    status=1
                else:
                    pass
            except KeyError:
                pass

print ("""Content-Type:text""")
print()

#用户身份验证成功
if status:
    ACCESSFILE="post_demo.json"
    json_obj=json.loads(post_json)
    with open(ACCESSFILE,"w") as fp:
        json.dump(json_obj,fp)

if status:
    print(f"{post_json}")

