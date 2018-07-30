#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
【例子】发言热度

"""

import itchat
from itchat.content import TEXT

from collections import Counter

from pyecharts import Bar

import time

@itchat.msg_register(TEXT, isGroupChat=True)
def statistics(msg):
    if msg['FromUserName'] == groupID:
        print('{}发言了:{}'.format(msg['ActualNickName'], msg['Text']))
        talkCounter[msg['ActualNickName']] += 1
        print(talkCounter)

if __name__ == '__main__':s
    itchat.auto_login(hotReload=True)
    groupName = '啊哈'
    groupID = itchat.search_chatrooms(name=groupName)[0]['UserName']

    talkCounter = Counter()
    beginTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    itchat.run()
    endTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    duration = '统计自 {} 到 {} 时间段内'.format(beginTime, endTime)

    bar = Bar(title='{}群活跃度表'.format(groupName), subtitle=duration, width=1200, height=600, title_pos='left')
    attr, value = bar.cast(talkCounter.most_common(100))
    bar.add(
        '', attr, value,
        xaxis_name='昵称',
        yaxis_name='发言活跃度',
        is_label_show = True,
        is_datazoom_show = True,
        datazoom_type = 'both',
        xaxis_name_pos = 'end'
    )
    bar.render('./{}发言活跃度.html'.format(groupName))