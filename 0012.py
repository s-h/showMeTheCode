#!/usr/bin/env python
#coding: utf-8
#第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
import re,sys

with open("filtered_words.txt") as f:
    contrabandWords = [line.strip() for line in f.readlines()]

userInput = raw_input("测试内容:")
for word in contrabandWords:
    strip = re.compile(word)
    userInput =  strip.sub("*" * len(word), userInput)

print userInput
