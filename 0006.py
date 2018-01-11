#!/usr/bin/env python
#coding:utf-8
#第 0006 题： 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
import os,sys,re,operator
fileList = []
dirName = sys.argv[1]
def getNodeFile(dirName):
    List = os.listdir(dirName)
    os.chdir(dirName)
#    print List
    for filename in List:
        if not os.path.isdir(filename):
            fileList.append(os.path.join(os.getcwd(),filename))

def veryImportant(fileName):
    wordDict = {}
    with open(fileName) as f:
        f = f.read()
        words = re.findall('\w+',f)
    for word in words:
        if word not in wordDict:
            wordDict[word] = 1
        else:
            wordDict[word] += 1
    print fileName + " 中最重要的词："
    if not wordDict:
        print "null"
    else:
        print sorted(wordDict.items(),key=operator.itemgetter(1),reverse=False)[-1][0]


getNodeFile(dirName)
#print fileList
for fileName in fileList:
    veryImportant(fileName)

