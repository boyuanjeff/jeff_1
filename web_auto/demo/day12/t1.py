# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 8:30
# @Author  : 周博远
# @Email   : boyuanky@gmail.com
# @File    : t1.py
# @Software: PyCharm
'''
    is_displayed()---判断元素是否显示

'''

from common.base import Base
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html")
zentao = Base(driver)
loc1 = ("id", "account")
loc2 = ("name", "password")
loc3 = ("id", "submit")

el1 = zentao.findElement(loc1)

#判断元素
r1 = el1.is_displayed()
print(r1) # True 显示的


loc4 = ("id","hiddenwin")
el2 = zentao.findElement(loc4)
r2 = el2.is_displayed()
print(r2) # False 隐藏的

loc5 = ("id","hiddenwin1")
el3 = zentao.findElement(loc5)
r3 = el3.is_displayed()
print(r3) # 报错selenium.common.exceptions.TimeoutException: Message元素不存在