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


# 定义resultlog和processlog
P_log = Log(processlog_dir)
R_log = Log(resultlog_dir)


class Analytical(BasePage):
    任务总数 = '(//div[@class="number"])[1]'
    运行中 = '(//div[@class="number"])[2]'
    已停止 = '(//div[@class="number"])[3]'
    故障中 = '(//div[@class="number"])[4]'