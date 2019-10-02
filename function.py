import requests        #导入requests包
import urllib.request
import re
from bs4 import BeautifulSoup
from scrapy import Selector
from lxml import etree
url='https://bt.byr.cn/torrents.php?pktype=1'    #pktype选择种子标签
header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        'cookie': '_ga=GA1.2.539363764.1569910414; _gid=GA1.2.95074819.1569910414; c_secure_ssl=eWVhaA%3D%3D; c_secure_uid=MjE0Njg1; c_secure_pass=fc9aa84921ee624d2c9175ed7ad17310; c_secure_tracker_ssl=bm9wZQ%3D%3D; c_secure_login=bm9wZQ%3D%3D'
        }
res = requests.get(url,headers=header)
#print(res.text)
soup=BeautifulSoup(res.text,'html.parser')
response=res.content
#path="byrbt.html"
#with open(path,"wb") as f:
  #f.write(response)
#f.close()

def name(html):
  #name1=html.select_one('tr[class="free_bg"] > td[class="rowfollow"] > table[class="torrentname"] > tr[class="free_bg"] > td[class="embedded"] > a')
  name = etree.HTML(html).xpath(
      '//table[@class="torrents"]//tr[@class="free_bg"][1]/td[@class="rowfollow"][1]/table/tr/td/a/b/text()')
  #print('种子名称：',name.title)
  #print('详情页：',name['href'])
  print('种子名称：',name[0])
  return html

def get_downloadlink(html):
  #dl=html.select_one('tr[class="free_bg"] > td[class="rowfollow"] > table[class="torrentname"] > tr[class="free_bg"] > td[class="embedded"][width="20"] > a')
  dl = etree.HTML(html).xpath(
      '//table[@class="torrents"]//tr[@class="free_bg"][1]/td[@class="rowfollow"][1]/table/tr/td[2]/a/@href')
  #dllink=dl['href']
  dllink=dl[0]
  fdllink='https://bt.byr.cn/'+dllink
  print(fdllink)
  return fdllink

def download(url):
  path="test1.exe.torrent"
  download=requests.get(url,headers=header)
  with open(path,"wb") as f:
    f.write(download.content)
  f.close()

def comments(html):
    comment=html.select_one('tr[class="free_bg"] > td[class="rowfollow"]> a[title="添加评论"]')
    print('评论数：',comment.text)
    return comment.text

def livetime(html):
    livetime = html.select_one('tr[class="free_bg"] > td[class="rowfollow nowrap"]> span')
    print('存活时间：',livetime.text)
    return livetime.text

def attributes(response):
    size=etree.HTML(response).xpath('//table[@class="torrents"]//tr[@class="free_bg"][1]/td[@class="rowfollow"][3]/text()')
    print('文件大小：',size)
    seeders=etree.HTML(response).xpath('//table[@class="torrents"]//tr[@class="free_bg"][1]/td[@class="rowfollow"][4]/b/a/text()')
    print('做种数：',seeders)
    leechers=etree.HTML(response).xpath('//table[@class="torrents"]//tr[@class="free_bg"][1]/td[@class="rowfollow"][5]/b/a/text()')
    print('下载数：',leechers)
    snatched=etree.HTML(response).xpath('//table[@class="torrents"]//tr[@class="free_bg"][1]/td[@class="rowfollow"][6]/a/b/text()')
    print('完成数：',snatched)
    fabuzhe=etree.HTML(response).xpath('//table[@class="torrents"]//tr[@class="free_bg"][1]/td[@class="rowfollow"][7]/span/a/b/text()')
    print('发布者：',fabuzhe)

name(response)
url1=get_downloadlink(response)
download(url1)
comments(soup)
livetime(soup)
attributes(response)
