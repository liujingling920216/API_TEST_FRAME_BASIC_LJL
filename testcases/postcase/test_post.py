import time

import requests
import unittest
import warnings
from common.logutils import logger
from common.common_api import *

class TestPost(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()
        self.token = get_main_page_token(self.session)
        self.token_id = get_login_token_id(self.session)

    def tearDown(self) -> None:
        pass

    def test_post_sucess_01(self):
        logger.info("执行发帖模块第一个案例：登录授权后进行发贴")
        login_auth(self.session)
        post_req01= post(self.session,
                       title = "ljl0709发帖"+ time.strftime('%Y-%m-%d-%H-%M-%S'),
                       content = "ljl0709发帖"+time.strftime('%Y-%m-%d-%H-%M-%S'),
                       token = self.token)
        post_rep01 = post_req01.content.decode('utf-8')
        # print(post_rep01)
        self.assertEqual(post_req01.json()['state'], "success")

    def test_post_no_auth_fail_02(self):
        logger.info("执行发帖模块第二个案例：登录后不进行授权进行发贴")
        # login_auth(self.session)
        post_req02= post(self.session,
                       title = "ljl0709发帖"+ time.strftime('%Y-%m-%d-%H-%M-%S'),
                       content = "ljl0709发帖"+time.strftime('%Y-%m-%d-%H-%M-%S'),
                       token = self.token)
        post_rep02 = post_req02.content.decode('utf-8')
        # print(post_rep02)
        self.assertEqual(post_req02.json()['state'], "fail")

    def test_post_wrong_token_fail_03(self):
        logger.info("执行发帖模块第三个案例：发贴接口上送错误的token")
        # login_auth(self.session)
        post_req03= post(self.session,
                       title = "ljl0709发帖"+ time.strftime('%Y-%m-%d-%H-%M-%S'),
                       content = "ljl0709发帖"+time.strftime('%Y-%m-%d-%H-%M-%S'),
                       token = "111111")
        post_rep03 = post_req03.content.decode('utf-8')
        # print(post_rep03)
        self.assertEqual(post_req03.json()['state'], "fail")

    def test_post_title_null_fail_04(self):
        logger.info("执行发帖模块第四个案例：发贴接口标题送None")
        # login_auth(self.session)
        post_req04= post(self.session,
                       title = None,
                       content = "ljl0709发帖"+time.strftime('%Y-%m-%d-%H-%M-%S'),
                       token = self.token)
        post_rep04 = post_req04.content.decode('utf-8')
        print(post_rep04)
        self.assertEqual(post_req04.json()['state'], "fail")
