#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/9 15:51
# @File    : log_manage.py
# @Software: PyCharm


from selenium.webdriver.common.keys import Keys
from Common.BasePage import BasePage
from selenium.webdriver.common.by import By


class log_manage(BasePage):
    head = "ant-table-thead" #头部标题
    body = "ant-table-tbody" #正文内容
    search = "//input[@class='ant-input']" #查询框
    # 参数化text中的文档内容
    菜单选择公共 = "//ul[@class='ant-select-dropdown-menu ant-select-dropdown-menu-vertical ant-select-dropdown-menu-root']//li[text()='人脸图库']"
    操作模块 = "(//div[@class='ant-select-selection__rendered'])[1]"
    操作功能 = "(//div[@class='ant-select-selection__rendered'])[2]"
    开始时间 = "(//input[@placeholder='请选择时间'])[1]"
    结束时间 = "(//input[@placeholder='请选择时间'])[2]"




