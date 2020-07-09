import os
import re
from collections import OrderedDict

from common.configutils import config_utils

def get_main_page_token(session):
    url01 = config_utils.URL + '/phpwind/'
    res01 = session.get(url=url01)
    rep01 = res01.content.decode('utf-8')
    token = re.findall('" name="csrf_token" value="(.+?)"/', rep01)[0]
    return token

def login(session,usr,pwd,token):
    # token = get_main_page_token(session)
    headers_info = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    get_param = {
        "m": "u",
        "c": "login",
        "a": "dorun"}
    post_data = {
        "username": usr,
        "password": pwd,
        "backurl": "",
        "invite	": "",
        "csrf_token": token
    }
    req02 = session.post(url=config_utils.URL + "/phpwind/index.php",
                         params=get_param,
                         data=post_data,
                         headers=headers_info
                              )
    return req02

def get_login_token_id(session):
    req03 = login(session, "sophia.liu", "123456",token = get_main_page_token(session))
    rep03 = req03.content.decode("utf-8")
    login_id = re.findall('&_statu=(.+?)","refresh"',rep03)[0]
    return login_id

# 登录后进行授权操作
def login_auth(session):
    login_id = get_login_token_id(session)
    get_params = {
        "m": "u",
        "c": "login",
        "a": "welcome",
        "_statu": login_id
    }
    res04 = session.get(url=config_utils.URL + '/phpwind/index.php',
                        params=get_params
                        )

def post(session,title,content,token):
    # token = get_main_page_token(session)
    get_params = {
        "c": "post",
        "a": "doadd",
        "_json": 1,
        "fid": 80
    }
    headers_info = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        # "Content-Type":"multipart/form-data; boundary=----WebKitFormBoundaryAS42cPv6bKiOKp1e",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    mul_form_data = OrderedDict(
        [
            ("atc_title", (None, title)),
            ("atc_content", (None, content)),
            ('pid', (None, '')),
            ('tid', (None, '')),
            ('special', (None, 'default')),
            ('reply_notice', (None, '1')),
            ('csrf_token', (None,token))
        ]
    )
    res05 = session.post( url = config_utils.URL + '/phpwind/index.php',
                      headers = headers_info,
                      params = get_params,
                      files = mul_form_data
                      )
    return res05