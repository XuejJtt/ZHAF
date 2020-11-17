#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 14:35
# @File    : edgeIntelligence.py
# @Software: PyCharm


from Common.BasePage import *
from Common.log import Log
from Common.dir_config import *
from selenium.webdriver.common.by import By
import time

# 定义resultlog和processlog
P_log = Log(processlog_dir)
R_log = Log(resultlog_dir)


class EdgeIntelligence(BasePage):
    全屏预览 = '//span[contains(text(),"全屏预览")]'
    退出全屏 = '//span[contains(text(),"退出全屏")]'
    预览模式 = '//span[contains(text(),"预览模式")]'
    地图模式 = '//span[contains(text(),"地图模式")]'
    关闭所有预览 = '//div[contains(text(),"关闭全部预览")]'
    下拉箭头 = '//i[@class="el-select__caret el-input__icon el-icon-arrow-up"]'
    请输入设备名称 = '(//input[@class="el-input__inner"])[1]'
    在线设备标签 = '(//span[@class="el-popover__reference"])[1]'
    资源按钮 = '//div[@style="cursor: pointer;"]'
    视频流相机 = '//div[contains(text(),"视频流相机")]'
    智能抓拍机 = '//div[contains(text(),"智能抓拍机")]'
    GB28181 = '//div[contains(text(),"GB28181")]'
    视图库相机 = '//div[contains(text(),"视图库")]'
    在线 = '(//button)[1]'
    离线 = '(//button)[2]'