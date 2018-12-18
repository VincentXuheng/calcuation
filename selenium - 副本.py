# -*- coding:utf-8 -*-
import requests
import bs4
from bs4 import BeautifulSoup
import csv

url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
ulist=[]
num=int(input('请输入需要多少：'))

r=requests.get(url,timeout=30)
r.raise_for_status()
r.encoding=r.apparent_encoding
html=r.text
soup=BeautifulSoup(html,'html.parser')
for tr in soup.find('tbody').children:
    if isinstance(tr,bs4.element.Tag):
        tds=tr('td')
        ulist.append([tds[0].string,tds[1].string,tds[2].string])

print("{:^10}\t{:^6}\t{:^10}".format("排名",'学校名称',"地区"))
with open('D:\\pic\\1.csv','a') as csvfile:
    write=csv.writer(csvfile)
    write.writerow(["index","a",'b'])
for i in range(num):
    u=ulist[i]
    print('{:^10}\t{:^6}\t{:^10}'.format(u[0],u[1],u[2]))
    with open('D:\\pic\\1.csv','a') as csvfile:
        write=csv.writer(csvfile)
        write.writerows([u[0],u[1],u[2]])
    with open('D:\\pic\\2.txt','a') as f:
        f.write(str([u[0],u[1],u[2]]))
    
input("jjjj")
