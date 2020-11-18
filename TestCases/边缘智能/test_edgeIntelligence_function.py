#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 17:54
# @File    : test_edgeIntelligence_function.py
# @Software: PyCharm


import pytest
from PageObjects.index.first_page import First_Page
from PageObjects.edgeIntelligence.edgeIntelligence import *
from Common.log import Log
from Common import dir_config
from TestDatas.边缘智能 import edgeIntelligence_data as E
from selenium.webdriver.support import expected_conditions as EC
from Common.Compare import GraphicalLocator as G

#定义resultlog和processlog
P_log = Log(dir_config.processlog_dir)
R_log = Log(dir_config.resultlog_dir)


@pytest.mark.usefixtures("login_web")
class Test_edgeInteligence:

    @pytest.mark.smoke
    def test_fullscreen(self,login_web):
        self.test_fullscreen.__func__.__doc__ = E.full_screen['dec']
        P_log.info("*******开始执行{0}测试用例******".format(E.full_screen['name']))
        try:
            First_Page(login_web).select_item('边缘智能')
            time.sleep(2)
            EdgeIntelligence(login_web).click(EdgeIntelligence.全屏预览)
            time.sleep(1)
            # 判断退出全屏按钮出现在当前的页面中
            assert EC.invisibility_of_element_located(EdgeIntelligence.退出全屏)
        except Exception as e:
            R_log.info("{0}用例执行失败".format(E.full_screen['name']))
            P_log.error("{0}用例失败原因:{1}".format(E.full_screen['name'], e))
            EdgeIntelligence(login_web).save_picture('用例异常截图')
            raise e


    @pytest.mark.smoke
    def test_change_model(self,login_web):
        self.test_change_model.__func__.__doc__ = E.model_change['dec']
        P_log.info("*******开始执行{0}测试用例******".format(E.model_change['name']))
        try:
            First_Page(login_web).select_item('边缘智能')
            time.sleep(2)
            EdgeIntelligence(login_web).click(EdgeIntelligence.下拉箭头)
            time.sleep(2)
            EdgeIntelligence(login_web).click(EdgeIntelligence.预览模式)
            time.sleep(1)
            # 判断退出全屏按钮出现在当前的页面中
            assert EC.invisibility_of_element_located(EdgeIntelligence.关闭所有预览)
        except Exception as e:
            R_log.info("{0}用例执行失败".format(E.model_change['name']))
            P_log.error("{0}用例失败原因:{1}".format(E.model_change['name'], e))
            EdgeIntelligence(login_web).save_picture('用例异常截图')
            raise e


    @pytest.mark.smoke
    def test_search_device(self,login_web):
        self.test_search_device.__func__.__doc__ = E.search_onlinge_device['dec']
        P_log.info("*******开始执行{0}测试用例******".format(E.search_onlinge_device['name']))
        try:
            First_Page(login_web).select_item("边缘智能")
            time.sleep(2)
            EdgeIntelligence(login_web).input_text(EdgeIntelligence.请输入设备名称, E.search_onlinge_device['device'])
            device = EdgeIntelligence(login_web).get_text(EdgeIntelligence.在线设备标签)
            assert device == E.search_onlinge_device['device']
        except Exception as e:
            R_log.info("{0}用例执行失败".format(E.search_onlinge_device['name']))
            P_log.error("{0}用例失败原因:{1}".format(E.search_onlinge_device['name'], e))
            EdgeIntelligence(login_web).save_picture('用例异常截图')
            raise e


    @pytest.mark.smoke
    def test_search_outline_device(self,login_web):
        self.test_search_outline_device.__func__.__doc__ = E.search_outline_device['dec']
        P_log.info("*******开始执行{0}测试用例******".format(E.search_outline_device['name']))
        try:
            First_Page(login_web).select_item("边缘智能")
            time.sleep(2)
            EdgeIntelligence(login_web).input_text(EdgeIntelligence.请输入设备名称, E.search_outline_device['device'])
            device = EdgeIntelligence(login_web).get_text(EdgeIntelligence.在线设备标签)
            assert device == E.search_outline_device['device']
        except Exception as e:
            R_log.info("{0}用例执行失败".format(E.search_outline_device['name']))
            P_log.error("{0}用例失败原因:{1}".format(E.search_outline_device['name'], e))
            EdgeIntelligence(login_web).save_picture('用例异常截图')
            raise e


    @pytest.mark.parametrize('data', E.resource_select)
    @pytest.mark.smoke
    def test_resource(self,login_web,data):
        self.test_resource.__func__.__doc__ = data['dec']
        P_log.info("*******开始执行{0}测试用例******".format(data['name']))
        try:
            First_Page(login_web).select_item("边缘智能")
            time.sleep(2)
            EdgeIntelligence(login_web).click(EdgeIntelligence.资源按钮)
            time.sleep(1)
            d = EdgeIntelligence.__dict__
            # 字典解析式
            dic = {key: d[key] for key in d if "_" not in d}
            EdgeIntelligence(login_web).click(dic[data['object']])
            # 图像比对
            src = EdgeIntelligence(login_web).save_picture('src')
            time.sleep(1)
            res = G(data['pic']).find_and_check(src)
            assert res

        except Exception as e:
            R_log.info("{0}用例执行失败".format(data['name']))
            P_log.error("{0}用例失败原因:{1}".format(data['name'], e))
            EdgeIntelligence(login_web).save_picture('用例异常截图')
            raise e