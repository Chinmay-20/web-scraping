from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
import re

html=urlopen('http://www.pythonscraping.com/pages/page3.html')
bs=BS(html,'html.parser')
images=bs.find_all('img',{'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})

for image in images:
	print(image['src'])
