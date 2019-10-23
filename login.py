import requests
from lxml import etree
import VCRmodule
from requests.cookies import RequestsCookieJar

def getimglink(html):
  imgpath='//table[@class="mainouter"]//form[@method="post"]/table[@border="0"]/tr[3]/td[@align="left"]/img/@src'
  imglink = etree.HTML(html).xpath(imgpath)
  print(imglink[0])
  return imglink[0]

def downloadimg(imglink,header):
  path="./img/loginimage.jpg"
  download=requests.get("https://bt.byr.cn/"+imglink,headers=header)
  with open(path,"wb") as f:
      f.write(download.content)
  f.close()
  return path

def char_set(char_new):
    res = char_new.split('=')[2]
    print (res)
    return res

def main(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}

    session=requests.Session()
    r1=session.get('https://bt.byr.cn/login.php',headers=header)
    print(r1.cookies)
    response=r1.content
    imglink=getimglink(response)
    imgpath=downloadimg(imglink,header)
    imgstring=VCRmodule.main(imgpath)
    imagehash = char_set(imglink)
    formdata={
      'username':'HYD0525',
      'password':'HYD112358',
      'imagestring':imgstring,
      'imagehash':imagehash
      }
    r2=session.post('https://bt.byr.cn/takelogin.php',data=formdata, allow_redirects=True)
    print(r2.cookies)

    r3=session.get(url, cookies = r2.cookies,  headers=header)
    print(session.cookies)
    return session.cookies


