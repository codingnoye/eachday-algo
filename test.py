from bs4 import BeautifulSoup
from urllib.request import Request,urlopen

req = Request("https://kmucoop.kookmin.ac.kr:42666/restaurant/restaurant.php?w=1")
res = urlopen(req)
html = res.read().decode('cp949')

bs = BeautifulSoup(html, 'lxml')
tags = bs.select('table:nth-of-type(4) tr')
for tag in tags:
    print('1', tag.text)
print(len(tags))