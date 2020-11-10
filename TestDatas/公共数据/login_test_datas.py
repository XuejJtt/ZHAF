#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 11:09
# @Author  : Xuej
# @File    : login_test_datas.py
# @Software: PyCharm


#正常的测试用例

success_data ={'name':'登录功能_正常测试', 'username':'19900000001' ,'pwd':'123qwe','dec':'登录功能正常测试'}


#异常的测试用例

error_data =[{'name':'登录功能_异常测试_用户名为空','username':'','pwd':'1234','dec':'用户名为空的测试','errormsg':'请输入用户名'},
             {'name':'登录功能_异常测试_密码为空','username':'securityAdmin','pwd':'','dec':'密码为空的测试','errormsg':'请输入密码'},
             {'name':'登录功能_异常测试_用户名错误','username':'security' ,'pwd':'123','dec':'错误的用户名测试','errormsg':'用户名或者密码错误'},
             {'name':'登录功能_异常测试_密码错误','username':'securityAdmin' ,'pwd':'123','dec':'错误的密码测试','errormsg':'用户名或者密码错误'}]
