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
text=form.getvalue('post_textarea')
#共有sum张图片
#相应内容类型
print ("""Content-Type:text/html""")
print()

#post文件
post_json={"textarea":text,"username":"123","imgindex":[]}

#保存图片文件(sum张图片)

for i in range(9):
    name="img"+str(i)
    print(i)
    if form[name].filename:
        print("yes")
    else:
        continue
    fileitem=form[name]
    with open("/var/www/html/DataBase/"+"123"+"/"+"img/img_json.kdb","r") as fp:
        img_set=json.load(fp)
    counter=str(img_set["counter"]+1)
    img_set["counter"]=img_set["counter"]+1
    with open("/var/www/html/DataBase/"+"123"+"/"+"img/img_json.kdb","w") as fp:
        json.dump(img_set,fp)
    #设置文件路径
    fn=os.path.basename(fileitem.filename.replace("\\","/"))
    dot_set=-1
    for index in range(len(fn)):
        if fn[index]=='.':
            dot_set=index
    file_type=""
    file_type+=fn[dot_set+1:]
    print(file_type)
    open('/var/www/html/DataBase/'+"123"+"/img/"+str(counter)+"."+file_type,'wb').write(fileitem.file.read())
    post_json["imgindex"].append(str(counter)+"."+file_type)


#读取post_json

with open("/var/www/html/DataBase/"+"123"+"/"+"post/post_json.kdb","r") as fp:
    post_set=json.load(fp)
counter=str(post_set["counter"])
post_set["counter"]+=1
with open("/var/www/html/DataBase/"+"123"+"/"+"post/post_json.kdb","w") as fp:
    json.dump(post_set,fp)

#存储json
with open("/var/www/html/DataBase/"+"123"+"/"+"post/"+counter+".post","w") as fp:
    json.dump(post_json,fp)


print(text)





