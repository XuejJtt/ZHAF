#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author : Zhuzj
# @file : test_user.py
# @time : 2020/9/8 16:04
# @Software :PyCharm

import pytest
from Common.BasePage import BasePage
from PageObjects.登录页面 import login
from PageObjects.首页 import First_Page
from PageObjects.system.user import *
from Common.log import Log
from Common import dir_config
import TestDatas.login_test_datas as LTD

P_log = Log(dir_config.processlog_dir)
R_log = Log(dir_config.resultlog_dir)

@pytest.mark.usefixture("login_web")
class Test_user:
    @pytest.mark.smoke
    def test_newuser(self,login_web):
        P_log.info('*******开始执行【新增用户】测试用例******')
        First_Page(login_web).manager(2,'user')
        User(login_web).add_user()
        try:
            P_log.info("*******开始进行【新增用户】测试用例结果校验*********")
            assert User(login_web).get_user(2) == News.newuser['name']
            R_log.info("******【新增用户】用例执行成功******")
        except Exception as e:
            R_log.info("【新增用户】用例执行失败")
            P_log.error("【新增用户】用例失败,失败原因:{0}".format(e))
            login(login_web).save_picture('用例异常截图')
            raise e

    @pytest.mark.usefixtures
    def test_modifyuser(self,login_web):
        P_log.info('*******开始执行【修改用户】测试用例******')
        First_Page(login_web).manager(2, 'user')
        User(login_web).modify_user()
        try:
            P_log.info("*******开始进行【修改用户】测试用例结果校验*********")
            assert User(login_web).get_user(6) == '2022-12-18'
            assert User(login_web).get_user(7) == '已激活'
            R_log.info("******【修改用户】用例执行成功******")
        except Exception as e:
            R_log.info("【修改用户】用例执行失败")
            P_log.error("【修改用户】用例失败,失败原因:{0}".format(e))
            login(login_web).save_picture('用例异常截图')
            raise e

    @pytest.mark.usefixtures
    def test_freezeuser(self,login_web):
        P_log.info('*******开始执行【冻结用户】测试用例******')
        First_Page(login_web).manager(2, 'user')
        User(login_web).freeze_user()
        try:
            P_log.info("*******开始进行【冻结用户】测试用例结果校验*********")
            assert User(login_web).get_user(7) == '已冻结'
            R_log.info("******【冻结用户】用例执行成功******")
        except Exception as e:
            R_log.info("【冻结用户】用例执行失败")
            P_log.error("【冻结用户】用例失败,失败原因:{0}".format(e))
            login(login_web).save_picture('用例异常截图')
            raise e

    @pytest.mark.usefixtures
    def test_deluser(self,login_web):
        P_log.info('*******开始执行【删除用户】测试用例******')
        First_Page(login_web).manager(2, 'user')
        User(login_web).del_user()
        try:
            P_log.info("*******开始进行【删除用户】测试用例结果校验*********")
            assert User(login_web).get_user_null()=='No Data'
            R_log.info('******【删除用户】测试用例执行成功******')
        except Exception as e:
            R_log.info("【删除用户】用例执行失败")
            P_log.error("【删除用户】用例失败,失败原因:{0}".format(e))
            login(login_web).save_picture('用例异常截图')
            raise e





if __name__ == '__main__':
    pytest.main(["-q","test_user.py"])