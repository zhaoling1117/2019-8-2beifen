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

import allure
from tools import assert_tool

@allure.feature("添加商品分类流程")
@allure.story("")
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
    page_source = base.driver.page_source

    with allure.step('登录界面跳转断言'):
        allure.attach(page_source,"实际结果",allure.attachment_type.TEXT)
        allure.attach("首页", "预期结果", allure.attachment_type.TEXT)
        assert_tool.assert_in(page_source, '首页')
# 点击商品 (//span[contains(text(),'商品')])[1]
    base.click("点击商品",'''(//span[contains(text(),'商品')])[1]''')
    # 点击添加商品 //span[contains(text(),'添加商品')]
    base.click("点击添加商品",'''//span[contains(text(),'添加商品')]''')
    # 点击商品分类 //label[contains(text(),'商品分类')]/../div//input
    base.click("点击商品分类","""//label[contains(text(),'商品分类')]/../div//input""")
    # 点击下拉框第一个选项 //ul[@role='menu' and contains(@id,'cascader-menu')]/li[1]
    base.click("点击下拉框第一个选项","//ul[@role='menu' and contains(@id,'cascader-menu')]/li[1]")
    # 点击二级下拉菜单第一个选项  //li[@role='menuitem' and contains(@id,'menu-')][1]
    base.click("点击二级下拉菜单第一个选项",'''//li[@role='menuitem' and contains(@id,'menu-')][1]''')
    # 填写商品名称 //label[contains(text(),'商品名称')]/../div//input
    base.send_keys("填写商品名称","//label[contains(text(),'商品名称')]/../div//input","小米11")
    # 填写副标题 //label[contains(text(),'副标题')]/../div//input
    base.send_keys("填写副标题",'''//label[contains(text(),'副标题')]/../div//input''','手机')
    # 点击商品品牌 //label[contains(text(),'商品品牌')]/../div//input
    base.click("点击商品品牌","""//label[contains(text(),'商品品牌')]/../div//input""")
    # 点击下拉菜单中第一个选项 (//ul[@class="el-scrollbar__view el-select-dropdown__list"])[2]/li[1]
    base.click("点击下拉菜单中第一个选项","""(//ul[@class="el-scrollbar__view el-select-dropdown__list"])[2]/li[1]""")
    # 滚动窗口
    base.scroll_screen("滚动窗口")
    #点击下一步，填写商品促销 //span[text()='下一步，填写商品促销']
    base.click("点击下一步，填写商品促销",'''//span[text()='下一步，填写商品促销']''')
    #滚动窗口
    base.scroll_screen("滚动窗口")
    #点击下一步，填写商品属性//span[text()='下一步，填写商品属性']
    base.click("点击下一步，填写商品属性", '''//span[text()='下一步，填写商品属性']''')
    #滚动窗口
    base.scroll_screen("滚动窗口")
    # # #切换窗口至iframe
    # # base.switch_to_frame("切换窗口至iframe ",'(//iframe)[1]')
    #
    # #输入电脑端详情   //body/p
    # base.send_keys("#输入电脑端详情 ","//body",'测试数据')
    # #切出iframe
    # base.switch_to_content("切出iframe")
    #
    # # 点击下一步，选择商品关联
    base.click("点击下一步，选择商品关联", '''//span[text()='下一步，选择商品关联']''')
    base.click("点击完成，提交商品",'''//span[text()='完成，提交商品']''')
    base.click("点击确定",'''//span[contains(text(),'确定')]''')

    # print(base.page_source())
    sleep(5)


    pass