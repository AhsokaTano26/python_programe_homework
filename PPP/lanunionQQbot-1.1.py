#!/usr/bin/env pyrhon3
# Copyright (C) 2019 Lanunion
#
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                    Version 2, December 2004
#
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.

# Config
username='' #用户名
password='' #密码
group_id=[646240303,926050637] #群号
coolqurl="http://127.0.0.1:5700/send_group_msg" #CoolQ http api 地址
delay=150 # s

# Changelog
# 1.1:
#   增强容错能力和可靠性：
#       通过 CoolQ 的返回状态判断是否应该重发，尽量避免单子漏发。
#       在能处理因网络原因无法访问蓝盟网站时产生的错误，使网络恢复后能够自动恢复运行。
#   能够设定发送到多于一个的 QQ 群组。
#   增加加了一些注释。
# 1.0:
#   具备基本的报修单获取功能，并能将其发送给 CoolQ。


from bs4 import BeautifulSoup
import requests
import re
import time
import json
import traceback

httpSession=requests.session()

def login():
    loginPost=httpSession.post('http://lanunion.cqu.edu.cn/repair/admin/index.php/user/loginpost',data={'username':username,'password':password})
    if loginPost.status_code==200:
        loginPost.encoding=loginPost.apparent_encoding
        if "用户名或密码错误" in loginPost.text:
            raise RuntimeError("Error username or password")
        else:
            return True
    else:
        raise RuntimeError("Unexpected status code when trying to login: "+str(loginPost.status_code))

# 获得指定单子的详情
def getBx(num):
    # 每张单子的详情都在 http://lanunion.cqu.edu.cn/repair/admin/index.php/bxsheet/show/xxxx （这个 xxxx 是四个数字，而且这个编号似乎是唯一的？）
    bxSheet=httpSession.get('http://lanunion.cqu.edu.cn/repair/admin/index.php/bxsheet/show/'+num,allow_redirects = False)
    # Cookies 过期时蓝盟后台页面会 203 跳转到登陆页面
    if bxSheet.status_code == 203:
        login()
        getBx()
    bxSheet.encoding=bxSheet.apparent_encoding
    soup=BeautifulSoup(bxSheet.text,features='lxml')
    n=True
    text=''
    for subStr in soup.contents[0].contents[1].stripped_strings:
        if n: subStr='\n\n'+subStr+"："
        text+=subStr
        n=not n
    return text[2:]

# 获取某一页的报修单列表，可选参数 n 为 Str 类型的页码，n 为 '' 时获取所有页码的单子列表。
def getList(n=''):
    # 蓝盟后台的单子列表在 http://lanunion.cqu.edu.cn/repair/admin/index.php/bxsheet/datatable/页码
    listSheet=httpSession.get('http://lanunion.cqu.edu.cn/repair/admin/index.php/bxsheet/datatable/'+n)
    # Cookies 过期时蓝盟后台页面会 203 跳转到登陆页面
    if listSheet.status_code == 203:
        login()
        getList(n)
    listSheet.encoding=listSheet.apparent_encoding
    # 每张单子的详情都在 http://lanunion.cqu.edu.cn/repair/admin/index.php/bxsheet/show/xxxx （这个 xxxx 是四个数字，而且这个编号似乎是唯一的？）
    # 此处通过正则表达式将 xxxx 从网页中提取出来
    bxList=re.findall('<a href="javascript:void\\(0\\)" onclick="showModel\\(\'w\',\'查看报修单\',\'http://lanunion\\.cqu\\.edu\\.cn/repair/admin/index\\.php/bxsheet/show/(\\d*)\',\'show-bxsheet-\\d*\'\\)">查看</a>',listSheet.text)
    if not n:
        # 提取出报修单列表的页码，按页码顺序提取。
        for num in list(map(str,sorted(map(int,set(re.findall('<a href="http://lanunion\\.cqu\\.edu\\.cn/repair/admin/index\\.php/bxsheet/index/(\\d*)">',listSheet.text))))[1:])):
            bxList.extend(getList(n=num))
    return bxList[::-1]
login()
fullList={}
fullList[group_id[0]]=getList()[:-1]

for num in range(1,len(group_id)):
    fullList[group_id[num]]=fullList[group_id[0]]

# 发送信息到指定 QQ 群，这是对 CoolQ http api 的一个简单封装
def sendMsg(text,group):
    try:
        coolqPost=requests.post(coolqurl,data=json.dumps({"group_id":group,"message":text,"auto_escape":True}),headers={'Content-Type':'application/json'})
    except requests.exceptions.ConnectionError:
        traceback.print_exc()
        return False
    time.sleep(2)
    coolqPost.encoding=coolqPost.apparent_encoding
    coolqJson=json.loads(coolqPost.text)
    if coolqJson['status']=='failed':
        return False
    else:
        return True

# 将新获得的单子列表与旧单子列表对比并发送新增单子。
def sendList(newList):
    newFullList={key:[] for key in group_id}
    textList={}
    for group in group_id:
        isStop=False
        for a in newList:
            if a in fullList[group]: newFullList[group].append(a)
            else:
                if not isStop:
                    if not a in textList: textList[a]=getBx(a)
                    if sendBx(textList[a],group): newFullList[group].append(a)
                    else: isStop=True
    return newFullList
def updateList():
    global fullList
    fullList=sendList(getList())

def sendBx(text,group):
    print("-------------------------")
    print(text)
    if sendMsg(text,group):
        return True
    else:
        print("--Failed to send to QQ group "+str(group)+"--")

while True:
    try:
        updateList()
    except requests.exceptions.ConnectionError:
        traceback.print_exc()
    time.sleep(delay)
