# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 15:55
# @Author  : 周博远
# @Email   : boyuanky@gmail.com
# @File    : add_bug.py
# @Software: PyCharm

from selenium import webdriver
from common.base import Base
import time


class AddBugPage(Base):

    #添加bug
    loc_test = ("link text", "测试")
    loc_bug = ("link text", "Bug")
    loc_addbug = ("xpath",".//*[@id='createActionMenu']/a")
    loc_truck = ("xpath",".//*[@id='openedBuild_chosen']/ul")
    loc_truck_add = ("xpath",".//*[@id='openedBuild_chosen']/div/ul/li")
    loc_input_title = ("id","title")
    #需要先切换iframe
    loc_input_body = ("class name","article-content")
    loc_avse = ("id","submit")

    #新增的列表
    loc_new = ("xpath", ".//*[@id='bugList']/tbody/tr[1]/td[4]/a")

    def add_bug(self, title="测试提交BUG"):
        self.click(self.loc_test)
        self.click(self.loc_bug)
        self.click(self.loc_addbug)
        self.click(self.loc_truck)
        self.click(self.loc_truck_add)

        self.sendkeys(self.loc_input_title, title)
        #输入body
        frame = self.findElement(("class name", "ke-edit-iframe"))
        self.driver.switch_to.frame(frame)
        #富文本不能clear
        body = '''[测试步骤]XXX
        [结果]xxx
        [期望结果]xxx
        '''
        self.sendkeys(self.loc_input_body, body)
        self.driver.switch_to.default_content()
        #保存提交
        self.click(self.loc_avse)

    def is_add_bug_success(self, _text):
        return self.is_text_in_element(self.loc_new,_text)


if __name__ =="__main__":
    driver = webdriver.Firefox()
    bug = AddBugPage(driver)

    from pages.login_page import LoginPage
    a = LoginPage(driver)
    a.login()

    timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
    title = "测试提交BUG"+timestr
    bug.add_bug(title)
    result = bug.is_add_bug_success(title)
    print(result)