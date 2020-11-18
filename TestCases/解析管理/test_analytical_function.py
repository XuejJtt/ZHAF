#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 15:26
# @File    : test_analytical_function.py
# @Software: PyCharm



import pytest
from PageObjects.index.first_page import First_Page
from PageObjects.edgeIntelligence.edgeIntelligence import *
from PageObjects.analytical.analytical import *
from Common.log import Log
from Common import dir_config
from TestDatas.解析管理 import analytical_data as E
from selenium.webdriver.support import expected_conditions as EC
from Common.Compare import GraphicalLocator as G

# 定义resultlog和processlog
P_log = Log(processlog_dir)
R_log = Log(resultlog_dir)

@pytest.mark.usefixtures('login_web')
class Test_analytical:


    @pytest.mark.smoke
    def test_sum_devices(self,login_web):
        self.test_sum_devices.__func__.__doc__ = E.sum_devices['dec']
        P_log.info("*******开始执行{0}测试用例******".format(E.sum_devices['name']))
        try:
            First_Page(login_web).select_item('解析管理')
            time.sleep(2)
            任务总数 = Analytical(login_web).get_text(Analytical.任务总数)
            运行中 = Analytical(login_web).get_text(Analytical.运行中)
            已停止 = Analytical(login_web).get_text(Analytical.已停止)
            故障中 = Analytical(login_web).get_text(Analytical.故障中)
            # 判断退出全屏按钮出现在当前的页面中
            assert int(任务总数) == int(运行中) + int(已停止) + int(故障中)
        except Exception as e:
            R_log.info("{0}用例执行失败".format(E.sum_devices['name']))
            P_log.error("{0}用例失败原因:{1}".format(E.sum_devices['name'], e))
            Analytical(login_web).save_picture('用例异常截图')
            raise e
