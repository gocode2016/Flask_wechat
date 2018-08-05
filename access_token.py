#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests

Token = "sdfrhgcfb452135"
Appid = "wx1faaf9bd50cec162"
Appsecret = "fbff6ed16c87fdbce8dce1dbaf316624"

access_token = requests.get('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (Appid,Appsecret)).json()
print(access_token)