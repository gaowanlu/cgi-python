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
#-----------------功能:发送上传文件表单-----------------

#CGI中使用Cookie
#通过客户的浏览器，在客户的硬盘上写入记录数据
#当下次客户访问脚本时取回数据信息，从而达到身份判别的功能
#cookie常用在身份校验中
#cookie传递早于文件传递
#cookie格式 Set-cookie:name=name;expires=date;path=path;domain=domain;secure


# HTTP头部
"""
HTTP 字段名 : 字段内容
Content-type:   请求的与实体对应的MIME信息。例如: Content-type:text/html
Expires: Date   响应过期的日期和时间
Location: URL   用来重定向接收方到非请求URL的位置来完成请求或标识新的资源
Last-modified: Date 请求资源的最后修改时间
Content-length: N   请求的内容长度
Set-Cookie: String  设置Http Cookie
"""

#用户数据库文件名称

UserDataBaseName="UserData.kdb"
#加载用户数据库
with open(UserDataBaseName,"r") as fp:
    UserDataBase=json.load(fp)


#GET和POST方法
#创建 FieldStorage的实例化
form=cgi.FieldStorage()
#获取数据
site_name=form.getvalue('id')
site_url=form.getvalue('password')

status=0

if site_name and (site_name in UserDataBase.keys()):
    if UserDataBase[site_name] == site_url:
        status=1

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

if status:
    print("Content-Type:text/html")
    print(f'Set-Cookie:{site_name}="{create_cookie(site_name,site_url)}";path="/cgi-bin/";expires="Wed, 28 Aug 2022 18:30:00 GMT";')
    print() #空行，告诉服务器结束头部
    # HTML渲染
    print("""
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>IMage Share文件上传</title>
    </head>
    <style>
    </style>
    
    <body>
    """)
    


    #文件上传实例
    print("""
    <div style="width:100%;height:100%;background-color:#fafafa;display:flex;justify-content:center;align-items:center;flex-wrap:wrap;">
    <h1 style="color:rgb(79,192,141);">IMageShare</h1>
    <form enctype="multipart/form-data" action="/cgi-bin/save_file.py" method="post">
    <p>
        <span style="color:rgb(230,99,99);font-weight:bold;">选中文件:</span>
        <input type="file" name="filename" />
    </p>
    <p>
        <span style="color:orange;">账号:</span>
        <input id="id" type="text" name="id" />
    </p>
    <p>
        <span style="color:orange;">密码:</span>
        <input id="password" type="password" name="password" />
    </p>
    <p>
        <input style="
        width:80px;height:30px;background-color:rgba(180,40,40,0.8);
        border-radius:40px;color:#ffffff;border:0px;outline:none;
        " type="submit" value="上传" />
    </p>
    <form>
    </div>
    """)



    # js
    print("""
    <script>
    var id=document.getElementById("id");
    var password=document.getElementById("password");
    """)

    print(f'id.value="{site_name}";password.value="{site_url}";')
    
    print("""
    </script>     
    """)
    print("""
    <body>
    </html>
    """)
else:
    print("Content-Type:text/html")
    print('Set-Cookie:name="119.3.180.71-123";expires="Wed, 28 Aug 2022 18:30:00 GMT"; ')
    print() #空行，告诉服务器结束头部
    # HTML渲染
    print("""
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>IMage Share文件上传</title>
    </head>
    <style>
    </style>
    
    <body>
    """)
    print("""
    <div style="
        width:100%;
        height:100%;
        display:flex;
        justify-content:center;
        align-items:center;
        background-color:#fafafa;"
    >
        <span style="color:rgb(79,192,141);font-size:60px;">HELLO,PLEASE TRY ONCE</span>
    </div>
    </body>
    </html>
    """)

