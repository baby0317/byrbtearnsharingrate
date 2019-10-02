import requests        #导入requests包
import urllib.request
import re
from bs4 import BeautifulSoup
url='https://bt.byr.cn/torrents.php?pktype=2'    #pktype选择种子标签
header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        'cookie': '_ga=GA1.2.539363764.1569910414; _gid=GA1.2.95074819.1569910414; c_secure_ssl=eWVhaA%3D%3D; c_secure_uid=MjE0Njg1; c_secure_pass=fc9aa84921ee624d2c9175ed7ad17310; c_secure_tracker_ssl=bm9wZQ%3D%3D; c_secure_login=bm9wZQ%3D%3D'
        }
res = requests.get(url,headers=header)
print(res)
soup=BeautifulSoup(res.text,'html.parser')
for j in soup.select('tr[class="free_bg"] > td[class="embedded"][width!="20"] > a'):
    print(j['title'])
    print(j['href'])
