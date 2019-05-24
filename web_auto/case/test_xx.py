# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 15:18
# @Author  : 周博远
# @Email   : boyuanky@gmail.com
# @File    : test_xx.py
# @Software: PyCharm
from selenium import webdriver
import unittest
from pages.login_page import LoginPage,login_url
import ddt
from common.read_excel import ExcelUtil
import os


'''
1.输入账号admin，输入密码123456，点登录
2.输入账号admin  点登录
3.输入账号admin111 输入密码123456 点记住登录按钮 点登录
'''
# 测试数字
testdates = [{"user": "admin", "psw": "123456", "expect":True},
             {"user": "admin", "psw": "", "expect":False},
             {"user": "admin111", "psw": "123456", "expect":False}, ]


# propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
#
# filepath = os.path.join(propath, "common", "datas.xlsx")
# data = ExcelUtil(filepath)
# testdates = data.dict_data()
# print(testdates)


@ddt.ddt
class LoginPageCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox()
        cls.loginp = LoginPage(cls.driver)
        cls.driver.get(login_url)

    def setUp(self) -> None:
        self.loginp.is_alert_exist()
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.get(login_url)

    def login_case(self, user, psw, expect):
        self.loginp.login(user, psw)
        result = self.loginp.get_login_result(user)

        print("测试结果：%s" % result)
        self.assertTrue(result == expect)

    # ddt.data({"user":"admin","psw":"123456","expect":"admin"},
    #          {"user": "admin", "psw": "", "expect": ""},
    #          {"user": "admin111", "psw": "123456", "expect": ""},)

    @ddt.data(*testdates)
    def test_01(self, data):
        #1.输入账号admin，输入密码123456，点登录
        print("-----开始测试-----")
        print("测试数据 %s" % data)
        self.login_case(data["user"], data["psw"], data["expect"])
        print("-----测试结束：pass！-----")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
