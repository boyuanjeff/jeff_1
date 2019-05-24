# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 9:05
# @Author  : 周博远
# @Email   : boyuanky@gmail.com
# @File    : login_page.py
# @Software: PyCharm

from selenium import webdriver
from common.base import Base
import time

login_url = "http://127.0.0.1:81/zentao/user-login-L3plbnRhby9idWctYnJvd3NlLTEuaHRtbA==.html"

class LoginPage(Base):
    #定位登录
    loc_user = ("id", "account")
    loc_psw = ("name", "password")
    loc_button = ("xpath", ".//*[@id='submit']")
    loc_keep_login_on = ("id", "keepLoginon")
    loc_forget_psw = ("link text", "忘记密码")

    loc_get_user = ("css selector", "#userMenu>a")

    loc_forget_psw_page = ("xpath", "html/body/div[1]/div/div[2]/p/a")


    def input_user(self, text=""):
        self.sendkeys(self.loc_user, text)

    def input_psw(self, text=""):
        self.sendkeys(self.loc_psw, text)

    def click_login_button(self):
        self.click(self.loc_button)

    def click_keep_login(self):
        self.click(self.loc_keep_login_on)

    def click_forget_psw(self):
        self.click(self.loc_forget_psw)



    def get_login_name(self):
        #  判断是否登录成功
        user = self.get_text(self.loc_get_user)
        return user

    def get_login_result(self, user):
        # 登录结果
        result = self.is_text_in_element(self.loc_get_user, user)
        return result


    def is_alert_exist(self):
        #判断alert是否存在
        a = self.is_alert()
        if a:
            print(a.text)
            a.accept()

    def login(self, user="admin", psw="123456", keep_login=False):
        '''定位登录'''
        self.driver.get(login_url)
        self.input_user(user)
        self.input_psw(psw)
        if keep_login:self.click_keep_login()
        self.click_login_button()






    def is_refresh_exist(self):
        '''判断忘记密码页，刷新按钮是否存在'''
        r = self.isElementExist(self.loc_forget_psw_page)
        return r



if __name__ =="__main__":
    driver = webdriver.Firefox()
    login_page = LoginPage(driver)
    login_page.login(keep_login=True)