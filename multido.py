# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:19:49 2018

@author: yinti
"""

import re
import ssl 
import urllib.request
import os

ssl._create_default_https_context = ssl._create_unverified_context
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}
url=input('enter the url:')
x=0
def get(url):
    url=urllib.request.Request(url=url,headers=headers)
    h=urllib.request.urlopen(url)
    html=h.read().decode('utf-8')
    return html
def download(html,url):
    urls=re.compile('(img src=".*?\.(jpg|gif|png)")',re.I)
    paths=urls.findall(html)
    print(paths)
    global x
    for path,seq in paths:
        urllib.request.urlretrieve(url+path[9:-1],r'F:/img1/{}.{}'.format(x,path[-4:-1]))
        x+=1
def findurl(html):
    regx=re.compile('(href="(http|https).*?")',re.I)
    h=regx.findall(html)
    s=[]
    for path,seq in h:
        s.append(path)
    return s

html=get(url)
href=findurl(html)
pathd=[url]
for hre in href:
    pathd.append(hre[6:-1])
print(pathd)
for i in pathd:
    if i[-1]!='/':
        i=i+'/'
    else:
        pass
    try:
        htm=get(i)
        download(htm,i)
    except Exception:
        continue
    
