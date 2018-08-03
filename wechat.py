#!/usr/bin/python3
# -*- coding: utf-8 -*-
import hashlib
import json
from flask import Flask,request

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
            return None

    if request.method == 'POST':
        return ''

if  __name__=='__main__':
    app.run('0.0.0.0',80,debug=True)