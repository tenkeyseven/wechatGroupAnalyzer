#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import datetime
import json
from pyecharts import Bar
from collections import Counter
from pyecharts import Bar,Pie,Map,WordCloud
import jieba.analyse
import re
import os

def getFiles(inputFile):
    with codecs.open(inputFile,encoding='utf-8') as f:
        friendsList = json.load(f)
        return friendsList

def get_var(var,mlist):
	variable = []
	for i in mlist:
		value = i[var]
		variable.append(value)
	return variable

def peopledic(add,quit):
	dict_temp = {
	        'add'  : [], 
	        'quit' : []
	}
	dict_temp['add'] = add
	dict_temp['quit'] = quit
	return dict_temp

def getSelectedList(mlist,groupName):
	selectedList = []
	for rawGroup in mlist:
		if rawGroup['name'] == groupName:
			selectedList.append(rawGroup)
	return selectedList

def getAddQuitList(mlist):
	addlist = [[]]
	quitlist =[[]]
	lens = len(mlist)
	for i in range(lens):
		addlist.append(mlist[i]['add'])
		quitlist.append(mlist[i]['quit'])
	return addlist,quitlist

def getLenofList(addlist,quitlist):
	lenaddlist = []
	lenquitlist = []

	for i in addlist:
		lenaddlist.append(len(i))

	for i in quitlist:
		lenquitlist.append(len(i))
	return lenaddlist,lenquitlist

def drawBar(timeList,amountList,markdictList,name):
	outputFile='./result/{}_群人员变化表.html'.format(name)
	addlist,quitlist = getAddQuitList(markdictList)
	lenaddlist,lenquitlist = getLenofList(addlist,quitlist)

	bar = Bar('{} 群人员变化表'.format(name),width = 1200, height = 600, title_pos = 'left')
	bar.add(
		'群总人数',
		timeList,amountList,
		tooltip_tragger = 'item',
		tooltip_tragger_on ='mousemove|click',
		is_label_show = True,
	)
	bar.add(
		'较前一时间入群人数',
		timeList,lenaddlist,
		is_label_show = True,
		
	)
	bar.add(
		'较前一时间退群人数',
		timeList,lenquitlist,
		xaxis_name = '检测群时间',
		yaxis_name = '群人数',
		label_color = ['#8A2BE2','#EE2C2C','#7CFC00'],
		is_label_show = True,
		is_datazoom_show = True,
		datazoom_type = 'both',
		xaxis_label_textsize  = '10',
		xaxis_type = 'category'
	)

	bar.render(outputFile)

def analyseProvince(mlist):
	'''use this function to get provinceinfo'''
	provinceCounter = Counter()
	for province in mlist:
		if province != '':
			provinceCounter[province] += 1
	return provinceCounter

def extractTag(text,tagsList):
    if text:
        tags = jieba.analyse.extract_tags(text)

        for tag in tags:
            tagsList[tag] += 1

def analyseSignature(mlist):
	signatureCounter = Counter()
	for signature in mlist:
		signature = signature.strip().replace("emoji", "").replace("span", "").replace("class", "")
		rec = re.compile("1f\d+\w*|[<>/=]")
		signature = rec.sub("", signature)
		extractTag(signature,signatureCounter)
	return signatureCounter

def analyseSexInfo(mlist):
	'''This function accepet an sex list and return the statistics in tuple'''
	male = 0
	female = 0
	unknownsex = 0
	for sex in mlist:
		if sex == 1:
			male += 1
		elif sex == 2:
			female += 1
		else:
			unknownsex += 1
	return (male,female,unknownsex)

def counter2list(_counter):
    nameList,countList = [],[]
    for counter in _counter:
        nameList.append(counter[0])
        countList.append(counter[1])
    return (nameList,countList)

def drawMap(name,rank,chatroomname):
    outputFile = './result/{}_群成员区域分布图.html'.format(chatroomname)
    map = Map(title='{} 群成员区域分布图'.format(chatroomname), width=1200, height=600, title_pos='center')
    map.add(
        '',name,rank,
        maptype = 'china',   # 地图范围
        is_visualmap = True, # 是否开启鼠标缩放漫游等
        is_label_show = True, # 是否显示地图标记
    )
    map.render(outputFile)

def drawWorldCloud(name,rank,chatroomname):
    outputFile = './result/{}_群成员签名词云图.html'.format(chatroomname)
    cloud = WordCloud('{} 群成员签名词云图'.format(chatroomname), width=1200, height=600, title_pos='center')
    cloud.add(
        ' ',name,rank,
        shape='star',
        background_color='white',
        max_words=200 
    )
    cloud.render(outputFile)

def drawPie(name,rank,chatroomname):
    outputFile = './result/{}_群性别比例图.html'.format(chatroomname)
    pie = Pie('{} 群性别比例图'.format(chatroomname), width=1200, height=600, title_pos='center')
    pie.add(
        '',
        name,rank,
        is_label_show = True, # 是否显示标签
        label_text_color = None, # 标签颜色
        legend_orient = 'vertical', # 图例是否垂直
        legend_pos = 'left' 
    )
    pie.render(outputFile)

