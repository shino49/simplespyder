# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 10:39:18 2018

@author: yinti
"""
import requests
def validateIP(IP,port):
    url="http://ip.chinaz.com/getip.aspx"
    try:
        proxy_host={port:IP}
        html=requests.get(url,proxies=proxy_host,timeout=3)
        txt=html.text
        if(html.status_code==200):
            return(True)
        else:
            return False
    except:
        return 'error'
