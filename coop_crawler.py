#!/usr/bin/env python
# coding: utf-8

from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup as BS



def header(url):
	url.add_header('Host','coop.jwsh.tp.edu.tw')
	url.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:40.0) Gecko/20100101 Firefox/40.0')
	url.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
	url.add_header('Accept-Language','zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3')
	url.add_header('Accept-Encoding','gzip, deflate')
	url.add_header('Connection','keep-alive')

def setuserid():
	global startuserid
	global crawlerNum
	global resultsList
	global useridList
	resultsList = []
	useridList = []
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
			header(req)
			x = urlopen(req)
			req = x.read()
			reqBS = BS(req,"html.parser")
		
			#Data of Request
			results = reqBS.find('font', {'color':'#bb0000'}).string
			resultsList.append(results)
			
		except:
			print ('查詢失敗：'+str(x))
			resultsList.append('')

def printResult():
	resultsFile = open('CrawlerResults.txt','w')
	print ('=========最終結果=========')
	for z in range(len(resultsList)):
		print (str(useridList[z])+'：',end='')
		print (str(useridList[z])+'：',end='',file=resultsFile)
		if len(resultsList[z]) <= 3:	
			print (resultsList[z])
			print (resultsList[z],file=resultsFile)
		else:
			print ('')
			print ('',file=resultsFile)
	print ('==========================')

def main():
	setuserid()
	generateUserIDList()
	get()
	printResult()
	main()

main()