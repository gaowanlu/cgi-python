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
#-----------------功能功能添加新用户-----------------



#用户数据是一个字典
UserDataBase="UserData.kdb"
#加载用户数据库
with open(UserDataBase,"r",encoding="utf-8") as fp:
    UserSet=json.load(fp)


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
        <h1 style="color:#707070;">用户账号密码数据库</h1>
""")

print('<table border="1px" style="color:#777777;">')
print("<tr>")
print(f"<th>用户名</th>")
print(f"<th>密码</th>")
print("</tr>")
for key,val in UserSet.items():
    print("<tr>")
    print(f'<td style="color:red;">{key}</td>')
    print(f'<td style="color:blue;">******</td>')
    print("</tr>")
print('</table>')



print("""
    </body>
</html>
""")
