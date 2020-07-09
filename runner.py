import os
import time
import unittest
from common import HTMLTestReportCN
from common.configutils import config_utils

# 获取所有的测试案例
def get_all_testcases_suite():
    discover = unittest.defaultTestLoader.discover(
        start_dir='.\\testcases',
        pattern='test*.py',
        top_level_dir='.\\testcases'
    )
    testsuite = unittest.TestSuite()
    testsuite.addTests(discover)
    return testsuite

# 生成报告
now = time.strftime(u'%Y-%m-%d-%H-%M-%S')
report_file = os.path.join(config_utils.REPORTS , now + "_test_report.html")

with open(report_file, 'wb') as report:
    runner = HTMLTestReportCN.HTMLTestRunner(stream=report,
                                             title=u'线性框架测试报告',
                                             description=u'论坛测试',
                                             )
    runner.run(get_all_testcases_suite())



