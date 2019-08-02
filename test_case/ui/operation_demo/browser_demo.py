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


#浏览器的基本操作
#1、打开
from time import sleep

from selenium import webdriver

from config.conf import DRIVER_PATH, GY_WEB_URL

driver = webdriver.Chrome(DRIVER_PATH)
#2、调整浏览器窗口大小
#①、最大化(推荐使用)
driver.maximize_window()
# # #②自定义
# # driver.set_window_size(1280,960)
# #③、移动浏览器
# driver.set_window_position()
#3、打开网址
driver.get(GY_WEB_URL)
sleep(2)
driver.get("https://www.baidu.com/")
sleep(3)
driver.get("https://www.runoob.com/")
sleep(4)
driver.get("https://www.tapd.cn")
sleep(5)
driver.get("https://www.jianshu.com/")
sleep(6)
#4、后退
driver.back()
sleep(2)
#5、前进
driver.forward()
sleep(2)
#6、刷新
driver.refresh()
#7、延时
sleep(5)

#8、关闭浏览器
driver.close()

#9、退出驱动
driver.quit()