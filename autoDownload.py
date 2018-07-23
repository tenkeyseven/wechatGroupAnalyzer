#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itchat

@itchat.msg_register([itchat.content.ATTACHMENT], isGroupChat=True)
def auto_download(msg):
    print(msg)
    msg.download(msg.fileName)
    sender = itchat.search_friends(userName=msg.fromUserName)
    print('get {} from {} sucessfully'.format(msg.fileName, sender.nickName))
    return

itchat.auto_login(hotReload=True)
itchat.run()
    