# -*- coding: utf-8 -*-
# @Time    : 2019/5/24 8:42
# @Author  : 周博远
# @Email   : boyuanky@gmail.com
# @File    : t_richtext.py
# @Software: PyCharm

from selenium import webdriver
from pages.login_page import LoginPage
import time


driver = webdriver.Firefox()
a = LoginPage(driver)
a.login()


# 打开编辑页面

driver.get("http://127.0.0.1:81/zentao/bug-create-1-0-moduleID=0.html")
# js操作太快，需要先sleep
time.sleep(3)
body = "hello,word"
js = 'document.getElementsByClassName("ke-edit-iframe")[0].contentWindow.document.body.innerHTML=("%s")'%body
driver.execute_script(js)