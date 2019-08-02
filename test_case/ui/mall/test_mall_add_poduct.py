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

#打开用户界面
from time import sleep

from tools import assert_tool


def test_login(base):
    base.get("打开登录界面",'http://qa.yansl.com/#/login')
#输入用户名//input[@type="text"]
    base.send_keys("输入用户名",'''//input[@type="text"]''',"admin")
#输入密码//input[@type="password"]
    base.send_keys("输入密码",'''//input[@type="password"]''',"123456")
#点击登录//span[contains(text(),'登录')]
    base.click("点击登录","//span[contains(text(),'登录')]")
#点击残忍拒绝//span[text()='残忍拒绝']
    base.click("点击残忍拒绝","//span[text()='残忍拒绝']")
#点击登录
    base.click("点击登录", "//span[contains(text(),'登录')]")
    sleep(5)
#断言 页面跳转至首页
    page_source = base.driver.page.source
    assert_tool.assert_in(page_source,'首页')
    # 点击商品//span[contains(text(),'商品')][1]
    # 点击添加商品(//span[contains(text(),'添加商品')])[1]
    # 点击商品分类//span[@class="el-cascader__label"]
    # 点击下拉框第一个选项(//ul[@role='menu' and contains(@id,'cascader-menu')]/li)[1]

    # 点击二级下拉菜单第一个选项(//ul[@role="menu"and@id="menu-2863-1"]/li)[1]
    # 填写商品名称(//div[@data-v-51f80952 and @class="el-input el-input--small"])[1]
    # 填写副标题(//div[@data-v-51f80952 and @class="el-input el-input--small"])[2]
    # 点击商品品牌(//div[@class="el-input el-input--small el-input--suffix"])[2]
    # 点击下拉菜单中第一个选项(//ul[@class="el-scrollbar__view el-select-dropdown__list"]/li[@data-v-51f80952])[1]

    # 滚动窗口
    base.scroll_screen("滚动窗口")
    #点击下一步，填写商品促销//span[text()='下一步，填写商品促销']
    #滚动窗口
    base.scroll_screen("滚动窗口")
    #点击下一步，填写商品属性//span[text()='下一步，填写商品促销']
    #滚动窗口base.scroll_screen("滚动窗口")
    base.scroll_screen("滚动窗口")
    # #切换窗口至iframe
    base.switch_to_frame("切换窗口至iframe ", '(//iframe)[1]')

    #输入电脑端详情

    #切出iframe


    # 点击下一步，选择商品关联


