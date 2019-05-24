# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 13:06
# @Author  : 周博远
# @Email   : boyuanky@gmail.com
# @File    : login_zentao.py
# @Software: PyCharm

import time


class LoginZentao():

    def __init__(self, driver):
        self.driver = driver


    def login(self, user="admin", psw="123456"):
        '''
        对应课9登录函数
        '''
        self.driver.get("http://127.0.0.1:81/zentao/user-login.html")
        time.sleep(2)
        self.driver.find_element_by_id("account").send_keys(user)
        self.driver.find_element_by_name("password").send_keys(psw)
        self.driver.find_element_by_id("submit").click()

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



if __name__ =="__main__":
    from selenium import webdriver
    driver = webdriver.Firefox()
    zentao = LoginZentao(driver)
    zentao.login()