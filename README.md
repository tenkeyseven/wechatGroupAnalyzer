#  微信群分析器

`python 3.6`  `itchat`  `pyecharts`  `jieba`                                 

##  实现功能

### 1.群聊人员增减分析

#### 	增减数量图

![](https://github.com/tenkeyseven/wechatGroupAnalyzer/blob/master/Images/change.png)

#### 	具体情况输出 

<div align="center">
<img src="https://github.com/tenkeyseven/wechatGroupAnalyzer/blob/master/Images/changedetails.png"></img>
</div>

### 2.生成群成员三图（地区分布图、签名词云图、性别比例图）

#### 	地区分布图



![](https://github.com/tenkeyseven/wechatGroupAnalyzer/blob/master/Images/reigon.png)

#### 	群成员签名词云图 



![](https://github.com/tenkeyseven/wechatGroupAnalyzer/blob/master/Images/cloud.png)

#### 	群成员性别比例图



![](https://github.com/tenkeyseven/wechatGroupAnalyzer/blob/master/Images/sex.png)

## 使用说明

基于`python3.6`环境开发，使用了微信端第三方 Api 库`itchat`，echarts 的 python 接口库`pyecharts`， 分词库`jieba`，以及其他一些在程序工作中要用到了编解码、存储等库。

安装方法：

```
pip install itchat
pip install pyecharts
pip install jieba
```

此分析器包含两个 python 程序，分别为 getLatestData.py 和 analyzeData.py 。

getLatestData.py 用于对指定的群列表获取最新的群成员信息，并写入文件保存。

analyzeData.py 用于对指定的群列表进行分析，输出群成员变化细则、群成员人数增减图和三图（群成员分布图、群成员签名云图和群成员性别比例图）

### 使用流程

1. 在手机上确定要分析的群聊，点开设置，将群聊保存至通讯录(Save to Contacts)。
2. 运行 getLatestData.py，第一次登陆，会弹出二维码，使用手机扫码登陆微信网页版，并确认，之后登陆只需要在手机确认即可。
3. 程序将会自动生成文件夹result，并将原始数据保存至此。
4. 运行 analyzeData.py，程序将会对数据进行分析，输出分许结果以及生成相应的图。

### 参数说明 

在 getLatestData.py 中，参数设置如下

```python
#getLatestData.py
if __name__ == '__main__':
	'''在GroupList中输入想要分析的群聊名称，输入login的参数
		login = 'auto',会调用itchat的自动缓存登陆模式，第二次登陆无需扫码
		适用于持续使用者
		logn = 'single',会调用itchat单次扫码登陆模式，适合于一次使用。
	'''
	GroupList = ['测试','计算机网络2018']
	introduce()
	init()
	mainWork(
		GroupList,
		login = 'auto'
	)
```



在 analyzeData.py 中，参数设置应如下

```python
#analyzeData.py
if __name__ == '__main__':
	'''在GroupList中添加需要分析的群名
	   在main函数中相应添加True/False值来确定是否要进行绘制 地理分布图、词云图和性别饼图
	   三个值默认都为True
	   对群成员的分析默认进行绘图。
	'''
	GrouppList = ['测试','计算机网络2018']
	main(
		GrouppList,
		Map = True,      #True 或 默认 为开启画图，False为不开启
		Cloud = True,    
		Pie = True       
	)
```

### 其他

对群成员人数增减进行分析依赖于多次采集的数据，而绘制三图相对不受人员变化影响，所以可以在第一次三图绘制好之后，将其设置为False，每次分析数据只分析人员变化。

### 参考内容

+ [pyecharts](https://github.com/pyecharts/pyecharts)
+ [itchat](https://github.com/littlecodersh/ItChat)
+ [CSDN:利用itchat接口进行微信好友数据分析](https://blog.csdn.net/alicelmx/article/details/80862340)

### 其他内容

---

![](https://img.shields.io/badge/Tenkeyseven-(%20%E2%80%A2%CC%80%20%CF%89%20%E2%80%A2%CC%81%20)%E2%9C%A7-green.svg)一些小例子

#### 1.微信好友的词云图

**依赖库安装**

`pip install itchat`

`pip install pyecharts`

**运行代码**

[有注释的代码](https://github.com/tenkeyseven/wechatGroupAnalyzer/blob/master/wordCloud.py)



#### 2.微信好友性别比

**依赖库安装**

`pip install itchat`

`pip install pyecharts`

**运行代码**

[有注释的代码](https://github.com/tenkeyseven/wechatGroupAnalyzer/blob/master/sex.py)



#### 3.微信好友地区分布图

**使用**

和以上两种一样，运行后会自动在程序根目录生成.html电子图

**依赖库安装**

`pip install itchat`

`pip install pyecharts`

`pip install echarts-countries-pypkg   `（安装必要的地图

**运行代码**

[代码](https://github.com/tenkeyseven/wechatGroupAnalyzer/blob/master/provinceMap.py)





#### 4.图灵小机器人私戳版（不是很图灵...）
**依赖库安装**

`pip install itchat`

**运行代码**

[bot.py的代码](https://github.com/tenkeyseven/wechatGroupAnalyzer/blob/master/bot.py)



#### 5.图灵小机器人群聊版（不是那么图灵+1）

**使用**

运行程序，在群里@机器人并且带消息，然后机器人就会在群里自动回复你了~

**依赖库安装**

`pip install itchat`

**运行代码**

[群聊版代码](https://github.com/tenkeyseven/wechatGroupAnalyzer/blob/master/groupBot.py)



#### 6.非常简单的群聊文件自动下载工具

**使用**

运行程序，然后此程序自动下载微信群中别人发的文件。

**依赖库安装**

`pip install itchat`

**运行代码**

[代码](https://github.com/tenkeyseven/wechatGroupAnalyzer/blob/master/autoDownload.py)



#### 7.微信消息转化器v1

**使用**

【例】微信转发消息工具，转发指定群个人消息至另外一群
例如：
    --在群聊A中，小T发消息：你好
    --在群聊B中有转发消息：及时收到来自群聊【A】，@小T的消息：你好
使用：
    --运行本程序即可，关闭退出即可
说明:
    --目前仅限于接收和转化文本消息，图片、语音、视频、文件暂时未添加功能。

**依赖库安装**

`pip install itchat`

**运行代码**

[有注释的代码](https://github.com/tenkeyseven/wechatGroupAnalyzer/blob/master/transfer_single.py)