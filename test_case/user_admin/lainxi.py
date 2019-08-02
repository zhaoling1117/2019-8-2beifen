#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'zhaoling'
__mtime__ = '2019/7/24'
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
# import requests
#1、发送json请求
# data = {
#   "password": "123456",
#   "username": "admin"
# }
# r = requests.post('http://qa.yansl.com:8080/admin/login',json=data)
# print(r.text)


#2、发送post请求，键值对请求
import requests

# pa = {"adminId":20,"roleIds":1}
# q = requests.post('http://qa.yansl.com:8080/admin/role/update',data=pa)
# print(q.text)

#3、发送get请求串数据，params
pa = {"name":"admin","pageSize":5,"pageNum":1}
re = requests.get('http://qa.yansl.com:8080/admin/list',params=pa)
print(re.text)
