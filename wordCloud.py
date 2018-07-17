#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

【例子】:对微信好友的个性签名生成词云图
引入库说明
    `itchat` 模拟登陆网页版微信
    `jieba`  用于分词
    `pyecharts`  用于绘图
    `collections`  使用Counter经行计数
功能
    模拟登陆微信网页版，获取好友列表签名生成词云图
    在本文件目录下生成词云图的 .html 文件

"""

import itchat
import jieba.analyse
from pyecharts import WordCloud
from collections import Counter

itchat.auto_login(hotReload=True)  #登陆微信

myFriendsList = itchat.get_friends()  #获取微信中的好友列表

signatureCounter = Counter()  #生成一个Counter对象，后续用于词频的计数
for friend in myFriendsList:
	signature = friend['Signature']
	signature = signature.strip().replace('emoji','').replace('class','').replace('span','')  #替换好友签名中表情的代码文本
	tags = jieba.analyse.extract_tags(signature)  #利用jieba分词，统计词频
	for tag in tags:
		signatureCounter[tag] += 1
tagsList = signatureCounter.most_common(200)  #选出分词后词频最高的200个词

wordCloud = WordCloud('你的微信好友签名云图',width=1200, height=600, title_pos='center')  #生成一个词云图对象，用于绘制词云图，在这里设置标题、高度宽度和位置
attr,value = wordCloud.cast(tagsList)
'''利用pyecharts的cast方法将字典列表转换成两个列表用于绘图
   例：
       tagsList = [{'周一':3},{'周二':2},{'周三':1}]
       用cast方法获得
       attr = ['周一','周二','周三']
       value = [3,2,1]
'''
wordCloud.add(
	'',attr,value,
	shape = 'star',
)
'''设置词云图属性，将分词列列表和词频列表添加进入
   设置词云图形状为'start'
   还有的图形 'cardioid', 'diamond', 'triangle-forward', 'triangle', 'pentagon', 'star'

'''
wordCloud.render('./你的微信好友签名云图.html')  #渲染，在本程序目录下生成.html文件		