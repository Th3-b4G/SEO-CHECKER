'''
CODE WITH LOVE
@TH3B4G
UNDER GPL V3
'''
import requests
import re
import os
import urllib3
urllib3.disable_warnings()

#color ..............
r = '\x1b[31m'
g = '\x1b[32m'
y = '\x1b[33m'
b = '\x1b[34m'
m = '\x1b[35m'
c = '\x1b[36m'
w = '\x1b[37m'
#......................

#........................

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}


#............................
def clear():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][(os.name == 'nt')])
#...........................
clear()
def daPA(domain):
	payload = 'http://seo.london/domains-authority-checker/?domain='+domain
	data = requests.get(payload,verify=False,headers=headers).content
	find = re.findall('<td>(.*?)</td>', data)
	print(w+'['+r+'CHACKED'+w+']  >> '+c+'DA :'+g+find[1]+'     '+c+'PA :'+g+find[2]+'     '+y+'SITE :'+find[0]+w)

banner = '''
   ,     ,
    {}({}\____/)
     {}({}_{}oo{}_)
       (O)
     __||__   \)
  []{}/{}______\[]/
  / \______/{}\{}/
 /    /__\     DOMAIN
{}({}\   /____\       TOOL 
-----------------'''
print(banner).format(g,w,g,w,r,w,g,w,g,w,g,w)
sitelist = raw_input(c+"SITE LIST : "+g)
sitelist = open(sitelist, 'r')
for site in sitelist:
	daPA(site)
