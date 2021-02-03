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

#-----------------程序处理-----------------
print("Content-Type:text/html")
print()

print ("""
<html>
<head>
<meta charset="utf-8">
<title>viewCookie</title>
</head>
<body>
<h1 style="color:blue;">读取cookie信息</h1>
""")

if 'HTTP_COOKIE' in os.environ:
    cookie_string=os.environ.get('HTTP_COOKIE')
    c= http.cookies.SimpleCookie()
    c.load(cookie_string)
    try:
        print ("name:\t"+c['name'].value+"<br>")
    except KeyError:
        print ("cookie 没有设置或者已过去<br>")

print ("""
</body>
</html>
""")