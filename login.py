import requests
from lxml import etree
url='https://www.zhihu.com/'
header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
'cookie': '_zap=e637e2d8-27a1-436c-ac4c-1557e4305847; _xsrf=t86YxVGL0qdJYOinrxQi8GjW8tWXmtVk; d_c0="AOCmNqq4IRCPTj7ao54dviiE8AIGAXFVGC4=|1569920908"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1569921041; tst=r; tgw_l7_route=18884ea8e9aef06cacc0556da5cb4bf1; capsion_ticket="2|1:0|10:1569921858|14:capsion_ticket|44:YzhiNTU2MmVkODk4NDBmNDliMTM4OTk2Njg4Y2FiZDM=|459c6e428ed0ac25bb20ea27b8962bbc96bfb99f27365cf62e3893c8a91c2170"; z_c0="2|1:0|10:1569921865|4:z_c0|92:Mi4xcjU5MUFnQUFBQUFBNEtZMnFyZ2hFQ1lBQUFCZ0FsVk5TV21BWGdDRzRvUk1ETXFRclJlMzZNaXhRSDF3N2ZvR0dR|eb240a083f0f4837fa6b9a26fccdb9e89bde5f073b3bb6785de8a4ebdbdadd94"; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1569921999'
        }
res = requests.get(url,headers=header).text
print(res)
html=etree.HTML(res)
print(html)
ids=html.xpath('//*[@id="TopstoryContent"]/div/div/div/div/div/div/h2/div/a/text()')
print(ids)

