from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
try:
	html=urlopen('https://pythonscrapingthisurldoesnotexist.com')
except HTTPError as e: #if page is not found 
	print(e)
except URLError as e:
	print('The server could not be found!')
else:
	bs=BeautifulSoup(html.read(),'html.parser')
	print(bs)
