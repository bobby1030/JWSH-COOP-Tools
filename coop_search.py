#!/usr/bin/env python
# coding: utf-8

from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup as BS

item = ['姓名：','餘額：','累積消費額：']
results = []

def setuserid():
	global userid
	userid = str(input('請輸入您的學號：'))

def get():
	rawRequest = [
	        'userid='+userid,
			'password='+userid
				]
	
	req = Request('http://coop.jwsh.tp.edu.tw/',data='&'.join(rawRequest).encode())
	x = urlopen(req)
	req = x.read()
	reqBS = BS(req,"html.parser")

	for i in reqBS.findAll('font', {'color':'#bb0000'}):
		results.append(i.string)

def printResult():
	print ('查詢結果：')

	for x in range(3):
		print ('	',end='')
		print (item[x]+results[x])
	print ('')
def main():
	setuserid()
	get()
	printResult()
	main()

if __name__ == "__main__":
	main()
