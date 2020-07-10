import re
import requests

session = requests.session()

# 授权页面

url = 'http://47.107.178.45' + '/phpwind/'
res = session.get(url=url)
rep = res.content.decode('utf-8')
token = re.findall('" name="csrf_token" value="(.+?)"/', rep)[0]
print(token)

url01 = "http://47.107.178.45/phpwind/index.php"
get_param = {
    "m":"u",
    "c":"register"
}
res01 = session.get(url=url01,params=get_param)
rep01 = res01.content.decode("utf-8")
token01 = re.findall("TOKEN : '(.+?)',	//token ",rep01)[0]
print(token01)

# 注册
url02 = 'http://47.107.178.45/phpwind/index.php'
post_data = {
    "m":"u",
    "c":"register",
    "a":"dorun"
}
get_param = {
    "username":"sophia03",
# 注册
url02 = 'http://47.107.178.45/phpwind/index.php'
get_params={}

post_data = {
    "username":"sophia02",
    "password":"123456",
    "repassword":"123456",
    "email":"test111@cardinfolink.com",
    "csrf_token":token01
}
rep02 = session.post(url=url02,params= get_param,data=get_param)
rep02 = session.post(url=url02,data=post_data,params= )
print(rep02.content.decode("utf-8"))
print(rep02.status_code)