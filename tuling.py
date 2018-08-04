#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import json
import xml.etree.ElementTree as et
import time

class Chat(object):

    def __init__(self, request):
        self.xml_data = et.fromstring(request.data)
        self.ToUserName = self.xml_data.find('ToUserName').text
        self.fromUser = self.xml_data.find('FromUserName').text
        self.MsgType = self.xml_data.find('MsgType').text
        self.Content = self.xml_data.find('Content').text
        self.MsgId = self.xml_data.find('MsgId').text

    def text(self):
        '''xml_data = et.fromstring(request.data)
        ToUserName = xml_data.find('ToUserName').text
        fromUser = xml_data.find('FromUserName').text
        MsgType = xml_data.find('MsgType').text
        Content = xml_data.find('Content').text
        MsgId = xml_data.find('MsgId').text'''

        data = { "reqType": 0,"perception": {"inputText": {"text": self.Content}, },"userInfo": {"apiKey": "4a8d5245cbfc491bb9468a978e186114", "userId": "303496"}}
        data1 = json.dumps(data)

        try:
            post = requests.post('http://openapi.tuling123.com/openapi/api/v2', data=data1, timeout=5)
            answer = post.json()['results'][0]['values']['text']
        except:
            answer = 'success'

        res = '''<xml>
                    <ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime>%s</CreateTime>
                    <MsgType><![CDATA[text]]></MsgType>
                    <Content><![CDATA[%s]]></Content>
                </xml>'''
        return res % (self.fromUser, self.ToUserName, int(time.time()), answer)


if  __name__=='__main__':
    a = Chat([1,2,3])