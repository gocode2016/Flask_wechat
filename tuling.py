#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import json
import xml.etree.ElementTree as et
import time

class Chat(object):

    def __init__(self, request):
        self.xml_data = et.fromstring(request.data)  #text,image,voice,video,shortvideo,location,link] 消息类型
        if  self.xml_data.find('MsgType').text == 'text':
            self.Content = self.xml_data.find('Content').text
        elif    self.xml_data.find('MsgType').text == 'image':
            self.PicUrl =   self.xml_data.find('PicUrl').text
            self.MediaId = self.xml_data.find('MediaId').text
        elif    self.xml_data.find('MsgType').text == 'voice':
            self.MediaId = self.xml_data.find('MediaId').text
            self.Format = self.xml_data.find('Format').text
        else:
            pass

        self.ToUserName = self.xml_data.find('ToUserName').text
        self.fromUser = self.xml_data.find('FromUserName').text
        self.MsgType = self.xml_data.find('MsgType').text
        self.MsgId = self.xml_data.find('MsgId').text

    def text(self):
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
                    <MsgType><![CDATA[voice]]></MsgType>
                    <Content><![CDATA[%s]]></Content>
                </xml>'''
        return res % (self.fromUser, self.ToUserName, int(time.time()), answer)


    def image(self):
        pass



    def voice(self):
        data = {"reqType": 0, "perception": {"inputMedia": {"url": self.MediaId}, },"userInfo": {"apiKey": "4a8d5245cbfc491bb9468a978e186114", "userId": "303496"}}
        data1 = json.dumps(data)
        try:
            post = requests.post('http://openapi.tuling123.com/openapi/api/v2', data=data1, timeout=5)
            answer = post.json()['results'][0]['values']['url']
        except:
            return 'success'
        res = '''<xml>
                    <ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime>%s</CreateTime>
                    <MsgType><![CDATA[text]]></MsgType>
                    <MediaId>< ![CDATA[%s]]></MediaId>
                    <Format>< ![CDATA[%s]]></Format>
                 </xml>'''
        return res % (self.fromUser, self.ToUserName, int(time.time()),answer,self.Format)


if  __name__=='__main__':
    data = {"reqType": 0, "perception": {"inputMedia": {"url": self.MediaId}, },
            "userInfo": {"apiKey": "4a8d5245cbfc491bb9468a978e186114", "userId": "303496"}}
    data1 = json.dumps(data)
    post = requests.post('http://openapi.tuling123.com/openapi/api/v2', data=data1, timeout=5)
    answer = post.json()['results'][0]['values']['url']
    print(answer)