def analyseGroupByName(selectedList,name):
	nickNameListSet = []
	remarkNameListSet = []
	amountList = []
	timeList = []
	markdictList = []

	for x in selectedList:
		nickNameListSet.append(get_var(var = 'NickName', mlist = x['record']))
		remarkNameListSet.append(get_var(var = 'RemarkName', mlist = x['record']))

	lenofSelectedList = len(selectedList) #this is the len of the name corresponding GrouppList

	for x in range(lenofSelectedList):
		timeList.append(selectedList[x]['time'])
		amountList.append(len(nickNameListSet[x]))

	'''  this loop are use to generate a list containing dictionary of the add/quit info
    '''	
	for i in range(lenofSelectedList-1):                         # the amount of stored groups' all data block
		quitlist = []
		addlist =[]
		for j in range(amountList[i]):
			if nickNameListSet[i][j] in nickNameListSet[i+1]:
				pass
			else:
				quitlist.append(nickNameListSet[i][j])

		for j in range(amountList[i+1]):
			if nickNameListSet[i+1][j] in nickNameListSet[i]:
				pass
			else:
				addlist.append(nickNameListSet[i+1][j])

		markdictList.append(peopledic(add = addlist,quit = quitlist))
		
	print('------------------------分析开始------------------------\n')
	drawBar(timeList,amountList,markdictList,name)
	print("{} 群分析完成!".format(name))
	info = '截至目前一共采集了{}组数据'.format(lenofSelectedList)
	print(info)
	info2 = '人员增减变化、地区分布、词云图、性别比的图表已经生成了，在本文件目录result文件夹下可以找到，接下来给出具体增减成员信息\n'
	print(info2)

	addlist,quitlist = getAddQuitList(markdictList)
	lenaddlist,lenquitlist = getLenofList(addlist,quitlist)

	for i in range(lenofSelectedList):
		print("时间：{}\n群总人数 {}".format(timeList[i],amountList[i]))
		if lenaddlist[i] != 0:
			print("群成员相较于前一次增加了{}人，分别为: ".format(lenaddlist[i]))
			for j in range(len(addlist[i])):
				print(addlist[i][j], end = '  ')
		else:
			print("群成员相较于前一次没有增加")
		if lenquitlist[i] != 0:
			print("\n群成员相较于前一次减少了{}人，分别为： ".format(lenquitlist[i]))
			for j in range(len(quitlist[i])):
				print(quitlist[i][j], end = '  ')
		else:
			print("\n群成员相较于前一次没有减少")
		print('\n')
	print('------------------------分析结束------------------------\n')

def drawThreeGraphies(selectedList, name, Map, Cloud, Pie):

	lenofSelectedList = len(selectedList)
	LatestIndex = lenofSelectedList - 1

	nickNameList = get_var(var = 'NickName', mlist = selectedList[LatestIndex]['record'])
	# remarkNameList = get_var(var = 'RemarkName', mlist = selectedList[LatestIndex]['record'])
	provinceList = get_var(var = 'Province', mlist = selectedList[LatestIndex]['record'])
	# cityList = get_var(var = 'City', mlist = selectedList[LatestIndex]['record'])
	sexList = get_var(var = 'Sex', mlist = selectedList[LatestIndex]['record'])
	signatureList = get_var(var = 'Signature', mlist = selectedList[LatestIndex]['record'])

	total = len(nickNameList)

	# for i in range(total):
	# 	print("{}({}) {} {}{} {}".format(nickNameList[i],remarkNameList[i],provinceList[i],cityList[i],sexList[i],signatureList[i]))

	if Map :
		provinceCounter = analyseProvince(provinceList)
		nameList,ranklist = counter2list(provinceCounter.most_common(15))
		drawMap(nameList,ranklist,name)		
	else:
		pass

	if Cloud :
		signatureCounter = analyseSignature(signatureList)
		nameList,ranklist = counter2list(signatureCounter.most_common(200))
		drawWorldCloud(nameList,ranklist,name)
	else:
		pass

	if Pie:
		sextuple = analyseSexInfo(sexList)
		nameList = ['男','女','未标记']
		ranklist = []
		for i in sextuple:
			ranklist.append(i)
		drawPie(nameList,ranklist,name)
	else:
		pass

def main(GrouppList, Map = True, Cloud = True, Pie = True):
	print("analysing...Please wait a little while")
	inputfiles = './result/records.json'
	if os.path.exists(inputfiles) != True:
		print("Program has stopped, Please make sure data file exists and be in right path")
		return
	dataList = getFiles(inputfiles)
	searchGroupList = GrouppList

	for group in searchGroupList:
		selectedList = getSelectedList(mlist = dataList, groupName = group)
		drawThreeGraphies(selectedList = selectedList, name = group, Map = Map, Cloud = Cloud, Pie = Pie)
		analyseGroupByName(selectedList = selectedList, name = group)

if __name__ == '__main__':
	'''在GroupList中添加需要分析的群名
	   在main函数中相应添加True/False值来确定是否要进行绘制 地理分布图、词云图和性别饼图
	   三个值默认都为True
	   对群成员的分析默认进行绘图。
	'''
	GrouppList = ['pyecharts 可视化交流群','测试','计算机网络2018']
	main(
		GrouppList,
		Map = False,
		Cloud = False,
		Pie = False
	)