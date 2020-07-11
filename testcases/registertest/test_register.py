import requests
import unittest
import warnings
from common.common_api import *
from common.logutils import logger

class Register(unittest.TestCase):
    def setUp(self) -> None:
        warnings.simplefilter('ignore',ResourceWarning)
        self.session = requests.session()
        self.token01 = register_auth(self.session)
    def tearDown(self) -> None:
        pass

    def test_register_success_01(self):
        logger.info("执行注册模块第一个案例：注册信息正确，注册成功")
        res = resister(self.session, config_utils.REGISTER_NAME, '123456', '123456', config_utils.REGISTER_EMAIL,self.token01)
        rep = res.content.decode('utf-8')
        # print(rep)
        self.assertIn('，恭喜您注册成为phpwind 9.0会员！',rep)

    def test_regester_fail_usr_none_02(self):
        logger.info("执行注册模块第二个案例：注册用户名是空，注册失败")
        res = resister(self.session, None, '123456', '123456', config_utils.REGISTER_EMAIL,self.token01)
        rep = res.content.decode('utf-8')
        # print(rep)
        self.assertIn('错误提示 - phpwind 9.0 - Powered by phpwind',rep)

    def test_regester_fail_token_wrong_03(self):
        logger.info("执行注册模块第三个案例：注册token错误，注册失败")
        res = resister(self.session, config_utils.REGISTER_NAME, '123456', '123456', config_utils.REGISTER_EMAIL, '1111')
        rep = res.content.decode('utf-8')
        # print(rep)
        self.assertIn('错误提示 - phpwind 9.0 - Powered by phpwind', rep)




if __name__ == '__main__':
    unittest.main()
