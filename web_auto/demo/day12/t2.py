# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 9:01
# @Author  : 周博远
# @Email   : boyuanky@gmail.com
# @File    : t2.py
# @Software: PyCharm
'''
    .is_selected（）
    判断是否被select，返回True和False
    【注意是针对于select下拉框情况】
'''
from common.base import Base
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select



driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
zentao = Base(driver)

loc1 = ("link text", "设置")
mouse = zentao.findElement(loc1)
ActionChains(driver).move_to_element(mouse).perform()

loc2 = ("link text", "搜索设置")
mouse1 = zentao.click(loc2)


loc3 = ("xpath", ".//*[@id='nr']/option[3]")
r1 = zentao.findElement(loc3).is_selected()
print(r1)  #False 没有被选中


#鼠标选择角标为2的选项
loc4 = ("id", "nr")
select = zentao.findElement(loc4)
Select(select).select_by_index(2)


r2= zentao.findElement(loc3).is_selected()
print(r2)  #True 被选中
