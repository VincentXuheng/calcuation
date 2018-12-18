# -*- coding:utf-8 -*-
"""

 抓取OA通讯录信息，并写入到文件中

"""
import re
import requests
import xlsxwriter

num=range(170228001,170228037)
root='http://100.100.20.215:5120/employee/search?name=&badge='
root2='&phone=&mobileshort='
count=0
badge=[]
phone=[]
name=[]
officephone=[]
stationname=[]
workplace=[]
for i in range(0,len(num)):
    url=root+str(num[i])+root2
    r=requests.get(url,timeout=60)
    r.encoding=r.apparent_encoding
    if len(r.text)>10:
        print(r.text)
        temp=re.split(',',r.text)
        badge.append(temp[0][11:20:])
        phone.append(temp[1][9:20:])
        name.append(temp[2][8::][len(temp[2][8::])-2::-1][::-1])
        officephone.append(temp[3][15::][len(temp[3][15::])-2::-1][::-1])
        stationname.append(temp[6][15::][len(temp[6][15::])-2::-1][::-1])
        workplace.append(temp[7][13::][len(temp[7][13::])-4::-1][::-1])


workbook=xlsxwriter.Workbook(u"d:\通讯录.xlsx")
worksheet=workbook.add_worksheet("17届")
title=[u"name",u"badge",u"phone",u"officephone",u"stationname",u"workplace"]
worksheet.write_row("A1",title)
for i in range(len(name)):
    num=str(i+2)
    row='A'+num
    data=[i+1,name[i],badge[i],phone[i],officephone[i],stationname[i],workplace[i],]
    worksheet.write_row(row,data)
    i+=1
workbook.close()

