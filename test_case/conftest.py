from selenium import webdriver
from tools import request_tool
from tools import assert_tool
from tools import random_tool
from tools import mysql_tool
from tools import excel_tool
from tools import log_tool
from tools import os_tool
from tools import shell_tool
import pytest
import allure
# 项目根目录建config包，里面建conf.py文件，用于配置
from config import conf


import pytest

from config.conf import DRIVER_PATH
from tool.base_ui import BaseUI


@pytest.fixture(scope='session')
def pub_dic():
    data = {'token':'asdfasdfjsldkfjlsxllkj'}
    return data


@pytest.fixture(scope='session')
def pub_list():
    data = ['张三','zhangsan',30,'男','aaa123']
    return data


@pytest.fixture(scope='session')
def pub_var():
    token = 'xxxxsdfsdfjkllwklewe'
    return token


@pytest.fixture(scope="session")
def token():
    url = conf.GY_API_URL + '/admin/login'
    req = {
        "password": "123456",
        "username": "admin"
    }

    resp = request_tool.post_request(url, json=req)
    body = resp.json()
    # 判断响应码
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    assert_tool.assert_equal(body['data']['tokenHead'], 'Bearer ')
    return body['data']['tokenHead'] + body['data']['token']

#id提取
@pytest.fixture(scope="session")
def id():
    url = conf.GY_API_URL + '/admin/register'
    username = "赵令" + random_tool.random_str_abc(8)
    req = {
        "email": "string",
        "icon": "string",
        "nickName": "string",
        "note": "string",
        "password": "123456",
        "username": username
    }
    resp = request_tool.post_request(url, json=req)
    body = resp.json()
    # 判断响应码
    with allure.step("断言响应状态码，实际结果是：{}，预期结果为：200".format(resp.status_code)):
        pass
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    with allure.step("断言用户名，实际结果是：{}，预期结果为：{}".format(body['data']["username"], username)):
        pass
    assert_tool.assert_equal(body['data']["username"], username)
    return body['data']["id"]


@pytest.fixture(scope="session")
def base():
    #fixture装饰器可以设置前置后置步骤
    #返回值存到了方法名中
    #测试用例中，根据方法名来使用该方法的返回值
    # 打开浏览器
    dr = webdriver.Chrome(DRIVER_PATH)
    dr.maximize_window()  # 最大化浏览器
    dr.implicitly_wait(8)  # 设置隐式时间等待
    # 使用baseUI
    base = BaseUI(dr)
    yield base
    dr.quit()