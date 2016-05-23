# downforeveryoneorjustme.com cli client 
# language: python 
# author: brent rubell
# date: 2016
# desc: fetches website status from downforeveryoneorjustme.com and displays to console

import bs4, requests, sys
# string manipulation
urluser = sys.argv[1]
urlfetch = 'http://www.downforeveryoneorjustme.com/'
# .join used, faster than +
url2 =  ''.join([urlfetch, urluser]) 
# requests/bs4
res = requests.get(url2)
res.raise_for_status()
NSS = bs4.BeautifulSoup(res.text)
type(NSS)
elem = NSS.select('#container')
# string manipulation 
str = elem[0].getText()
str2 = str[12:15]
# comparison 
if str2 == 'not':
	print('This site is OFFLINE')    
else:
	print('This site is ONLINE')



