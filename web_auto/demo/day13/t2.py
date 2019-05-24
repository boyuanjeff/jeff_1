# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 14:35
# @Author  : 周博远
# @Email   : boyuanky@gmail.com
# @File    : t2.py
# @Software: PyCharm

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
'''
    判断title内容

'''

driver = webdriver.Firefox()
driver.get("http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html")

loc1 = ("xpath", "//*[text()='忘记密码']")
r1 = EC.presence_of_element_located(loc1)(driver)
print(r1)#返回WebElement元素对象

