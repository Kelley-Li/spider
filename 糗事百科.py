#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'li'
# @Time : 2018/3/26
import re
import urllib.request


def getcontent(url,page):
    headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36")

    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(url).read().decode("utf-8")
    userpat='target="_blank" title="(.*?)">'
    contentpat='<div class="content">(.*?)</div>'
    userlist=re.compile(userpat,re.S).findall(data)
    contentlist=re.compile(contentpat,re.S).findall(data)

    x=1
    for content in contentlist:
        cotent=content.replace("\n"," ")
        name="content"+str(x)
        exec(name+'=content')
        x+=1

    y=1
    for user in userlist:
        name="content"+str(y)
        print("用户"+str(page)+str(y)+"是:"+user)
        print("内容是:")
        exec("print("+name+")")
        print("\n")
        y+=1

for i in range(1,30):
    url="http:// www.qiushibaike.com/8hr/page/"+str(i)
getcontent(url,i)
