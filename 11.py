import re
import requests

session = requests.session()

# 授权页面
url01 = 'http://47.107.178.45' + '/phpwind/'
res01 = session.get(url=url01)
rep01 = res01.content.decode('utf-8')
token = re.findall('" name="csrf_token" value="(.+?)"/', rep01)[0]
print(token)

# 注册
url02 = 'http://47.107.178.45/phpwind/index.php'
get_params={}

post_data = {
    "username":"sophia02",
    "password":"123456",
    "repassword":"123456",
    "email":"test111@cardinfolink.com",
    "csrf_token":token
}
rep02 = session.post(url=url02,data=post_data,params= )
print(rep02.content.decode("utf-8"))
print(rep02.status_code)