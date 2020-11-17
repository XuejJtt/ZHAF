#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author : Zhuzj
# @file : test_role.py
# @time : 2020/11/10 14:17
# @Software :PyCharm

import pytest
from PageObjects.index.first_page import *
from PageObjects.system.role import *
from  Common.read_cofig import *
from Common.dir_config import *
import TestDatas.系统管理.rolemanage  as d

#读取yaml文件内容
# d=Read_Config(testdatas_dir+"\\"+'系统管理',"newrole.yaml").read_yaml()

@pytest.mark.usefixtures("login_web")
class Test_Role():
    def test_newrole(self,login_web):
        P_log.info('*******开始执行【{0}】测试用例******'.format(d.addrole["casename"]))
        First_Page(login_web).manager(1,"role")
        role_manage(login_web).new_role(d.addrole["rolename"],d.addrole['roledisc'])
        try:
            P_log.info("*******开始进行【{0}】测试用例结果校验*********".format(d.addrole["casename"]))
            assert d.addrole["rolename"] in role_manage(login_web).getroletext()[0]
            P_log.info("新增后的角色名为：{0}".format(role_manage(login_web).getroletext()[0]))
            assert d.addrole["roledisc"] in role_manage(login_web).getroletext()[1]
            P_log.info("新增后的角色描述为：{0}".format(role_manage(login_web).getroletext()[1]))
            R_log.info("******【{0}】用例执行成功******".format(d.addrole["casename"]))
        except Exception as e:
            R_log.info("******【{0}】用例执行失败******")
            P_log.error("******【{0}】用例失败,失败原因:{1}******".format(d.addrole["casename"],e))
            role_manage(login_web).save_picture('用例异常截图')
            raise e

    def test_modifyrole(self,login_web):
        P_log.info('*******开始执行【{0}】测试用例******'.format(d.editrole["casename"]))
        First_Page(login_web).manager(1,"role")
        role_manage(login_web).modify_role(d.addrole["rolename"],d.editrole['rolename'],d.editrole['roledisc'])
        try:
            P_log.info("*******开始进行【{0}】测试用例结果校验*********".format(d.editrole["casename"]))
            assert d.editrole["rolename"] in role_manage(login_web).getroletext()[0]
            P_log.info("修改后的角色名为：{0}".format(role_manage(login_web).getroletext()[0]))
            assert d.editrole["roledisc"] in role_manage(login_web).getroletext()[1]
            P_log.info("修改后的角色描述为：{0}".format(role_manage(login_web).getroletext()[1]))
            R_log.info("******【{0}】用例执行成功******".format(d.editrole["casename"]))
        except Exception as e:
            R_log.info("******【{0}】用例执行失败******".format(d.editrole["casename"]))
            P_log.error("******【{0}】用例失败,失败原因:{1}******".format(d.editrole["casename"],e))
            role_manage(login_web).save_picture('用例异常截图')
            raise e

    def test_delrole(self,login_web):
        P_log.info('*******开始执行【删除角色】测试用例******')
        First_Page(login_web).manager(1, "role")
        role_manage(login_web).del_role(d.editrole['rolename'])
        try:
            P_log.info("*******开始进行【删除角色】测试用例结果校验*********")
            assert d.editrole["rolename"] not in role_manage(login_web).getroletext()[0]
            P_log.info("删除后的角色名为：{0}".format(role_manage(login_web).getroletext()[0]))
            assert d.editrole["roledisc"] not in role_manage(login_web).getroletext()[1]
            P_log.info("删除后的角色描述为：{0}".format(role_manage(login_web).getroletext()[1]))
            R_log.info("******【删除角色】用例执行成功******")
        except Exception as e:
            R_log.info("******【删除角色】用例执行失败******")
            P_log.error("******【删除角色】用例失败,失败原因:{0}******".format(e))
            role_manage(login_web).save_picture('用例异常截图')
            raise e


if __name__ == '__main__':
    pytest.main(["-q", "test_role.py"])
