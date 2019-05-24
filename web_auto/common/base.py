# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 12:46
# @Author  : 周博远
# @Email   : boyuanky@gmail.com
# @File    : base.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By



class Base():

    def __init__(self, driver:webdriver.Firefox):
        self.driver = driver
        self.timeout = 3
        self.t = 0.5

    def findElementNew(self,locator):
        '''定位到元素，返回元素对象，没定位到，Timeout异常'''
        ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator)(driver))
        return ele

    def findElement(self, locator):
        '''定位元素'''
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        else:
            print(f"正在定位元素信息：定位方式->%s, value值->%s"%(locator[0], locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
            return ele


    def findElements(self, locator):
        '''定位一组元素'''
        try:
            eles = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_elements(*locator))
            return eles
        except:
            return []



    def clear(self, locator):
        '''清空输入框'''
        ele = self.findElement(locator)
        ele.clear()


    def sendkeys(self, locator, text, is_clear_first=False):
        '''输入内容'''
        ele = self.findElement(locator)
        if is_clear_first:
            ele.clear()
        ele.send_keys(text)

    def click(self, locator):
        '''点击按钮'''
        ele = self.findElement(locator)
        ele.click()

    def isSelected(self, locator):
        '''判断元素是否被选中，返回bool值'''
        ele = self.findElement(locator)
        r = ele.is_selected()
        return r

    def isElementExist(self,locator):
        '''判断元素是否存在'''
        try:
            ele = self.findElement(locator)
            return True
        except:
            return False


    def isElementExist2(self,locator):
        '''判断一组元素是否存在'''
        eles = self.findElements(locator)
        n = len(eles)
        if n == 0:
            return False
        elif n==1:
            return True
        else:
            print("定位到元素的个数：%s"%n)
            return True


    def is_title(self,locator,_title=""):
        '''返回bool值,判断title文本'''
        if not isinstance(locator,tuple):
            print("locator参数类型错误，必须传元组类型：loc= ('id', 'value1')")
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(_title))
            return result
        except:
            return False

    def is_title_contains(self,locator,_title):
        '''返回bool值，判断本文是否有这些元素'''
        if not isinstance(locator,tuple):
            print("locator参数类型错误，必须传元组类型：loc= ('id', 'value1')")

        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
            return result
        except:
            return False

    def is_text_in_element(self,locator,_text):
        '''判断文本是否在元素里'''
        '''返回bool值'''
        if not isinstance(locator,tuple):
            print("locator参数类型错误，必须传元组类型：loc= ('id', 'value1')")
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator,_text))
            return result
        except:
            return False


    def is_value_in_element(self,locator,_value):
        if not isinstance(locator,tuple):
            print("locator参数类型错误，必须传元组类型：loc= ('id', 'value1')")
        '''返回bool值, value为空字符串，返回False'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element_value(locator,_value))
            return result
        except:
            return False

    def is_alert(self):
        '''判断alert在不在当前页面'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def get_title(self):
        '''获取title'''
        return self.driver.title

    def get_text(self, locator):
        '''获取文本'''
        try:
            t = self.findElement(locator).text
            return t
        except:
            print("获取text失败，返回'' ")
            return ""

    def get_attribute(self, locator, name):
        '''获取属性'''
        try:
            element = self.findElement(locator)
            return element.get_attribute(name)
        except:
            print("获取%s属性失败，返回'' "%name)
            return ""


    def js_focus_element(self, locator):
        '''聚焦元素'''
        target = self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        '''滚到顶部'''
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self,x=0):
        '''滚到底部'''
        js = "window.scrollTo(%s,document.body.scrollHeight)"%x
        self.driver.execute_script(js)

    def select_by_index(self, locator, index=0):
        '''通过索引,index是索引第几个，从0开始，默认选第一个'''
        element = self.find(locator)  # 定位select这一栏
        Select(element).select_by_index(index)

    def select_by_value(self, locator, value):
        '''通过value属性'''
        element = self.find(locator)
        Select(element).select_by_value(value)

    def select_by_text(self, locator, text):
        '''通过文本值定位'''
        element = self.find(locator)
        Select(element).select_by_visible_text(text)

    def switch_iframe(self, id_index_locator):
        '''切换iframe'''
        try:
            if isinstance(id_index_locator, int):
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, str):
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, tuple):
                ele = self.findElement(id_index_locator)
                self.driver.switch_to.frame(ele)
        except:
            print("iframe切换异常")

    def switch_handle(self, window_name):
        self.driver.switch_to.window(window_name)

    def switch_alert(self):
        r = self.is_alert()
        if not r:
            print("alert不存在")
        else:
            return r


    def move_to_element(self, locator):
        '''鼠标悬停操作'''
        ele = self.findElement(locator)
        ActionChains(driver).move_to_element(ele).perform()


if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html")

    zentao =Base(driver)
    '''
        ID = "id"
        XPATH = "xpath"
        LINK_TEXT = "link text"
        PARTIAL_LINK_TEXT = "partial link text"
        NAME = "name"
        TAG_NAME = "tag name"
        CLASS_NAME = "class name"
        CSS_SELECTOR = "css selector"
    '''


    # loc1 = (By.ID, "account")
    # loc2 = (By.NAME, "password")
    # loc3 = (By.ID, "submit")
    loc1 = ("id", "account")
    loc2 = ("name", "password")
    loc3 = ("id", "submit")

    zentao.sendkeys(loc1, "admin")
    zentao.sendkeys(loc2, "123456")
    zentao.click(loc3)
    # zentao.findElement(loc1).send_keys("admin")
    # zentao.findElement(loc2).send_keys("123456")
    # zentao.findElement(loc3).click()