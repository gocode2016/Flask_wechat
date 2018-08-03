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
        data = json.dumps(request.args)
        timestamp = data['timestamp']
        nonce = data['nonce']
        echostr = data['echostr']
        signature = data['signature']

        l = [timestamp,nonce,echostr].sort()
        mes = l[0]+l[1]+l[2]
        sha1 = hashlib.sha1(mes).hexdigest()
        if sha1 == signature :
            return echostr
        else:
            return None

if  __name__=='__main__':
    app.run('0.0.0.0',80,debug=True)