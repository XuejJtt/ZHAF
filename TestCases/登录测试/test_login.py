#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 14:51
# @Author  : Xuej
# @File    : test_login.py
# @Software: PyCharm

import pytest
from PageObjects.login.login import login
from PageObjects.index.first_page import First_Page
from Common.log import Log
from Common import dir_config
import TestDatas.公共数据.login_test_datas as LTD


#定义resultlog和processlog
P_log = Log(dir_config.processlog_dir)
R_log = Log(dir_config.resultlog_dir)



@pytest.mark.usefixtures("init_web")
class Test_login:

    @pytest.mark.smoke
    def test_login_success(self,init_web):
        #动态添加Description中的内容
        self.test_login_success.__func__.__doc__ =LTD.success_data['dec']
        P_log.info("*******开始执行{0}测试用例******".format(LTD.success_data['name']))
        login(init_web).login_system(LTD.success_data['username'],LTD.success_data['pwd'])
        P_log.info("********{0}用例执行完成*******".format(LTD.success_data['name']))
        name = First_Page(init_web).get_login_name()
        try:
            P_log.info("*******开始进行结果校验*********")
            assert name == LTD.success_data['username']
            R_log.info("{0}用例执行成功".format(LTD.success_data['name']))
        except Exception as e:
            R_log.info("{0}用例执行失败".format(LTD.success_data['name']))
            P_log.error("{0}用例失败原因:{1}".format(LTD.success_data['name'],e))
            login(init_web).save_picture('用例异常截图')
            raise e

    @pytest.mark.parametrize('data',LTD.error_data)
    def test_login_error(self,init_web,data):
        self.test_login_error.__func__.__doc__ = data['dec']
        P_log.info("*******开始执行{0}测试用例******".format(data['name']))
        login(init_web).login_system(data['username'], data['pwd'])
        P_log.info("********{0}用例执行完成*******".format(data['name']))
        msg = login(init_web).get_login_msg()
        try:
            P_log.info("*******开始进行结果校验*********")
            assert data['errormsg'] in msg
            R_log.info("{0}用例执行成功".format(data['name']))
        except Exception as e:
            R_log.info("{0}用例执行失败".format(data['name']))
            P_log.error("{0}用例失败原因:{1}".format(data['name'], e))
            login(init_web).save_picture('用例异常截图')
            raise e










if __name__ == '__main__':
    pytest.main(["-q","test_login.py"])



