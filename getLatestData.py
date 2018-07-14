#!/usr/bin/python
# -*- coding: utf-8 -*-
import itchat
import codecs
import json
import datetime
import os

def introduce(GroupList):
	intro = '''
welcome to use this program to know your wechat groups
we can use this program to
1.Know how many people are in this group and who are they.
2.Get visible data in sex ratio, local distribution and signature wordcloud.
3.if run full time, maybe it can get the real time monitoring on group members.
PLEASE MAKE SURE THAT YOU SAVE THIS GROUPCHAT TO YOUR CONTACT
	'''
	print(intro)
	intro_getChatRoom = 'pleae input the amounts of groups you want to know'

	user_chatRoomList = GroupList

	intro_begin = 'OK, program is ready to work, this may take a little while.\n'
	print(intro_begin)

	return user_chatRoomList

def saveFiles(friendsList):
    outputFile = './result/records.json'
    with codecs.open(outputFile,'w',encoding='utf-8') as jsonFile:
        # 默认使用ascii，为了输出中文将参数ensure_ascii设置成False
        jsonFile.write(json.dumps(friendsList,ensure_ascii=False))

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

def getTime():
	return datetime.datetime.now().strftime('%Y-%m-%d|%H:%M:%S')

def generateDict(mlist,name):
	currentTime = getTime()

	currentDict ={
	'time'   :    currentTime,
	'name'   :    name,
	'record' :    mlist
	}

	return currentDict

def saveData(saveddict):
	filesAddress = './result/records.json'
	data = getFiles(filesAddress)
	data.append(saveddict)
	print("Save data sucessfully!")
	print("we have already saved {} data block\n".format(len(data)))
	saveFiles(data)

def makedir(folderAddress):
	if os.path.exists(folderAddress):
		pass
	else:
		os.makedirs(folderAddress)

def init():
	makedir('./result')

	init_list = []

	if os.path.exists('./result/records.json'):
		pass
	else:
		saveFiles(init_list)

def mainWork(chatRoomList):

	itchat.auto_login(hotReload = True)

	for chatRoomName in chatRoomList:
		searchedChatRoomList = itchat.search_chatrooms(chatRoomName)
		''' Try to search the matched chatrooms  '''
		'''                                      '''
		if searchedChatRoomList is None:
			print("{} is not founded".format(chatRoomName))
		elif len(searchedChatRoomList) is 0:
			print("Oh No, We got nothing, ** Make sure that you save this groupchat to contact **")
		else:
			''' get the chatroom '''
			# print(searchedChatRoomList)
			thisUserName = searchedChatRoomList[0]["UserName"]
			# print(thisUserName)      #get the "id" UserName

			chatRoom = itchat.update_chatroom(thisUserName, detailedMember=True) #update the group message，and then return the chatroom
			# print(chatRoom['MemberList'])
			total = len(chatRoom['MemberList']) #get the len of chatroom memberlist

			currentSavedDict = generateDict(chatRoom['MemberList'], chatRoomName)

			saveData(currentSavedDict)
			
if __name__ == '__main__':

	GroupList = ['测试','计算机网络2018']
	init()
	mainWork(introduce(GroupList = GroupList))