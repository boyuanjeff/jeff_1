# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 10:42
# @Author  : 周博远
# @Email   : boyuanky@gmail.com
# @File    : test_login_01.py
# @Software: PyCharm

import unittest
from selenium import webdriver
from demo.day9.loginfunc import login

class LoginCase(unittest.TestCase):

    '''
    对应课9登录函数
    '''

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()

    def test_login_1(self):
        login(self.driver,"admin","123456")
        #self.driver.find_element_by_xpath()