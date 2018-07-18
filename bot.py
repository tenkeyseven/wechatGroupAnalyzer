#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itchat
import requests

KEY = 'd6adf489248347428178a7bbff5502a7'

def get_response(msg):
	apiUrl = 'http://www.tuling123.com/openapi/api'
	data = {
    'key'    : KEY, 
    'info'   : msg, 
    'userid' : 'wechat-robot', 
	}

	try:
		r = requests.post(apiUrl, data=data).json()
		return r.get('text')
	except:
		return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
	defaultReply = '我收到你的消息啦，让我想想~'
	reply = get_response(msg['Text'])
	return reply or defaultReply

itchat.auto_login(hotReload=True)
itchat.run()
