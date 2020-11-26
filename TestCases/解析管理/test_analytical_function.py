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
            list_1 = Analytical(login_web).process_text(head, body)
            #判断查询到的设备名称是否是查询输入的设备名称
            assert E.query_device['device'] == list_1[0][0]
        except Exception as e:
            R_log.info("{0}用例执行失败".format(E.query_device['name']))
            P_log.error("{0}用例失败原因:{1}".format(E.query_device['name'], e))
            Analytical(login_web).save_picture('用例异常截图')
            raise e


    @pytest.mark.smoke
    def test_query_reset(self,login_web):
        self.test_query_reset.__func__.__doc__ = E.query_reset['dec']
        P_log.info("*******开始执行{0}测试用例******".format(E.query_reset['name']))
        First_Page(login_web).select_item('解析管理')
        time.sleep(1)
        try:
            head = Analytical(login_web).get_text(Analytical.列表标题)
            Analytical(login_web).input_text(Analytical.请输入设备名称, E.query_reset['device'])
            time.sleep(1)
            Analytical(login_web).click(Analytical.查询按钮)
            body = Analytical(login_web).get_text(Analytical.列表)
            time.sleep(1)
            Analytical(login_web).click(Analytical.重置按钮)
            time.sleep(2.5)
            body_1 = Analytical(login_web).get_text(Analytical.列表)
            list = Analytical(login_web).process_text(head,body)
            list_1 = Analytical(login_web).process_text(head,body_1)
            #判断标准执行前后的解析列表长度不相等
            assert list != list_1
        except Exception as e:
            R_log.info("{0}用例执行失败".format(E.query_reset['name']))
            P_log.error("{0}用例失败原因:{1}".format(E.query_reset['name'], e))
            Analytical(login_web).save_picture('用例异常截图')
            raise e

    @pytest.mark.smoke
    def test_mix_select(self,login_web):
        self.test_mix_select.__func__.__doc__ = E.mix_query['dec']
        P_log.info("*******开始执行{0}测试用例******".format(E.query_reset['name']))
        First_Page(login_web).select_item('解析管理')
        time.sleep(1)
        try:
            head = Analytical(login_web).get_text(Analytical.列表标题)
            time.sleep(2)
            Analytical(login_web).click(Analytical.设备类型)
            time.sleep(2)
            Analytical(login_web).select_type(E.mix_query['type'])
            time.sleep(2)
            Analytical(login_web).click(Analytical.任务状态)
            time.sleep(2)
            Analytical(login_web).select_state(E.mix_query['state'])
            time.sleep(1)
            Analytical(login_web).click(Analytical.查询按钮)
            time.sleep(1)
            body = Analytical(login_web).get_text(Analytical.列表)
            list_1 = Analytical(login_web).process_text(head, body)
            #检验筛选过后的实际状态与预期的状态一致
            assert list_1[2][0] == E.mix_query['type'] and list_1[3][0] == E.mix_query['state']
        except Exception as e:
            R_log.info("{0}用例执行失败".format(E.query_reset['name']))
            P_log.error("{0}用例失败原因:{1}".format(E.query_reset['name'], e))
            Analytical(login_web).save_picture('用例异常截图')
            raise e


    @pytest.mark.parametrize('data', E.devices_select)
    def test_device_type_select(self,login_web,data):
        self.test_device_type_select.__func__.__doc__ = data['dec']
        P_log.info("*******开始执行{0}测试用例******".format(data['name']))
        First_Page(login_web).select_item('解析管理')
        time.sleep(1)
        try:
            head = Analytical(login_web).get_text(Analytical.列表标题)
            time.sleep(1)
            Analytical(login_web).click(Analytical.设备类型)
            time.sleep(1)
            Analytical(login_web).select_type(data['type'])
            time.sleep(1)
            Analytical(login_web).click(Analytical.查询按钮)
            body = Analytical(login_web).get_text(Analytical.列表)
            list_1 = Analytical(login_web).process_text(head, body)
            if list_1[0][0] == '暂无数据':
                P_log.info("查询结果为空")
            else:
                assert list_1[2][0] == data['type']

        except Exception as e:
            R_log.info("{0}用例执行失败".format(data['name']))
            P_log.error("{0}用例失败原因:{1}".format(data['name'], e))
            Analytical(login_web).save_picture('用例异常截图')
            raise e

    @pytest.mark.parametrize('data', E.task_select)
    def test_task_state_select(self,login_web,data):
        self.test_device_type_select.__func__.__doc__ = data['dec']
        P_log.info("*******开始执行{0}测试用例******".format(data['name']))
        First_Page(login_web).select_item('解析管理')
        time.sleep(1)
        try:
            head = Analytical(login_web).get_text(Analytical.列表标题)
            time.sleep(1)
            Analytical(login_web).click(Analytical.任务状态)
            time.sleep(1)
            Analytical(login_web).select_state(data['state'])
            time.sleep(1)
            Analytical(login_web).click(Analytical.查询按钮)
            body = Analytical(login_web).get_text(Analytical.列表)
            list_1 = Analytical(login_web).process_text(head, body)
            if list_1[0][0] == '暂无数据':
                P_log.info("查询结果为空")
            else:
                assert list_1[3][0] == data['state']
        except Exception as e:
            R_log.info("{0}用例执行失败".format(data['name']))
            P_log.error("{0}用例失败原因:{1}".format(data['name'], e))
            Analytical(login_web).save_picture('用例异常截图')
            raise e

    @pytest.mark.smoke
    def test_batch_start(self,login_web):
        self.test_mix_select.__func__.__doc__ = E.batch_start['dec']
        P_log.info("*******开始执行{0}测试用例******".format(E.batch_start['name']))
        First_Page(login_web).select_item('解析管理')
        time.sleep(1)
        try:
            head = Analytical(login_web).get_text(Analytical.列表标题)
            Analytical(login_web).input_text(Analytical.请输入设备名称, E.batch_start['device'])
            time.sleep(2)
            Analytical(login_web).click(Analytical.查询按钮)
            body = Analytical(login_web).get_text(Analytical.列表)
            list_1 = Analytical(login_web).process_text(head,body)
            if list_1[3][0] == '已停止':
                P_log.info('当前设备状态为已停止开始批量启动测试')
                Analytical(login_web).click(Analytical.筛选框)
                time.sleep(1)
                Analytical(login_web).click(Analytical.批量启动)
                time.sleep(1)
                Analytical(login_web).click(Analytical.启动)
                time.sleep(2)
                Analytical(login_web).click(Analytical.确定)
                # 等待相机启动完成
                time.sleep(8)
                body_1 = Analytical(login_web).get_text(Analytical.列表)
                list_2 = Analytical(login_web).process_text(head,body_1)
                assert list_2[3][0] == '运行中'
            else:
                P_log.info('当前设备状态不是已停止，无法继续执行用例')
                raise Exception('当前设备状态无法继续执行用例')
        except Exception as e:
            R_log.info("{0}用例执行失败".format(E.batch_start['name']))
            P_log.error("{0}用例失败原因:{1}".format(E.batch_start['name'], e))
            Analytical(login_web).save_picture('用例异常截图')
            raise e

    @pytest.mark.smoke
    def test_batch_stop(self,login_web):
        self.test_batch_stop.__func__.__doc__ = E.batch_stop['dec']
        P_log.info("*******开始执行{0}测试用例******".format(E.batch_start['name']))
        First_Page(login_web).select_item('解析管理')
        time.sleep(1)
        try:
            head = Analytical(login_web).get_text(Analytical.列表标题)
            Analytical(login_web).input_text(Analytical.请输入设备名称, E.batch_stop['device'])
            time.sleep(2)
            Analytical(login_web).click(Analytical.查询按钮)
            body = Analytical(login_web).get_text(Analytical.列表)
            list_1 = Analytical(login_web).process_text(head, body)
            if list_1[3][0] == '运行中':
                P_log.info('当前设备状态为运行中开始批量启动测试')
                Analytical(login_web).click(Analytical.筛选框)
                time.sleep(1)
                Analytical(login_web).click(Analytical.批量停止)
                time.sleep(1)
                Analytical(login_web).click(Analytical.启动)
                time.sleep(2)
                Analytical(login_web).click(Analytical.确定)
                # 等待相机启动完成
                time.sleep(8)
                body_1 = Analytical(login_web).get_text(Analytical.列表)
                list_2 = Analytical(login_web).process_text(head, body_1)
                assert list_2[3][0] == '运行中'
            else:
                P_log.info('当前设备状态不是运行中，无法继续执行用例')
                raise Exception('当前设备状态无法继续执行用例')
        except Exception as e:
            R_log.info("{0}用例执行失败".format(E.batch_stop['name']))
            P_log.error("{0}用例失败原因:{1}".format(E.batch_stop['name'], e))
            Analytical(login_web).save_picture('用例异常截图')
            raise e


    @pytest.mark.smoke
    def test_batch_modification(self,login_web):
        self.test_batch_stop.__func__.__doc__ = E.batch_modification['dec']
        P_log.info("*******开始执行{0}测试用例******".format(E.batch_modification['name']))
        First_Page(login_web).select_item('解析管理')
        time.sleep(1)
        try:
            pass
        except Exception as e:
            R_log.info("{0}用例执行失败".format(E.batch_modification['name']))
            P_log.error("{0}用例失败原因:{1}".format(E.batch_modification['name'], e))
            Analytical(login_web).save_picture('用例异常截图')
            raise e