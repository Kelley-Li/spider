#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'li'
import os,requests,re
from bs4 import BeautifulSoup
from urllib.request import urlopen
url='http://www.tooopen.com/img/87.aspx'
html=requests.get(url) #获取网页源码
html.encoding='utf-8'        #设置源码内容的编码方式
sp = BeautifulSoup(html.text, "html.parser")        #解析源码到sp对象

#创建images目录保存图片
images_dir="images/"            #设置目录文件夹
if not os.path.exists(images_dir):      #判断目录文件夹是否已存在
    os.mkdir(images_dir)            #如果不存在贼创建文件夹

all_links=sp.find_all(['a','img'])        #获取所有的<a>标签和<img>标签
for link in all_links:
    #抓取src和href属性内容
    src=link.get('src')         #把src属性值存入src对象
    href=link.get('href')           #把href属性值存入href对象
    attrs=[src,href]                #把src和href存入一个列表
    for attr in attrs:
        #如果sttr不为空或其中包含 .jpg 或 .png 关键字
        if attr!=None and ('.jpg' in attr or '.png' in attr):
            #则取出这个连接至full_path变量
            full_path=attr
            filename=full_path.split('/')[-1]       #取得图片全名
            ext = filename.split('.')[-1]  # 取得扩展名
            filename = filename.split('.')[-2]  # 取得主文件名
            if 'jpg' in ext:filename=filename+'.jpg'
            else:filename=filename+'.png'
            print(attr)
            #保存图片
            try:
                image=urlopen(full_path)
                f=open(os.path.join(images_dir,filename),'wb')
                f.write(image.read())
                f.close()
            except:
                print("{} 无法读取！" .format(filename))