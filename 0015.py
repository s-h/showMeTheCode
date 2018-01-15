#!/usr/bin/env python
#coding: utf-8
#第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：
#{
#   "1" : "上海",
#   "2" : "北京",
#   "3" : "成都"
#}
import xlwt,json
fileName = "city.txt"
with open(fileName) as f:
    data = json.load(f)

wb = xlwt.Workbook(encoding='utf-8')
ws = wb.add_sheet('city')

for i in data:
    ws.write(int(i)-1,0,i)    #(行，列)
    ws.write(int(i)-1,1,data[i])

wb.save('city.xls')
