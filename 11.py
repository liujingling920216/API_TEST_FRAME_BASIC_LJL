import re
import requests

session = requests.session()

# 授权页面
# url = 'http://47.107.178.45' + '/phpwind/'
# res = session.get(url=url)
# rep = res.content.decode('utf-8')
# token = re.findall('" name="csrf_token" value="(.+?)"/', rep)[0]
# print(token)
# 授权页面
url01 = "http://47.107.178.45/phpwind/index.php"
get_param01 = {
    "m":"u",
    "c":"register"
}
res01 = session.get(url=url01,params=get_param01)
rep01 = res01.content.decode("utf-8")
token01 = re.findall("TOKEN : '(.+?)',	//token ",rep01)[0]
print(token01)

# 注册
url02 = 'http://47.107.178.45/phpwind/index.php'
get_param02 = {
    "m":"u",
    "c":"register",
    "a":"dorun"
}

post_data = {
    "username":"sophia03",
    "password":"123456",
    "repassword":"123456",
    "email":"test111@cardinfolink.com",
    "csrf_token":token01
}
rep02 = session.post(url=url02,params= get_param02,data=post_data)
print(rep02.content.decode("utf-8"))
print(rep02.status_code)