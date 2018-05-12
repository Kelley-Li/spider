#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'li'
import requests
from bs4 import BeautifulSoup
url='http://www.pm25x.com/'
html=requests.get(url)
sq=BeautifulSoup(html.text,'html.parser')

city=sq.find('a',{'title':'北京PM2.5'})
citylink=city.get("href")
url1=url+citylink
html1=requests.get(url1)
sq1=BeautifulSoup(html1.text,'html.parser')
data=sq1.select(".aqivalue")
PM=data[0].text
print(PM)