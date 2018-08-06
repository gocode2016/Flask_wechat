#!/usr/bin/python3
# -*- coding:utf-8 -*-
from __future__ import unicode_literals
import requests
import json

with open('static/access_token.txt','r') as f:
    access_token = f.read()

def get_menu(access_token):
    res = requests.get('https://api.weixin.qq.com/cgi-bin/menu/get?access_token=%s' % access_token).json()
    return menu


def remove_menu(access_token):
    res = requests.get('https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s' % access_token).json()
    return res

def update_menu(access_token):
    new = {'button': [
                     {'name': '玩家部落', 'sub_button': [
                         {'type': 'view', 'name': '游戏论坛', 'url': 'http://buluo.qq.com/p/barindex.html?bid=391903','sub_button': []},
                         {'type': 'click', 'name': '撩撩小乔', 'key': 'chat_id','sub_button': []}
                                                        ]},
                     {'type': 'view', 'name': '官网', 'url': 'http://sso.siweikongjian.net', 'sub_button': []},
                     {'name': '口令礼包', 'sub_button': [
                         {'type': 'click', 'name': '每日礼包', 'key': 'day_card', 'sub_button': []},
                         {'type': 'click', 'name': '每周礼包', 'key': 'week_card', 'sub_button': []},
                         {'type': 'click', 'name': '每月礼包', 'key': 'month_card', 'sub_button': []},
                                                        ]
                     }
                    ]
               }
    data = json.dumps(new,ensure_ascii=False)
    res = requests.post('https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s' % access_token ,data=data.encode('utf-8'))
    return res.json()

if __name__=='__main__':
    update_menu(access_token)
