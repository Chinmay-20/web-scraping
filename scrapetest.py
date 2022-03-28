#this application works like browser

from urllib.request import urlopen
html = urlopen('http://pythonscraping.com/pages/page1.html')

print(html.read())

#urllib is standard python library which contains functions for requesting data across web, handling cookies and even changing meta data such as headers and your user agent

#urlopen is used to open a remote object across network and read it. It can read HTML files image files, or any other file stream with ease


