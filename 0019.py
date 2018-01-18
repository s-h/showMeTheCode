#!/usr/bin/env python
#coding: utf-8
'''
[
	[1, 82, 65535], 
	[20, 90, 13],
	[26, 809, 1024]
]
'''
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
    xlsData = []
    for i in range(nrows):
        xlsData.append(table.row_values(i))
    return xlsData



def writeXml(data):
    doc = xml.dom.minidom.Document()   #创建xml文件
    root = doc.createElement("root")
    doc.appendChild(root)

    student = doc.createElement("students")
    root.appendChild(student)

    comment = '数字信息'
    student.appendChild(doc.createComment(comment))
    student.appendChild(doc.createTextNode(str(data)))

    fp = open('number.xml', 'w')
    doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding='utf-8')


fileName = "number.xls"
data = readXls(fileName)
writeXml(data)
