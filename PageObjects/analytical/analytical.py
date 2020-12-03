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
    # 子标签数需要根据页面标签的变化进行调整
    子标签 = '(//span[@class="custom-tree-node"])[7]'
    子标签名 = '(//span[@class="custom-tree-node"])[7]//span[1]'
    子标签数量 = '(//span[@class="custom-tree-node"])[7]//span[2]'
    请输入场所名称 = '//input[@placeholder="请输入场所名称"]'
    请输入设备名称 = '//input[@placeholder="请输入设备名称"]'
    列表 = '//div[@class="el-table__body-wrapper is-scrolling-none"]'
    列表标题 = '//div[@class="el-table__header-wrapper"]'
    查询按钮 = '//span[text()="查询"]'
    重置按钮 = '//span[text()="重置"]'
    设备类型 = '(//input[@placeholder="请选择"])[1]'
    任务状态 = '(//input[@placeholder="请选择"])[2]'
    下拉列表 = '(//ul[@class="el-scrollbar__view el-select-dropdown__list"])[3]'
    批量启动 = '//span[text()="批量启动"]/..'
    批量停止 = '//span[text()="批量停止"]/..'
    批量修改 = '//span[text()="批量修改"]/..'
    筛选框 = '(//span[@class="el-checkbox__inner"])[2]'
    启动 = '//span[text()="启动"]/..'
    确定 = '//button[@class="el-button el-button--default el-button--small el-button--primary "]'
    人脸 = '(//span[@class="el-checkbox__inner"])[4]'
    人体 = '(//span[@class="el-checkbox__inner"])[5]'
    机动车 = '(//span[@class="el-checkbox__inner"])[6]'
    非机动车 = '(//span[@class="el-checkbox__inner"])[7]'
    批量修改确定 = '(//button[@class="el-button el-button--primary"])[1]'
    查看 = '(//button[@class="el-button el-button--text el-button--small"])[1]'
    启动按钮 = '(//button[@class="el-button el-button--text el-button--small"])[2]'
    修改 = '(//button[@class="el-button el-button--text el-button--small"])[3]'
    停止按钮 = '//button[@class="el-button error el-button--text el-button--small"]'
    设备名称 = '(//h3[@class="title"])[1]'

    #选择设备类型
    def select_type(self,item):

        self.click(self.设备类型)
        if item =='智能抓拍机':
            # self.click('(//ul[@class="el-scrollbar__view el-select-dropdown__list"])[3]/li[2]')
            self.excute_js('(//ul[@class="el-scrollbar__view el-select-dropdown__list"])[3]/li[2]')
        elif item =='视频流相机':
            self.excute_js('(//ul[@class="el-scrollbar__view el-select-dropdown__list"])[3]/li[3]')
        elif item =='GB28181':
            self.excute_js('(//ul[@class="el-scrollbar__view el-select-dropdown__list"])[3]/li[4]')
        elif item =='1400视图库':
            self.excute_js('(//ul[@class="el-scrollbar__view el-select-dropdown__list"])[3]/li[5]')
    #选择任务状态
    def select_state(self,state):
        self.click(self.任务状态)
        if state =='已停止':
            self.excute_js('(//ul[@class="el-scrollbar__view el-select-dropdown__list"])[3]/li[2]')
        elif state =='运行中':
            self.excute_js('(//ul[@class="el-scrollbar__view el-select-dropdown__list"])[3]/li[3]')
        elif state == '启动中':
            self.excute_js('(//ul[@class="el-scrollbar__view el-select-dropdown__list"])[3]/li[4]')
        elif state == '停止中':
            self.excute_js('(//ul[@class="el-scrollbar__view el-select-dropdown__list"])[3]/li[5]')
        elif state == '故障中':
            self.excute_js('(//ul[@class="el-scrollbar__view el-select-dropdown__list"])[3]/li[6]')
