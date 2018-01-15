#!/usr/bin/env python
#coding: utf-8
#第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
#{
#        "1":["张三",150,120,100],
#        "2":["李四",90,99,95],
#        "3":["王五",60,66,68]
#}
import xlwt,json
fileName = "student.txt"
with open(fileName) as f:
    data = json.load(f)

wb = xlwt.Workbook(encoding='utf-8')
ws = wb.add_sheet('student')

for i in data:
    ws.write(int(i)-1,0,i)    #(行，列)
    ws.write(int(i)-1,1,data[i][0])
    ws.write(int(i)-1,2,data[i][1])
    ws.write(int(i)-1,3,data[i][2])
    ws.write(int(i)-1,4,data[i][3])

wb.save('student.xls')
