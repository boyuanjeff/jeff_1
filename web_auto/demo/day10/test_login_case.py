# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 13:18
# @Author  : 周博远
# @Email   : boyuanky@gmail.com
# @File    : test_login_case.py
# @Software: PyCharm

from selenium import webdriver
import time
import unittest
from demo.day10.login_zentao import LoginZentao


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox()
        cls.zentao = LoginZentao(cls.driver)



    def setUp(self) -> None:
        self.driver.get("http://127.0.0.1:81/zentao/user-login.html")







    def test_01(self):
        '''登录成功的案例'''
        time.sleep(2)
        self.zentao.login("admin","123456")
        #  判断是否登录成功
        time.sleep(3)
        t = self.zentao.get_login_username()
        print("获取的结果： %s" %t)
        self.assertTrue(t == "admin")

    def test_02(self):
        time.sleep(2)
        #  测试错误账号and密码
        self.zentao.login("admin","1234567")
        #  判断是否登录成功
        time.sleep(3)
        t = self.zentao.get_login_username()
        print("登录失败，获取的结果： %s" %t)
        self.assertTrue(t=="")
        #self.assertTrue(1==2)#断言失败截图

    def tearDown(self) -> None:
        self.zentao.is_alert_exist()

        self.driver.delete_all_cookies()  # 清空cookies,退出登录
        self.driver.refresh()      # 刷新页面


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()       # 退出浏览器




if __name__ == "__main__":
    unittest.main()