# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 10:30
# @Author  : 周博远
# @Email   : boyuanky@gmail.com
# @File    : loginfunc.py
# @Software: PyCharm

import time

def login(driver, user, psw):
    '''
    对应课9登录函数
    '''
    driver.get("http://127.0.0.1:81/zentao/user-login.html")
    time.sleep(2)
    driver.find_element_by_id("account").send_keys(user)
    driver.find_element_by_name("password").send_keys(psw)
    driver.find_element_by_id("submit").click()








