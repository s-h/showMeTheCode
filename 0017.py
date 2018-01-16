#!/usr/bin/env python
#coding: utf-8
#第 0017 题： 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如
#
#下所示：
#
#<?xml version="1.0" encoding="UTF-8"?>
#<root>
#<students>
#<!-- 
	#学生信息表
	#"id" : [名字, 数学, 语文, 英文]
#-->
#{
	#"1" : ["张三", 150, 120, 100],
	#"2" : ["李四", 90, 99, 95],
	#"3" : ["王五", 60, 66, 68]
#}
#</students>
#</root>
import xml.dom.minidom,json
import xlrd,json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def readXls(fileName):
    data = xlrd.open_workbook(fileName)
    table = data.sheets()[0]
    nrows = table.nrows      #表格行数
    ncols = table.ncols      #表格列数
    xlsData = {}
    for i in range(nrows):
        xlsData[i+1] = table.row_values(i)
    return xlsData



def writeXml(data):
    doc = xml.dom.minidom.Document()   #创建xml文件
    root = doc.createElement("root")
    doc.appendChild(root)

    student = doc.createElement("students")
    root.appendChild(student)

    comment = '学生信息表 "id" : [名字, 数学, 语文, 英文]'
    student.appendChild(doc.createComment(comment))
    student.appendChild(doc.createTextNode(json.dumps(data, encoding='utf-8',ensure_ascii=False)))

    fp = open('student.xml', 'w')
    doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding='utf-8')


fileName = "student.xls"
data = readXls(fileName)
writeXml(data)
