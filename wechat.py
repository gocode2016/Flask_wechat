#!/usr/bin/python3
# -*- coding: utf-8 -*-
import hashlib
import json
import time
from flask import Flask,request
import xml.etree.ElementTree as et
from tuling import  Chat

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
        mes = Chat(request)
        xml_data = et.fromstring(request.data)  #text,image,voice,video,shortvideo,location,link] 消息类型

        if  xml_data.find('MsgType').text == 'text':
            res = mes.text()
        elif  xml_data.find('MsgType').text == 'image':
            res = mes.image()
        elif  xml_data.find('MsgType').text == 'voice':
            res = mes.voice()
        else:
            return 'success'
        return res

if  __name__=='__main__':
    app.run('0.0.0.0',80,debug=True)