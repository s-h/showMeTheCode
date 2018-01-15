#!/usr/bin/env python
#coding: utf-8
#第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：
#[
#    [1, 82, 65535], 
#    [20, 90, 13],
#    [26, 809, 1024]
#]
import xlwt,json
fileName = "number.txt"
with open(fileName) as f:
    data = json.load(f)    

wb = xlwt.Workbook(encoding='utf-8')
ws = wb.add_sheet('number')

for i in range(0,len(data)):
    ws.write(int(i),0,data[i][0])    #(行，列)
    ws.write(int(i),1,data[i][1])
    ws.write(int(i),2,data[i][2])

wb.save('number.xls')

