# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 15:53
# @Author  : 周博远
# @Email   : boyuanky@gmail.com
# @File    : test_add_bug.py
# @Software: PyCharm

import unittest
from selenium import webdriver
from pages.add_bug import ZentaoBug
import time


class Test_Add_Bug(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.bug = ZentaoBug(cls.driver)
        cls.bug.login()

    def test_add_bug(self):
        timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
        title = "测试提交BUG" + timestr
        self.bug.add_bug(title)
        result = self.bug.is_add_bug_success(title)
        print(result)
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()

