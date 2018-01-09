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
                print "添加" + str(path)
            else:
                print "略过" + str(path)


def getStatistics(path):
    lineNumber = 0   #行
    nodeNumber = 0   #注释
    blankNumber = 0  #空行
    f = open(path,'r')
    data = [line.strip() for line in f.readlines()]
    f.close()
    for line in data:
        lineNumber += 1
        if line == '':
            blankNumber += 1
        elif re.match("^#!/usr/",line):
            pass
        elif re.match("^#",line):       #多行注释没有解决
            nodeNumber += 1
    return lineNumber,nodeNumber,blankNumber
        

    
dirname = sys.argv[1]
getCodeFile(dirname)
for path in fileList:
    print path
    print getStatistics(path)

