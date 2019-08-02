#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'xuepl'
__mtime__ = '2019/7/31'
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

def open_a():
    baidu = driver.find_element_by_partial_link_text("度娘")
    dd = driver.find_element_by_partial_link_text("当当")
    jd = driver.find_element_by_partial_link_text("京东")
    action=action = ActionChains(driver)
    action.key_down(Keys.CONTROL).click(baidu).click(dd).click(jd).key_up(Keys.CONTROL).perform()

def windows_change_ddemo():
    handles=driver.window_handles
    for h in handles:
        driver.switch_to.window(h)
        sleep(2)
        if(driver.title.__contains__('百度')):
            break
def open_alert():
    driver.find_element_by_xpath('//input[@type="reset"]').click()
    sleep(2)
def alert_alert_open():
    a=driver.switch_to.alert
    #确认
    a.accept()
    sleep(2)
def open_button():
    driver.find_element_by_xpath('//input[@type="button"]').click()
    sleep(2)




if __name__ == '__main__':
    get_url()
    sleep(2)
    open_a()
    sleep(3)
    windows_change_ddemo()
    open_alert()
    alert_alert_open()

    driver.quit()
