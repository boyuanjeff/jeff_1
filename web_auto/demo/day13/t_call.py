# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 14:16
# @Author  : 周博远
# @Email   : boyuanky@gmail.com
# @File    : t_call.py
# @Software: PyCharm
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
'''
    判断title内容

'''

driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")


r = EC.title_is("百度一下，你就知道")(driver)
print(r)

#assert r
r2 = EC.title_contains("百度一下")(driver)#检错title包含
print(r2)





