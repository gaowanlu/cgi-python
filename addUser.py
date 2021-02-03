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

#-----------------程序处理-----------------
#-----------------功能:更改用户信息-----------------

#用户数据是一个字典
UserDataBase="UserData.kdb"
#加载用户数据库
with open(UserDataBase,"r") as fp:
    UserSet=json.load(fp)

#操纵数据库
#手动删除用户
if 0:
  del UserSet['null']

#创建 FieldStorage的实例化
form=cgi.FieldStorage()
#获取数据
User_id=form.getvalue('id')
User_password=form.getvalue('password')
UserSet[User_id]=User_password

#重新写入数据库
with open(UserDataBase,"w") as fp:
    json.dump(UserSet,fp)

#发送HTML
print("Content-Type:text/html")
print ()
print ("""
<html>
  <head>
    <meta charset="utf-8">
    <title>用户数据库</title>
  </head>
    <body>
        <h1 style="color:#707070;">成功写入数据库</h1>
""")
print(f"<p>{User_id} : {User_password}</p>")
print("""
    </body>
</html>
""")