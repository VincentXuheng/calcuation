# coding:utf8

import re
import urllib
import urllib2
import cookielib

loginUrl = 'http://211.87.126.78/loginAction.do'

#cookie
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
#postdata
values = {
    'zjh':'20130503235',
    'mm':'20130503235',
    'v_yzm':''
}
postdata = urllib.urlencode(values)
#headers
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Referer':'http://211.87.126.78/loginAction.do'
}

#第一次请求网页得到cookie
request = urllib2.Request(loginUrl,postdata,headers=header)
response = opener.open(request)
print '第一次请求网页得到cookie:'
print response.getcode()

#获取验证码----------------
yzm = opener.open('http://211.87.126.78/validateCodeAction.do')
yzm_data =  yzm.read()
yzm_pic = file('yzm.jpg','wb')
yzm_pic.write(yzm_data)
yzm_pic.close()


#用户输入验证码
print '请输入验证码：'
values['v_yzm'] = raw_input()
#带验证码模拟登陆
postdata = urllib.urlencode(values)
request = urllib2.Request(loginUrl,postdata,header)
response = opener.open(request)
print 'Response of loginAction.do'




top_url = 'http://211.87.126.78/gradeLnAllAction.do?type=ln&oper=qbinfo&lnxndm=2016-2017学年秋(两学期)'
response = opener.open(top_url)
print 'Response of top.jsp'
content = response.read().decode('gbk')

pattern = re.compile('<tr.*?class="odd".*?</td>.*?</td>.*?<td align="center">(.*?)</td>.*?<p align="center">(.*?)&nbsp;</P>', re.S)
grades = re.findall(pattern, content)
for grade in grades:
    print grade[0], grade[1]

input("Prease <enter>")

