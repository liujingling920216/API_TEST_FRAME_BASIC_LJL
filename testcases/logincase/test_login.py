import requests
import re
import unittest
import warnings
from common.configutils import config_utils
from common.logutils import logger

class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        warnings.simplefilter('ignore',ResourceWarning)
        self.session = requests.session()
        url01 =config_utils.URL + '/phpwind/'
        res01 = self.session.get(url=url01)
        rep01 = res01.content.decode('utf-8')
        self.token = re.findall('" name="csrf_token" value="(.+?)"/', rep01)[0]
        # 登录
        self.headers_info = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }
        self.get_param = {
            "m": "u",
            "c": "login",
            "a": "dorun"}
        self.url02 = config_utils.URL+"/phpwind/index.php"

    def tearDown(self) -> None:
        pass

    def test_login_pass_01(self):
        logger.info("执行第一个案例：正常用户名密码登录")
        post_data = {
            "username": "sophia.liu",
            "password": "123456",
            "backurl": "",
            "invite	": "",
            "csrf_token": self.token}
        req01 = self.session.post(url = self.url02,
                                  params = self.get_param,
                                  data= post_data,
                                  headers = self.headers_info
        )
        # rep01 = req01.content.decode("utf-8")
        self.assertEqual(req01.json()['state'],"success")

    def test_login_fail_wrong_u_02(self):
        logger.info("执行第二个案例：错误的用户名登录")
        post_data = {
            "username": "sophia",
            "password": "123456",
            "backurl": "",
            "invite	": "",
            "csrf_token": self.token}
        req02 = self.session.post(url = self.url02,
                                  params = self.get_param,
                                  data= post_data,
                                  headers = self.headers_info
        )
        # rep02 = req02.content.decode("utf-8")
        # print(rep02)
        self.assertEqual(req02.json()['state'],"fail")

    def test_login_fail_wrong_p_03(self):
        logger.info("执行第三个案例：错误的密码登录")
        post_data = {
            "username": "sophia",
            "password": "123456",
            "backurl": "",
            "invite	": "",
            "csrf_token": self.token}
        req03 = self.session.post(url = self.url02,
                                  params = self.get_param,
                                  data= post_data,
                                  headers = self.headers_info
        )
        # rep03 = req03.content.decode("utf-8")
        # print(rep03)
        self.assertEqual(req03.json()['state'],"fail")


if __name__ == '__main__':
    unittest.main()