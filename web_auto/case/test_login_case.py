# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 9:52
# @Author  : 周博远
# @Email   : boyuanky@gmail.com
# @File    : test_login_case.py
# @Software: PyCharm
from selenium import webdriver
import unittest
from pages.login_page import LoginPage,login_url

'''
1.输入账号admin，输入密码123456，点登录
2.输入账号admin  点登录
3.输入账号admin 输入密码123456 点记住登录按钮 点登录
4.点忘记密码
'''

class LoginPageCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox()
        cls.loginp = LoginPage(cls.driver)

    def setUp(self) -> None:
        self.driver.get(login_url)
        self.loginp.is_alert_exist()
        self.driver.delete_all_cookies()
        self.driver.refresh()



    def test_01(self):
        #1.输入账号admin，输入密码123456，点登录
        self.loginp.input_user("admin")
        self.loginp.input_psw("123456")
        self.loginp.click_login_button()
        result = self.loginp.get_login_name()
        self.assertTrue(result=="admin")

    def test_02(self):
        #2.输入账号admin  点登录
        self.loginp.input_user("admin")
        self.loginp.click_login_button()
        result = self.loginp.get_login_name()
        self.assertTrue(result == "")

    def test_03(self):
        #3.输入账号admin 输入密码123456 点记住登录按钮 点登录
        self.loginp.input_user("admin")
        self.loginp.input_psw("123456")
        self.loginp.click_keep_login()
        self.loginp.click_login_button()
        result = self.loginp.get_login_name()
        self.assertTrue(result == "admin")

    def test_04(self):
        #4.点忘记密码
        self.loginp.click_forget_psw()
        result = self.loginp.is_refresh_exist()
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
