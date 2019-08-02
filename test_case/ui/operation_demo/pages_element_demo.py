#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'xuepl'
__mtime__ = '2019/7/30'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from config.conf import DRIVER_PATH

driver = webdriver.Chrome(DRIVER_PATH)
driver.maximize_window()
def get_url():
    url = driver.get("C:/Users/Administrator/Desktop/demo.html")
def text_demo():
    text = driver.find_element_by_xpath('//input[@type="text"]')
    text.clear()
    text.send_keys("我是谁？我在哪儿？我要干嘛？")
    print(text.get_attribute('value'))
def file_demo():
    file = driver.find_element_by_xpath('//input[@type="file"]')
    file.clear()
    file.send_keys('C:\\Users\\Administrator\\Desktop\\1564470399(1).jpg')
    print(file.get_attribute('value'))

def radio_demo():
    radio = driver.find_element_by_xpath('//input[@type="radio"][1]')
    radio.click()
def checkbox_demo():
    checkbox = driver.find_element_by_xpath('//input[@type="checkbox"][1]')
    checkbox.click()
    checkbox1 = driver.find_element_by_xpath('//input[@type="checkbox"][3]')
    checkbox1.click()
def button_demo():
    button = driver.find_element_by_xpath('//input[@type="button"]')
    button.click()
def password_demo():
    password = driver.find_element_by_xpath('//input[@type="password"]')
    password.clear()
    password.send_keys("木有密码")
    print(password.get_attribute('value'))
def number_demo():
    number = driver.find_element_by_xpath('//input[@type="number"]')
    number.clear()
    number.send_keys("583735876")
    print(number.get_attribute('value'))
#date:日期控件
def data_demo():
    js = '''var xpath = '//input[@type="date"]';var element = document.evaluate(xpath,document,null,XPathResult.ANY_TYPE,null).iterateNext();element.setAttribute("value","2019-07-30");'''
    driver.execute_script(js)
#time:时间控件
def time_demo():
    time = driver.find_element_by_xpath('//input[@type="time"]')
    time.clear()
    time.send_keys("17：20")
    sleep(2)


def textarea_demo():
    textarea = driver.find_element_by_xpath('//textarea')
    textarea.clear()
    textarea.send_keys("583735876")
    print(textarea.get_attribute('value'))
    sleep(2)

def select_demo():
    select=driver.find_element_by_xpath('//option[2]')
    select.click()
    sleep(2)
def a_demo():
    # a = driver.find_element_by_xpath('//a[@href="http://www.dangdang.com/"]')
    # a.click()
    # sleep(5)
    baidu = driver.find_element_by_partial_link_text("度娘")
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).click(baidu).key_up(Keys.CONTROL).perform()
    sleep(2)

if __name__ == '__main__':
    get_url()
    # sleep(2)
    # text_demo()
    # sleep(2)
    # file_demo()
    # sleep(2)
    # radio_demo()
    # sleep(2)
    # checkbox_demo()
    # sleep(2)
    # # button_demo()
    # # sleep(1)
    # password_demo()
    # sleep(2)
    # number_demo()
    # sleep(2)
    # data_demo()
    # sleep(2)
    time_demo()
    textarea_demo()
    select_demo()
    a_demo()

    driver.quit()

