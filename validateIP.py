# -*- coding: utf-8 -*-

"""
@author: yinti
email:yintianze49@gmail.com
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
