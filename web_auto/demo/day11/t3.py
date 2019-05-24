# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 12:13
# @Author  : 周博远
# @Email   : boyuanky@gmail.com
# @File    : t3.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html")

driver.find_element(By.ID, "account")
driver.find_element(By.NAME, "password")
driver.find_element(By.ID, "submit")

def findElement(driver, locator,timeout=30, t = 0.5 ):
    ele = WebDriverWait(driver, 10, 1).until(lambda x: x.find_element(*locator))
    return ele

loc1 = (By.ID, "account")
loc2 = (By.NAME, "password")
loc3 = (By.ID, "submit")




findElement(driver, loc1).send_keys("admin")
findElement(driver, loc2).send_keys("123456")
findElement(driver, loc3).click()



# # 等待时长10秒，默认0.5秒询问一次
# ele1 = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("account"))
#
# print(ele1)
# ele1.send_keys("admin")
#
# ele2 = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_name("password"))
# ele2.send_keys("123456")
#
# ele3 = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("submit"))
# ele3.click()