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

    @pytest.mark.somke
    def test_change_place(self,login_web):
        self.test_change_place.__func__.__doc__ = E.change_place['dec']
        P_log.info("*******开始执行{0}测试用例******".format(E.change_place['name']))
        try:
            First_Page(login_web).select_item('解析管理')
            time.sleep(2)
            任务总数_切换前 = Analytical(login_web).get_text(Analytical.任务总数)
            time.sleep(1)
            Analytical(login_web).click(Analytical.不包含子场所)
            time.sleep(3)
            任务总数_切换后 = Analytical(login_web).get_text(Analytical.任务总数)
            assert int(任务总数_切换前) != int(任务总数_切换后)
        except Exception as e:
            R_log.info("{0}用例执行失败".format(E.change_place['name']))
            P_log.error("{0}用例失败原因:{1}".format(E.change_place['name'], e))
            Analytical(login_web).save_picture('用例异常截图')
            raise e

    @pytest.mark.smoke
    def test_select_place(self,login_web):
        self.test_select_place.__func__.__doc__ = E.select_place['dec']
        P_log.info("*******开始执行{0}测试用例******".format(E.select_place['name']))
        try:
            First_Page(login_web).select_item('解析管理')
            time.sleep(2)
            Analytical(login_web).input_text(Analytical.请输入场所名称,E.select_place['place'])
            Analytical(login_web).click(Analytical.子标签)
            time.sleep(1)
            名称 = Analytical(login_web).get_text(Analytical.子标签名)
            数量 = Analytical(login_web).get_text(Analytical.子标签数量)
            实际数量 = Analytical(login_web).get_text(Analytical.任务总数)
            #取到的数量有多余的括号
            assert 名称 == E.select_place['place'] and 实际数量 in 数量

        except Exception as e:
            R_log.info("{0}用例执行失败".format(E.change_place['name']))
            P_log.error("{0}用例失败原因:{1}".format(E.change_place['name'], e))
            Analytical(login_web).save_picture('用例异常截图')
            raise e


    @pytest.mark.smoke
    def test_query_device(self,login_web):
        self.test_query_device.__func__.__doc__ = E.query_device['dec']
        P_log.info("*******开始执行{0}测试用例******".format(E.query_device['name']))
        First_Page(login_web).select_item('解析管理')
        time.sleep(1)
        try:
            # 获取列表标题头
            head = Analytical(login_web).get_text(Analytical.列表标题)
            Analytical(login_web).input_text(Analytical.请输入设备名称,E.query_device['device'])
            time.sleep(1)
            Analytical(login_web).click(Analytical.查询按钮)
            # 获取列表正文部分
            body = Analytical(login_web).get_text(Analytical.列表)
            # 得到处理完的页面数据，结构式大列表嵌套
            list = Analytical(login_web).process_text(head, body)
            print(list)
            #判断查询到的设备名称是否是查询输入的设备名称
            assert E.query_device['device'] == list[0][0]
        except Exception as e:
            R_log.info("{0}用例执行失败".format(E.query_device['name']))
            P_log.error("{0}用例失败原因:{1}".format(E.query_device['name'], e))
            Analytical(login_web).save_picture('用例异常截图')
            raise e




