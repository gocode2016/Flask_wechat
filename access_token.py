#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import time
import schedule
import datetime
Token = "sdfrhgcfb452135"
Appid = "wx1faaf9bd50cec162"
Appsecret = "fbff6ed16c87fdbce8dce1dbaf316624"


def get_access_token():
    at = time.time()
    access_token = requests.get('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (Appid,Appsecret)).json()
    with open('access_token.txt','w') as f:
        print(access_token,file=f)
    return access_token

if __name__=='__main__':

    schedule.every(120).minutes.do(get_access_token())
    while True:                                         ### 每30秒检查一次时间
        schedule.run_pending()
        print(datetime.datetime.now())
        time.sleep(30)
