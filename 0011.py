#!/usr/bin/env python
#coding: utf-8
#第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
import re,sys

contrabandWords = [
        "北京",
        "程序员",
        "公务员",
        "领导",
        "牛比",
        "牛逼",
        "你娘",
        "你妈",
        "love",
        "sex",
        "jiangge"
        ]

userInput = raw_input("测试内容:")
for word in contrabandWords:
    if re.search(word,userInput):
        print "Freedom"
        sys.exit(0)
print "Human Rights."
