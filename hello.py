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
print("Content-Type:text/html")
#print('Set-Cookie: name="菜鸟教程";expires=Wed, 28 Aug 2016 18:30:00 GMT')
print() #空行，告诉服务器结束头部

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


if status:
    # HTML渲染
    print("""
    <html>
    <head>
        <meta charset="utf-8">
            <title>Python CGI</title>
        <head>
    <style>
    </style>
    
    <body>
        <h1 style="color:red;">Code To Long</h1>
    """)
    print(f"<h2>上传文件</h2>")


    """
    print("读取cookie信息")
    if 'HTTP_COOKIE' in os.environ:
        cookie_string=os.environ.get('HTTP_COOKIE')
        c=http.cookies.SimpleCookie()
        c.load(cookie_string)
        try:
            data=c['name'].value
            print("cookie data: "+data+"<br>")
        except KeyError:
            print("cookie 没有设置或者已过去<br>")
    """

    #文件上传实例
    print("""
    <form enctype="multipart/form-data" action="/cgi-bin/save_file.py" method="post">
    <p>选中文件:<input type="file" name="filename" /></p>
    <p>账号:<input id="id" type="text" name="id" /></p>
    <p>密码:<input id="password" type="password" name="password" /></p>
    <p><input type="submit" value="上传" /></p>
    <form>
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
    print("警告:非相关人员请远离")

