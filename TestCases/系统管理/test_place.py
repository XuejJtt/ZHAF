#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author : Zhuzj
# @file : test_place.py
# @time : 2020/9/8 16:04
# @Software :PyCharm

import pytest
from PageObjects.system.place import *


@pytest.mark.usefixtures("login_web")
class Test_Place:
    @pytest.mark.smoke
    def test_new_area(self,login_web):
        P_log.info("*******开始执行{0}测试用例******".format(place_date.newarea['casename']))
        First_Page(login_web).manager(5,'place')
        Area_managerment(login_web).new_area()
        try:
            P_log.info("*******开始进行{0}测试用例结果校验*********".format(place_date.newarea['casename']))
            assert Area_managerment(login_web).get_areainfo()==place_date.newarea['areaname']
            R_log.info("******{0}用例执行成功******".format(place_date.newarea['casename']))
        except Exception as e:
            R_log.info("{0}用例执行失败".format(place_date.newarea['areaname']))
            P_log.error("{0}用例失败,失败原因:{1}".format(place_date.newarea['casename'],e))
            BasePage(login_web).save_picture('用例异常截图')
            raise e

    @pytest.mark.smoke
    def test_new_place(self,login_web):
        P_log.info("*******开始执行{0}测试用例******".format(place_date.newplace['casename']))
        First_Page(login_web).manager(5, 'place')
        Area_managerment(login_web).new_place()
        try:
           P_log.info("*******开始进行{0}测试用例结果校验*********".format(place_date.newplace['casename']))
           assert Area_managerment(login_web).get_placeinfo() == place_date.newplace['placename']
           R_log.info("******{0}用例执行成功******".format(place_date.newplace['casename']))
        except Exception as e:
            R_log.info("{0}用例执行失败".format(place_date.newplace['casename']))
            P_log.error("{0}用例失败,失败原因:{1}".format(place_date.newplace['casename'], e))
            BasePage(login_web).save_picture('用例异常截图')
            raise e

if __name__=='__main__':
    pytest.main(['-q','test_place.py'])