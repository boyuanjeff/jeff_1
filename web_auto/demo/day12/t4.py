# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 9:41
# @Author  : 周博远
# @Email   : boyuanky@gmail.com
# @File    : t4.py
# @Software: PyCharm
'''
    radio
'''

from common.base import Base
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select



driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
baidu = Base(driver)

loc1 = ("link text", "设置")
mouse = baidu.findElement(loc1)
ActionChains(driver).move_to_element(mouse).perform()

loc2 = ("link text", "搜索设置")
mouse1 = baidu.click(loc2)

loc3 = ("id", "s1_1")
loc4 = ("id", "s1_2")


r1 = baidu.isSelected(loc3)
print(r1)
r2 = baidu.isSelected(loc4)
print(r2)