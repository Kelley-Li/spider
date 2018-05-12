#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'li'
# @Time : 2018/3/24
import  re
import urllib.request

def craw(url,page):
    html1=urllib.request.urlopen(url).read()
    html1=str(html1)
    pat1='<div id="plist".+?<div class="page clearfix">'
    result1=re.compile(pat1).findall(html1)

    result1=result1[0]
    pat2='<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg)">'
    imglist=re.compile(pat2).findall(result1)

    x=1

    for imgeurl in imglist:
        imgename="F:/Python/爬虫/img/"+str(page)+str(x)+".jpg"

        imgeurl="http://"+imgeurl

        try:
            urllib.request.urlretrieve(imgeurl,filename=imgename)

        except urllib.error.URLError as e:

            if hasattr(e,"code"):
                x+=1
            if hasattr(e,"reason"):
                x+=1
        x+=1

for i in range(0,100):
    url = 'https://list.jd.com/list.html?cat=9987,653,655&page='+str(i)
    craw(url,i)
