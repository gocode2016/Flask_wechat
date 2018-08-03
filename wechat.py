#!/usr/bin/python3
# -*- coding: utf-8 -*-
import hashlib
import json
import time
from flask import Flask,request
import xml.etree.ElementTree as et


app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        token = 'sdfrhgcfb452135'
        data = request.args
        timestamp = data.get('timestamp')
        nonce = data.get('nonce')
        echostr = data.get('echostr')
        signature = data.get('signature')

        l = [timestamp,nonce,token]
        l.sort()
        mes = ''.join(l)
        sha1 = hashlib.sha1(mes.encode('utf-8')).hexdigest()
        if sha1 == signature :
            return echostr
        else:
            return ''

    if request.method == 'POST':
        xml_data = et.fromstring(request.args)
        ToUserName = xml_rec.find('ToUserName').text
        fromUser = xml_rec.find('FromUserName').text
        MsgType = xml_rec.find('MsgType').text
        Content = xml_rec.find('Content').text
        MsgId = xml_rec.find('MsgId').text
        print(ToUserName,fromUser,Content,MsgId)

        res = '''<xml>
                    <ToUserName><![CDATA[%]]></ToUserName>
                    <FromUserName><![CDATA[%]]></FromUserName>
                    <CreateTime>%s</CreateTime>
                    <MsgType><![CDATA[text]]></MsgType>
                    <Content><![CDATA[你好呀]]></Content>
                </xml>'''
        return res % (fromUser, ToUserName, int(time.time()))


if  __name__=='__main__':
    app.run('0.0.0.0',80,debug=True)