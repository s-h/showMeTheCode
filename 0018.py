#!/usr/bin/env python
#coding: utf-8
'''
第 0018 题： 将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中，如下 所示：
    <?xmlversion="1.0" encoding="UTF-8"?>
    <root>
    <cities>
    <!-- 
    	城市信息
    -->
    {
    	"1" : "上海",
    	"2" : "北京",
    	"3" : "成都"
    }
    </cities>
    </root>
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

    comment = '城市信息'
    student.appendChild(doc.createComment(comment))
    student.appendChild(doc.createTextNode(json.dumps(data, encoding='utf-8',ensure_ascii=False)))

    fp = open('city.xml', 'w')
    doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding='utf-8')


fileName = "city.xls"
data = readXls(fileName)
writeXml(data)
