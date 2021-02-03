#!/usr/bin/python3
# -*- coding:utf-8 -*-
import os
# CGI处理模块
import cgi,cgitb
#cookie处理模块
import http.cookies
#utf-8问题
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import json
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

#统计访问次数
ACCESS=0
ACCESSFILE="ACCESSFILE.json"
with open(ACCESSFILE,"r") as fp:
    ACCESS=json.load(fp)
    ACCESS+=1
with open(ACCESSFILE,"w") as fp:
    json.dump(ACCESS,fp)




# HTML渲染
print("""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"> <link rel="icon" 
    <link rel="icon" href="http://119.3.180.71/temp/20210123080543653_easyicon_net_128.ico" type="image/x-icon" />
    <link rel="shortcut icon" href="http://119.3.180.71/temp/20210123080543653_easyicon_net_128.ico"  type="image/x-icon"/> 
    <meta name="viewport" content="width=598,user-scalable=no">
    <title>GUET课程表</title>
    <style>
    .show-width{width:66.6%;}
    .downloadText-fontsize{font-size: 2.8em;}
    .show-appapge-div-dispaly{display: flex;}
    .show-appapge-phone-dispaly{display: none;}
    @media screen and (max-width:600px){
        .downloadText-fontsize{font-size: 2.3em;}
        .show-width{width:100%;}
        .show-appapge-div-dispaly{display: none;}
        .show-appapge-phone-dispaly{display: block;}
    }
    @media screen and (min-width:601px) and (max-width:1025px){
        .show-width{width:90%;}
    }
    @media screen and (min-width:1026px){
        .show-width{width:66.6%;}
    } 
    </style>
    <style>
        *{
            margin:0px;
            padding: 0px;
        }
        a{
            text-decoration:none;
            color:#707070;
        }
        body{
            font-variant-ligatures: no-common-ligatures;
            -webkit-font-smoothing: antialiased;
        }
        .header{
            width:100%;
            height:4em;
            display: flex;
            justify-content: center;
        }
        .header-content{
            width:66.6%;
            height:4em;
        }
        .downloadText{
            font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Microsoft YaHei", Tahoma, Arial;
            font-weight: bold;
            width:100%;
            display: flex;
            justify-content: center;
        }
        .hover-hand:hover{
            cursor:pointer;
        }
        .div-shadow{ 
            -webkit-box-shadow: rgb(185, 185, 185) 0px 0px 10px; 
            -moz-box-shadow: rgb(192, 192, 192) 0px 0px 10px; 
            box-shadow: rgb(199, 199, 199) 0px 0px 10px; 
        } 
    </style>
</head>
<body style="display: flex;justify-content: center;flex-wrap: wrap;background-color: rgb(250,251,255);">
    <div class="header" style="background-color: #ffffff;position: fixed;">
        <div class="header-content">
            <img src="http://119.3.180.71/table-view/img/u=3462933886,3601786463&fm=26&gp=0.jpg" style="height:100%;">
        </div>
    </div>
    <div style="width:100%;height:4em;"></div>
    <div class="show-width">
        <!-- 下载文字显示 -->
        <div style="width:100%;margin-bottom: 5em;">
            <div style="width:100%;display: flex;justify-content: center;padding-top: 6em;flex-wrap: wrap;">
                <div class="downloadText downloadText-fontsize">下载GUET课程表</div>
                <div style="width:100%;display: flex;justify-content: center;margin-top: 1.5em;color:#51565D;font-size: 1.1em;">暂时仅支持Android版本</div>
            </div>
        </div>
        <!-- 下载盒 -->
        <div style="width:100%;display: flex;flex-wrap: wrap;justify-content: center;">
            <!-- 点击下载 -->
            <div style="display: flex;flex-wrap: wrap;width:200px;justify-content: center;">
                <div class="hover-hand div-shadow"id="download" style="width:148px;height:148px;background-color: #ffffff;display: flex;justify-content: center;align-items: center;border-radius: 8px;">
                    <img style="width:30%;height:30%;" src="http://119.3.180.71/table-view/img/下载.png">
                </div>
                <div style="width:148px;height:32px;text-align: center;margin-top: 5px;" >
                    点击下载
                </div>
            </div>
            <!-- 扫码下载 -->
            <div style="display: flex;flex-wrap: wrap;width:200px;justify-content: center;">
                <div class="div-shadow" style="width:148px;height:148px;background-color: #ffffff;display: flex;justify-content: center;align-items: center;border-radius: 8px;">
                    <img style="width:70%;height:70%;" src="http://119.3.180.71/table-view/img/1610200080.png">
                </div>
                <div style="width:148px;height:32px;text-align:center;margin-top: 5px;">
                    手机扫码下载
                </div>
            </div>
        </div>
        <!-- 应用页面展示 -->
        <div class="show-appapge-div-dispaly" style="width:100%;justify-content: center;margin-top: 20px;">
            <img style="max-width:100%;width:2000px;" src="http://119.3.180.71/table-view/img/应用图.png">
        </div>
        <div class="show-appapge-phone-dispaly" style="width:100%;margin-top: 20px;">
            <img style="width:100%;" src="http://119.3.180.71/table-view/img/手机.png">
            <img style="width:100%;" src="http://119.3.180.71/table-view/img/1611392006066.png">
        </div>


        <!-- 尾部 -->
        <!-- 网页尾部 -->
        <div class="footer" style="color:#586069;display: flex;flex-wrap: wrap;width:100%;">
            <div style="width: 20%;margin-left: 4%;height: 10em;display: flex;align-items: center;justify-content: center;text-align: center;">
            GUET课程表.
            </div>
            <div style="width: 75%;display: flex;justify-content: space-around;align-items: center;flex-wrap: wrap;">
            <div style="width:6em;height:1em;display: flex;justify-content: center;align-items: center;">
                <a href="https://qm.qq.com/cgi-bin/qm/qr?k=ENIPuzR09ysdvBRhzHIcESMtMfgCEjnw&jump_from=webapi" style="font-size: 0.8em;">联系我们</a>
            </div>
            <div style="width:6em;height:1em;display: flex;justify-content: center;align-items: center;">
                <a href="http://www.guet1024.cn" style="font-size: 0.8em;">应用社区</a>
            </div>
            <div style="width:6em;height:1em;display: flex;justify-content: center;align-items: center;">
                <a href="https://github.com/guet1024" style="font-size: 0.8em;">Git仓库</a>
            </div>
""")
print('<div style="width:6em;height:1em;display: flex;justify-content: center;align-items: center;">')
print(f'<a href="#" style="font-size:0.8em;">{ACCESS} 访问</a>')
print("</div>")
print("""
            </div>
        </div>
    </div>
</body>
<script>
    document.getElementById("download").onclick=function(){
        window.location.href="https://wwa.lanzous.com/b00u3y7za";
    }
</script>
</html>


""")
