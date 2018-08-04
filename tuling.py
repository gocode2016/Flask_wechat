#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import json
import xml.etree.ElementTree as et
import time

def chat(request):

    xml_data = et.fromstring(request.data)
    ToUserName = xml_data.find('ToUserName').text
    fromUser = xml_data.find('FromUserName').text
    MsgType = xml_data.find('MsgType').text
    Content = xml_data.find('Content').text
    MsgId = xml_data.find('MsgId').text


    data = {
	        "reqType":0,
            "perception": {"inputText": {"text": Content},},
            "userInfo": {"apiKey": "4a8d5245cbfc491bb9468a978e186114","userId": "303496"}
           }
    data1 =json.dumps(data)
    res = requests.post('http://openapi.tuling123.com/openapi/api/v2',data=data1)
    answer =  res.json()['results'][0]['values']['text']


    res = '''<xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[text]]></MsgType>
                <Content><![CDATA[%s]]></Content>
            </xml>'''
    return res % (fromUser, ToUserName, int(time.time()),answer)

if  __name__=='__main__':
    pass