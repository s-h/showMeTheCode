#!/usr/bin/env python
#coding:utf-8
#第 0004 题： 任一个英文的纯文本文件，统计其中的单词出现的个数。
import sys,re

wordNumber = 0
fileName = sys.argv[1]
with open(fileName) as f:
    f = f.read()
    word = re.findall('\w+',f)
wordNumber += len(word)
print wordNumber
