from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

try:
	html=urlopen('http://www.pythonscraping.com/pages/page1.html')
except HTTPError as e:
	print(e)
except URLError as e:
	print(e)

try:
	bs=BeautifulSoup(html.read(),'html.parser')

#BeautifulSoup has find_all function to extract python list of proper nouns found by selecting only text 
	nameList=bs.find_all('span',{'class':'green'}) #there are two separate functions findAll and find_all
	for name in nameList:
		print(name.get_text()) #get_text to print content separate from tag
except ArrtributeError as e:
	print(e)
