# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 12:55
# @Author  : 周博远
# @Email   : boyuanky@gmail.com
# @File    : add_bug_case.py
# @Software: PyCharm
import unittest
from selenium import webdriver
from pages.add_bug_page import AddBugPage
import time
from pages.login_page import LoginPage



my_url ="http://127.0.0.1:81/zentao/my/"
class AddBugCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox()
        cls.bug = AddBugPage(cls.driver)

        cls.a = LoginPage(cls.driver)
        cls.a.login()

    def setUp(self) -> None:
        self.driver.get(my_url)


    def test_add_bug(self):
        '''添加bug'''
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
