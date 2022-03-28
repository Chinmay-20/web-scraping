from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def getTitle(url):
	try:
		html=urlopen(url)
	except HTTPError as e:
		print(e)
	except URLError as e:
		print(e)
	try:
		bs=BeautifulSoup(html.read(),'html.parser')
		title=bs.body.h1
	except AttributeError as e:
		print(e)
	return title
	
title=getTitle('https://www.pythonscraping.com/pages/page1.html')
if title==None:
	print('Title could not be found')
else:
	print(title)

