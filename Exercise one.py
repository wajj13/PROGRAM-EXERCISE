#获取NBA球员信息

import requests
from lxml import etree

url = 'https://nba.hupu.com/stats/players'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'}
resp = requests.get(url,headers=headers)
e = etree.HTML(resp.text)
nos = e.xpath
with open(‘nba.txt’,'w',encoding = 'UTF-8')