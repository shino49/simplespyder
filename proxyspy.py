# -*- coding: utf-8 -*-

"""
@author: yinti
email:yintianze49@gmail.com
"""

import re
import ssl 
import urllib.request
import os
import zlib
import chardet
import time
from validateIP import validateIP

ssl._create_default_https_context = ssl._create_unverified_context
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}
def get(url):
    url=urllib.request.Request(url=url,headers=headers)
    h=urllib.request.urlopen(url)
    html=h.read()
    html = zlib.decompress(html, 16+zlib.MAX_WBITS)
    #print(chardet.detect(html))
    html=html.decode('utf-8')
    return html
def findurl(html):
    regx=re.compile('(href="(http|https).*?")',re.I)
    h=regx.findall(html)
    s=[]
    for path,seq in h:
        s.append(path)
    return s
def findproxy(url):
    pattip=re.compile('(<td data-title="IP">(\d|\.)*)',re.I)
    pattport=re.compile('<td data-title="PORT">(\d{1,6})',re.I)
    html=get(url)
    ip=pattip.findall(html)
    port=pattport.findall(html)
    f=[]
    s=[]
    if len(ip)==len(port):
        f1=open(r'E:\source code\python\spy\data\ippool\proxyip2.txt','at')
        for n in range(len(ip)):
            f.append(ip[n][0][20:]+":"+port[n])           
            if validateIP(ip[n][0][20:],port[n])==True:
                s.append(ip[n][0][20:]+":"+port[n]+'\n')
        print(f)
        print(s)
        f1.writelines(s)
        f1.close()
        #return s
    else:
        print('false')
for i in range(1,21):
    try:
        url='https://www.kuaidaili.com/free/intr/{}/'.format(i)
        findproxy(url)
        time.sleep(2)
    except Exception:
        continue
