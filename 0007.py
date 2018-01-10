#!/usr/bin/env python
#coding:utf-8
#第 0007 题： 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
import os,sys,re

fileType=[
        ".py",
        ".sh",
        ".md"
        ]

fileList = []

def getCodeFile(dirName):
    for root,dirs,files in os.walk(dirName):
        for f in files:
            path = os.path.join(root,f) #获取绝对路径文件名
            if os.path.splitext(path)[1] in fileType:
                fileList.append(path)

def getStatistics(path):
    lineNumber = 0   #行
    singleLineNumber = 0   #注释
    blankNumber = 0  #空行
    mutilineNumber = 1
    mutiline = False #多行注释
    f = open(path,'r')
    data = [line.strip() for line in f.readlines()]
    f.close()
    for line in data:
        lineNumber += 1
        if line == '':
            blankNumber += 1
        if re.match("^'''$",line):      #多行注释
            mutiline = not(mutiline)
        if mutiline == True:
            mutilineNumber += 1
        elif re.match("^#!/usr/",line):
            pass
        elif re.match("^#",line):       #单行注释
            singleLineNumber += 1
    if mutilineNumber > 1:
        commentsNumber = singleLineNumber + mutilineNumber 
    else:
        commentsNumber = singleLineNumber
    return lineNumber,commentsNumber,blankNumber
        

    
dirname = sys.argv[1]
getCodeFile(dirname)
for path in fileList:
    print path
    print getStatistics(path)

