import requests
from lxml import etree
url='https://bt.byr.cn/torrents.php?pktype=1'
header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        'cookie': '_ga=GA1.2.539363764.1569910414; _gid=GA1.2.95074819.1569910414; c_secure_ssl=eWVhaA%3D%3D; c_secure_uid=MjE0Njg1; c_secure_pass=fc9aa84921ee624d2c9175ed7ad17310; c_secure_tracker_ssl=bm9wZQ%3D%3D; c_secure_login=bm9wZQ%3D%3D'
        }
res = requests.get(url,headers=header).text
print(res)
html=etree.HTML(res)
print(html)
ids=html.xpath('//*[@id="outer"]/table[@class="main"]/tr/td[@class="embedded"]/table[@class="torrents"]/tr[2]/td[2]/table[@class="torrentname"]/tr/td[1]/a/text()')   #种子标题信息
print(ids)

