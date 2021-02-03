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
#-----------------功能:上传文件-----------------

form=cgi.FieldStorage()

#获取文件名
fileitem=form['filename']
id=form.getvalue('id')
password=form.getvalue('password')

#用户数据库文件名称
UserDataBaseName="UserData.kdb"
#加载用户数据库
with open(UserDataBaseName,"r") as fp:
    UserDataBase=json.load(fp)
#是否为用户的决策
status=0
if id and (id in UserDataBase.keys()):
    if UserDataBase[id] == password:
        status=1


#非法用户则不做文件处理
if status:
    #检测文件是否上传
    if fileitem.filename:
        #设置文件路径
        fn=os.path.basename(fileitem.filename.replace("\\","/"))
        if os.path.isfile(fn):
            pass
        else:
            open('/var/www/html/temp/'+fn,'wb').write(fileitem.file.read())
        message='su"'+fn+'"su'
    else:
        message='no'


#HTML渲染

print ("""Content-Type:text/html""")
print()
print("""
        <html>
        <head>
        <meta charset="utf-8">
        <title>119.3.180.71</title>
        </head>
        <body>""")
#非法用户则账号或者密码错误
if status:
    print(f"<p>成功上传文件</p>")
else:
    print(f"<p>警告:非相关人员请远离</p>")

print("""
           </body>
           </html>
""")

