#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itchat
from pyecharts import Map
from collections import Counter

itchat.auto_login(hotReload=True)
myFriendList = itchat.get_friends()

provinceCounter = Counter()

for friend in myFriendList:
    province = friend['Province']
    if province != '':
        provinceCounter[province] += 1

myMap = Map('你的微信好友地区分布图',width=1200, height=600, title_pos='center')
attr, value = myMap.cast(provinceCounter)
myMap.add(
    '', attr, value,
    maptype = 'china',
    is_visualmap = True,
    is_label_show = True,
    visual_range = [0,80]
    )

myMap.render('./你的微信好友地区分布图.html')

