#!/usr/bin/env python
#coding: utf-8
#第 0009 题： 一个HTML文件，找出里面的链接。

import urllib2
from bs4 import BeautifulSoup

def getHtml(url):
    page = urllib2.urlopen(url)
    html = page.read()
    return html

def getLink(html):
    soup = BeautifulSoup(html, 'lxml')
    allLink = soup.find_all('a')
    for a in allLink:
        print a.get('href')


html = getHtml("http://www.jianghao.tech")
getLink(html)
