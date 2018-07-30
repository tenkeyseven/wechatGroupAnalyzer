#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
【例】微信转发消息工具，转发指定群个人消息至另外一群
例如：
    --在群聊A中，小T发消息：你好
    --在群聊B中有转发消息：及时收到来自群聊【A】，@小T的消息：你好
使用：
    --运行本程序即可，关闭退出即可
说明:
    --目前仅限于接收和转化文本消息，图片、语音、视频、文件暂时未添加功能。
"""

import itchat

@itchat.msg_register([itchat.content.TEXT], isGroupChat=True)
def transfer(msg):
    print('有群聊消息')

    if msg['ToUserName'] == groupID and msg['FromUserName'] == userID:
        '''
        此处注意：
                如果是转化自己发出的消息到其他群应设置判断条件为
                msg['ToUserName'] == groupID and msg['FromUserName'] == userID
                转化发别人消息到其他群则为
                msg['ToUserName'] == userID and msg['FromUserName'] == groupID
        '''
        print('收到关注消息')

        for toGroup in toGroupList:
            toGroupIDList = itchat.search_chatrooms(name=toGroup)
            toGroupID = toGroupIDList[0]['UserName']
            itchat.send('及时转发来自群【{}】,@{}的消息：{}'.format(groupName,userName,msg['Content']),toGroupID)

        print('已转发完成')

def main(userName,groupName,toGroupList):
    global groupID
    global userID

    itchat.auto_login(hotReload=True)
    # 登陆微信
    searchedGroupList = itchat.search_chatrooms(name=groupName)
    groupID = searchedGroupList[0]['UserName']
    chatRoom = itchat.update_chatroom(groupID, detailedMember=True)
    # 搜索指定群聊的id
    for member in chatRoom['MemberList']:
        if member['NickName'] == userName:
            userID = member['UserName']
    # 在指定群聊中搜索指定人员的id

    # print('userID = {}\ngroupID = {}\n'.format(userID,groupID))

    itchat.run()
    # 开始搜索

if __name__ == '__main__':
    '''以下可修改为
    '''
    userName = 'Tenkey'
    groupName = '新时代文化交流群'
    toGroupList = ['啊哈']
    main(userName,groupName,toGroupList)
