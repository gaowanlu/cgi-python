#!/usr/bin/python3
# -*- coding:utf-8 -*-

#-----------------程序准备-----------------
#功能获得cookie
import os,sys,stat
# CGI处理模块
import cgi,cgitb
#cookie处理模块
import http.cookies
#utf-8问题
import codecs
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
  id="wq7e"
  del UserSet[id]#删除账号与密码
  os.system("rm -rf ./DataBase/"+id)#删除用户数据

#创建 FieldStorage的实例化
form=cgi.FieldStorage()
#获取数据
User_id=form.getvalue('id').strip()
User_password=form.getvalue('password').strip()

#增加新用户
if User_id and User_password and(User_id not in UserSet.keys()):
  UserSet[User_id]=User_password
  os.mkdir("../html/DataBase/"+User_id,stat.S_IRWXU)
  #os.system("sudo chmod 777 /var/www/cgi-bin/DataBase/*")
  os.mkdir("../html/DataBase/"+User_id+"/"+"img",stat.S_IRWXU)
  #重新写入数据库
  with open("../html/DataBase/"+User_id+"/"+"img/img_json.kdb","w") as fp:
    json.dump({"counter":0},fp)
  os.mkdir("../html/DataBase/"+User_id+"/"+"post",stat.S_IRWXU)
  os.mkdir("../html/DataBase/"+User_id+"/"+"profile",stat.S_IRWXU)

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
print(f"<p>{User_id}:{UserSet[User_id]}</p>")
print("""
    </body>
</html>
""")