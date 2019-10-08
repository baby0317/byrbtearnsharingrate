# coding=utf-8

import requests        #导入requests包
import urllib.request
import re
import csv
from bs4 import BeautifulSoup
from scrapy import Selector
from lxml import etree

url='https://bt.byr.cn/torrents.php?pktype=1'    #pktype选择种子标签
header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        'cookie': '_ga=GA1.2.539363764.1569910414; c_secure_ssl=eWVhaA%3D%3D; _gid=GA1.2.1218800126.1570513305; _gat=1; c_secure_uid=MjE0Njg1; c_secure_pass=fc9aa84921ee624d2c9175ed7ad17310; c_secure_tracker_ssl=bm9wZQ%3D%3D; c_secure_login=bm9wZQ%3D%3D'
        }
res = requests.get(url,headers=header)
soup=BeautifulSoup(res.text,'html.parser')
response=res.content



def xpath(i):
    xpath='//table[@class="torrents"]//tr[@class="free_bg"]['+str(i)+']'
    print(xpath)
    return xpath

def name(html,xpath):
    path_name=xpath+'/td[@class="rowfollow"][1]/table/tr/td/a/b/text()'
    name = etree.HTML(html).xpath(path_name)
    print('种子名称：',name[0])
    return name[0]

def get_downloadlink(html,xpath):
    path_dl = xpath + '/td[@class="rowfollow"][1]/table/tr/td[2]/a/@href'
    dl = etree.HTML(html).xpath(path_dl)
    dllink=dl[0]
    fdllink='https://bt.byr.cn/'+dllink
    print(fdllink)
    return fdllink

def download(url,i):
    path=str(i)+".exe.torrent"
    download=requests.get(url,headers=header)
    with open(path,"wb") as f:
      f.write(download.content)
    f.close()

def comments(html,xpath):
    path_comments = xpath + '/td[@class="rowfollow"][2]/b/a/text()'
    comment = etree.HTML(html).xpath(path_comments)
    if comment:
        print('评论数：', comment[0])
        comments_str = str(comment[0])
    else:
        print('无评论')
        comments_str='无评论'
    return comments_str

def livetime(html,xpath):
    path_livetime = xpath + '/td[@class="rowfollow nowrap"][2]/span/text()'
    livetime = etree.HTML(html).xpath(path_livetime)
    print('存活时间：' ,livetime[0], livetime[1])
    livetime_str=str(livetime[0])+str(livetime[1])
    return livetime_str

def size(response,xpath):
    path_size=xpath+'/td[@class="rowfollow"][3]/text()'
    size = etree.HTML(response).xpath(path_size)
    print('文件大小：',size[0],size[1])
    size_str=str(size[0])+str(size[1])
    return size_str

def seeders(response, xpath):
    path_seeders=xpath+'/td[@class="rowfollow"][4]/b/a/text()'
    seeders=etree.HTML(response).xpath(path_seeders)
    print('做种数：',seeders[0])
    seeders_str=str(seeders[0])
    return seeders_str

def leechers(response, xpath):
    path_leechers=xpath+'/td[@class="rowfollow"][5]/b/a/text()'
    leechers=etree.HTML(response).xpath(path_leechers)
    if leechers:
        print('下载数：',leechers[0])
        leechers_str = str(leechers[0])
    else:
        print('无正在下载者')
        leechers_str='无正在下载者'
    return leechers_str

def snatched(response, xpath):
    path_snatched=xpath+'/td[@class="rowfollow"][6]/a/b/text()'
    snatched = etree.HTML(response).xpath(path_snatched)
    print('完成数：',snatched[0])
    snatched_str = str(snatched[0])
    return snatched_str

def publisher(response, xpath):
    path_publisher=xpath+'/td[@class="rowfollow"][7]/span/a/b/text()'
    publisher = etree.HTML(response).xpath(path_publisher)
    if publisher:
        print('发布者：', publisher[0])
        publisher_str = str(publisher[0])
    else:
        print('发布者匿名')
        publisher_str = '发布者匿名'
    return publisher_str

with open('torrent_information.csv','w',encoding='utf-8-sig',newline='') as csvfile:
    torrentwriter = csv.writer(csvfile, dialect='excel')
    torrentwriter.writerow(['排名']+['种子名称']+['详情页链接']+['评论数']+['存活时间']+['文件大小']+['做种数']+['下载数']+['完成数']+['发布者'])
    for i in range(1,5):
      torrent_xpath=xpath(i)
      torrent_name=name(response,torrent_xpath)
      torrent_url=get_downloadlink(response,torrent_xpath)
      download(torrent_url,i)
      torrent_comments=comments(response,torrent_xpath)
      torrent_livetime=livetime(response,torrent_xpath)
      torrent_size=size(response,torrent_xpath)
      torrent_seeders = seeders(response, torrent_xpath)
      torrent_leechers = leechers(response, torrent_xpath)
      torrent_snatched = snatched(response, torrent_xpath)
      torrent_publisher = publisher(response, torrent_xpath)

      torrentwriter.writerow([i]+[torrent_name]+[torrent_url]+[torrent_comments]+[torrent_livetime]+[torrent_size]+[torrent_seeders]+[torrent_leechers]+[torrent_snatched]+[torrent_publisher])
