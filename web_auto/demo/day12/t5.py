# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 10:04
# @Author  : 周博远
# @Email   : boyuanky@gmail.com
# @File    : t5.py
# @Software: PyCharm
from common.base import Base
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time

'''
    checkbox
'''

driver = webdriver.Firefox()
driver.get("https://login.sina.com.cn/signup/signup?entry=homepage")
xinlang = Base(driver)

loc1 = ("xpath", ".//*[@id='phone-form']/div[4]/div[2]/label[1]")
box1 = xinlang.isSelected(loc1)
print(box1)

#点击
che1 = xinlang.click(loc1)
#time.sleep(3)
loc2 = ("xpath", ".//*[@id='phone-form']/div[4]/div[2]/label[1]")
box2 = xinlang.isSelected(loc2)
print(box2)


#全部选中
loc_all = ("xpath", ".//*[@id='phone-form']/div[4]/div[2]")
all = xinlang.findElements(loc_all)

print(all)

def result():
    r = []#判断全部被选中

    for i in all:
        if not i.is_selected():
            i.click()
            r.append(i.is_selected)#判断结果
        else:
            r.append(i.is_selected)

    return r
rrrr =result(all)
print(rrrr)

for i in rrrr:
    assert i ==True