# -*- coding: utf-8 -*-
# @Time    : 2019/5/17 11:21
# @Author  : 周博远
# @Email   : boyuanky@gmail.com
# @File    : t2.py
# @Software: PyCharm

from selenium import webdriver
import time
import unittest


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox()

    def setUp(self) -> None:
        self.driver.get("http://127.0.0.1:81/zentao/user-login.html")


    def get_login_username(self):
        #  判断是否登录成功
        try:
            t = self.driver.find_element_by_xpath(".//*[@id='userMenu']/a").text
            print(t)
            return t
        except:
            return ""

    def is_alert_exist(self):
        #判断alert是否存在
        try:
            time.sleep(2)
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept() # 用alert 点alert
            return text
        except:
            return ""

    def login(self, user, psw):
        self.driver.find_element_by_id("account").send_keys(user)
        self.driver.find_element_by_name("password").send_keys(psw)
        self.driver.find_element_by_id("submit").click()





    def test_01(self):
        '''登录成功的案例'''
        time.sleep(2)
        self.login("admin", "123456")
        #  判断是否登录成功
        time.sleep(3)
        t = self.get_login_username()
        print("获取的结果： %s" %t)
        self.assertTrue(t == "admin")

    def test_02(self):
        time.sleep(2)
        #  测试错误账号and密码
        self.login("admin1", "123456")
        #  判断是否登录成功
        time.sleep(3)
        t = self.get_login_username()
        print("登录失败，获取的结果： %s" %t)
        self.assertTrue(t=="")

    def tearDown(self) -> None:
        self.is_alert_exist()

        self.driver.delete_all_cookies()  # 清空cookies,退出登录
        self.driver.refresh()      # 刷新页面


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()       # 退出浏览器




if __name__ == "__main__":
    unittest.main()