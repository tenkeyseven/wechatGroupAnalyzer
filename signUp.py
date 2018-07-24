#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
【例子】微信报名签到小工具
使用：
    在微信群中，@<签到管理器>报名，即时返回签到信息
例子：
    小A：@小T 报名
    小T：收到，目前报名人有
        1.小A
"""

import itchat
from collections import Counter

@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def signUp(msg):
    textMsg = msg['Text']
    # 获取信息的文本信息
    robotHostName = '@' + myself['NickName']
    rawMessage = textMsg.replace(robotHostName, '').strip()
    # 去除掉@<机器人名>之后的文本
    groupID = msg['FromUserName']
    # 群ID
    if msg.isAt and rawMessage == '报名':
        if signCounter[groupID] == 0 :
            sendMsg[groupID] = '收到，目前报名人有：'
            # 若第一次@，则创建该群下的计数和信息记录

        signCounter[groupID] += 1
        signUser = msg['ActualNickName']
        sendMsg[groupID] = sendMsg[groupID] + '\n' + str(signCounter[groupID]) + '.' + signUser
        # 将报名计数迭代，且将报名信息更新
        # 每一次添加字符串 <迭代次数>.<报名人ID>

        print(sendMsg[groupID])
        # 控制台输出
        itchat.send(sendMsg[groupID], groupID)
        # 将内容发送到群里

if __name__ == '__main__':
    signCounter = Counter()
    sendMsg = {}

    itchat.auto_login(hotReload=True)
    myself = itchat.search_friends()
    # 获取自身账号信息
    itchat.run()