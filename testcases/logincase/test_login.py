import requests
import unittest
import warnings
from common.logutils import logger
from common.common_api import *

class TestLogin(unittest.TestCase):
    """发帖模块测试用例"""
    def setUp(self) -> None:
        warnings.simplefilter('ignore',ResourceWarning)
        self.session = requests.session()
        self.token = get_main_page_token(self.session)


    def tearDown(self) -> None:
        pass

    def test_login_pass_01(self):
        self._testMethodDoc = '执行登录模块第一个案例：正常用户名密码登录'    # 测试报告中增加测试用例说明信息
        logger.info("执行登录模块第一个案例：正常用户名密码登录")
        req1 = login(self.session,"sophia.liu","123456",self.token)
        rep01 = req1.content.decode("utf-8")
        # print(rep01)
        self.assertEqual(req1.json()['state'],"success")

    def test_login_fail_wrong_usr_02(self):
        self._testMethodDoc = '执行登录模块第二个案例：错误的用户名登录'
        logger.info("执行登录模块第二个案例：错误的用户名登录")
        req2 = login(self.session,"sophia","123456",self.token)
        self.assertEqual(req2.json()['state'],"fail")

    def test_login_fail_wrong_pw_03(self):
        self._testMethodDoc = '执行登录模块第三个案例：错误的密码登录'
        logger.info("执行登录模块第三个案例：错误的密码登录")
        req3 = login(self.session, "sophia.liu", "12345",self.token)
        self.assertEqual(req3.json()['state'],"fail")


if __name__ == '__main__':
    unittest.main()