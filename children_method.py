from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

html=urlopen('http://pythonscraping.com/pages/page3.html')
bs=BS(html,'html.parser')

for child in bs.find('table',{'id':'giftList'}).children:
	print(child)
