#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 11:40
# @File    : analytical.py
# @Software: PyCharm


from Common.BasePage import *
from Common.log import Log
from Common.dir_config import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


# 定义resultlog和processlog
P_log = Log(processlog_dir)
R_log = Log(resultlog_dir)


class Analytical(BasePage):
    任务总数 = '(//div[@class="number"])[1]'
    运行中 = '(//div[@class="number"])[2]'
    已停止 = '(//div[@class="number"])[3]'
    故障中 = '(//div[@class="number"])[4]'
    包含子场所 = '//span[text()="包含子场所"]/preceding-sibling::span'
    不包含子场所 = '//span[text()="不包含子场所"]/preceding-sibling::span'
    子标签 = '(//span[@class="custom-tree-node"])[5]'
    子标签名 = '(//span[@class="custom-tree-node"])[5]//span[1]'
    子标签数量 = '(//span[@class="custom-tree-node"])[5]//span[2]'
    请输入场所名称 = '//input[@placeholder="请输入场所名称"]'
    请输入设备名称 = '//input[@placeholder="请输入设备名称"]'
    列表 = '//div[@class="el-table__body-wrapper is-scrolling-none"]'
    列表标题 = '//div[@class="el-table__header-wrapper"]'
    查询按钮 = '//span[text()="查询"]'
    重置按钮 = '//span[text()="重置"]'
    设备类型 = '(//input[@placeholder="请选择"])[1]'
    任务状态 = '(//input[@placeholder="请选择"])[2]'

    def select_type(self,item):
        if item =='':
            pass


    def select_state(self,state):
        if state =='':
            pass
