#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
【例】图灵小机器人的群聊版
功能：
    开启后，在群里@机器人并带上消息，机器人会在群聊里@提问者并回复
    机器人回复内容来自 http://www.tuling123.com/openapi/api，
    KEY值是使用api的通行证，可以自己申请。

"""

import itchat
import requests

def get_response(info):
	'''
	此函数用于调用API获取回复，若出现问题时，将会返回一个空值
	'''
	apiUrl = 'http://www.tuling123.com/openapi/api'
	data = {
    'key'    : KEY, 
    'info'   : info, 
    'userid' : 'wechat-robot', 
	}

	try:
		r = requests.post(apiUrl, data=data).json()
		return r.get('text')
	except:
		return
def getReply(text):
	'''
    此函数用于群里@机器人后消息的处理，处理除去@<机器人名>后的文本消息
	'''
	if text == '':
		return '@机器人的同时说些什么吧~'
	defalutReply = '机器人开小差了等会儿再试试吧'
	reply = get_response(text)
	return reply or defalutReply

@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def group_reply(msg):
	'''
	此函数用于接收群聊消息和回复消息，只有机器人被@之后，才做出回复
	例：
	   （在某群中）
	   群成员小k : @robot 你好啊
	   robot自动回复 ： @小k: 你也好呀
	'''

	# textMsg = msg['Text']
	print('收到群消息：{}'.format(textMsg))
	if msg.isAt:
		robotHostName = '@' + myself['NickName']
		rawMessage = textMsg.replace(robotHostName, '')   #对获取的消息做处理，将@<机器人名>从文本中去除
		# print('{}'.format(rawMessage))
		itchat.send(u'@{}\u2005: {}'.format(msg['ActualNickName'], getReply(rawMessage)),msg['FromUserName'])

if __name__ == '__main__':
	KEY = 'd6adf489248347428178a7bbff5502a7'
	itchat.auto_login(hotReload=True)  #登陆微信
	myself = itchat.search_friends()  #获取机器人账号自己的消息
	itchat.run()