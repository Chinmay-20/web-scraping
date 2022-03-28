from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

html=urlopen('http://www.pythonscraping.com/pages/page3.html')
bs=BS(html,'html.parser')

for sibling in bs.find('table',{'id':'giftList'}).tr.next_siblings:
	print(sibling)
	
#output is to print all rows of product from product table except for first title row. and it is skipped because object cannot be siblings of themselves. it calls next siblings only

