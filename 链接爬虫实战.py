#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'li'
# @Time : 2018/3/25
import re
import urllib.request


def getlink(url):
    headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36")

    opener = urllib.request.build_opener()
    opener.addheaders = [headers]

    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url)
    data = str(file.read())
    pat = '(http://[^\s) ";]+\.(\w|/)*)'
    link = re.compile(pat).findall(data)
    link = list(set(link))

    # print(data)
    # print(link)
    return link


url = "http://m.ifulidh.co/"
# getlink(url)
#
linklist = getlink(url)

for link in linklist:
    print(link[0])

    # for linkurl in link:

