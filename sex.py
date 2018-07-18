#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
【例子】分析微信好友性别比例
引入库
    `itchat`  模拟登陆网页版微信
    `pyecharts`  用于绘图
功能
   迷你登陆微信网页版，获取好友列表性别比例
"""

import itchat
from pyecharts import Pie

itchat.auto_login(hotReload=True)  #登陆微信

myFriendList = itchat.get_friends()  #获取微信中的好友列表

sexCounter = {'男' : 0, '女' : 0, '未标注' : 0}

for friend in myFriendList:
	if friend['Sex'] == 1:
		sexCounter['男'] += 1
	elif friend['Sex'] == 2:
		sexCounter['女'] += 1
	else:
		sexCounter['未标注'] += 1

pie = Pie('你的微信好友性别比例图',width=1200, height=600, title_pos='center')
attr, value = pie.cast(sexCounter)
'''利用pyecharts的cast方法将字典列表转换成两个列表用于绘图
   例：
       tagsList = [{'周一':3},{'周二':2},{'周三':1}]
       用cast方法获得
       attr = ['周一','周二','周三']
       value = [3,2,1]
'''
pie.add(
	'',attr,value,
	is_label_show = True,
    legend_orient = 'vertical', # 图例是否垂直
    legend_pos = 'left' 	
)
pie.render('./你的微信好友性别比例图.html') # 绘图渲染
