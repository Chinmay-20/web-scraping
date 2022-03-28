from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

try:
	html=urlopen("https://docs.google.com/document/d/1mG_dn1F9-a_hN2Y5OACCYi4gI-gt8TKPCHSZctj5lhs/edit")
	bs=BeautifulSoup(html.read(),'lxml') #two arguments are required first is HTML object and second is parser that you want Beautful soup to use in order to create that object
#most of times we use html.parser or lxml
except HTTPError as e:
	print(e)
#print(bs.h1) #this will return first instance of tag only
#print(bs.title)
print(bs)
