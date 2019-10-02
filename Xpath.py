import requests
from lxml import etree
url='https://movie.douban.com/chart'
header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
r = requests.get(url,headers=header).text
print(r)
html=etree.HTML(res)
print(html)
ids=html.xpath('//*[@id="TopstoryContent"]/div/div/div/div/div/div/h2/div/a/text()')
print(ids)
