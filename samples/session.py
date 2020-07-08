import json
import requests
import re
from collections import OrderedDict

host = 'http://47.107.178.45'

session = requests.session()

# 首页
res01 = session.get(url = host + '/phpwind/')
rep01 = res01.content.decode('utf-8')

token = re.findall('" name="csrf_token" value="(.+?)"/',rep01)[0]
print(token)

# 登录
# http://47.107.178.45/phpwind/index.php?m=u&c=login&a=dorun
headers_info02 = {
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "X-Requested-With":"XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9"
}

get_param02 = {
                "m" : "u",
                "c" : "login" ,
                "a" :"dorun"}

post_data02 = {
                "username":"sophia.liu",
                "password":"123456",
                "backurl":"",
                "invite	":"",
                "csrf_token":token}

res02 = session.post(url=host+"/phpwind/index.php",
             params=get_param02,
             data= post_data02,
             headers = headers_info02
)
rep02 = res02.content.decode("utf-8")
login_id = re.findall('_statu=(.+?)"',rep02)[0];
# print(login_id)
# print(rep02)

# 授权
get_param03 = {
            "m":"u",
            "c":"login",
            "a":"welcome",
            "_statu":login_id}

res03 = session.get(url=host+"/phpwind/index.php",params=get_param03)
# print(res03.content.decode('utf-8'))

# 发帖
get_param04 = {
    "c": "post",
    "a": "doadd",
    "_json": 1,
    "fid": 80}

mul_form_data = OrderedDict(
    [
        ("atc_title", (None, '第四个帖子_sophia')),
        ("atc_content", (None, '第四个帖子_sophia')),
        ('pid', (None, '')),
        ('tid', (None, '')),
        ('special', (None, 'default')),
        ('reply_notice', (None, '1')),
        ('csrf_token', (None, token))
     ]
)

headers_info04 = {
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "X-Requested-With":"XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    # "Content-Type":"multipart/form-data; boundary=----WebKitFormBoundaryAS42cPv6bKiOKp1e",
    "Accept-Encoding":"gzip,deflate",
    "Accept-Language":"zh-CN,zh;q=0.9"
}

res04 = session.post(url=host+"/phpwind/index.php",
                     headers=headers_info04,
                     params=get_param04,
                     files= mul_form_data
)
print( res04.content.decode('utf-8') )

