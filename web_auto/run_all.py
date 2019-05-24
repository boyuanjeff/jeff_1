# -*- coding: utf-8 -*-
# @Time    : 2019/4/29 13:12
# @Author  : 周博远
# @Email   : boyuanky@gmail.com
# @File    : run_all.py
# @Software: PyCharm

import unittest
from common import HTMLTestRunner_cn

casePath = "E:\\web_auto\\case"#用例路径
rule = "test*.py"#匹配规则

discover = unittest.defaultTestLoader.discover(start_dir=casePath, pattern=rule)
print(discover)

reportPath = "E:\\web_auto\\report\\"+"report.html"
fp = open(reportPath, "wb")
runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                       title=u'测试报告',
                                       description=u'用例执行情况：',
                                       retry=1)#失败重跑一次
runner.run(discover)
fp.close()
