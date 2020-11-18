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
        Area_managerment(login_web).new_area(place_date.newarea['areaname'],place_date.newarea['areadisc'])
        try:
            P_log.info("*******开始进行{0}测试用例结果校验*********".format(place_date.newarea['casename']))
            assert Area_managerment(login_web).get_areainfo(0)[0]==place_date.newarea['areaname']
            R_log.info("******{0}用例执行成功******".format(place_date.newarea['casename']))
        except Exception as e:
            R_log.info("{0}用例执行失败".format(place_date.newarea['areaname']))
            P_log.error("{0}用例失败,失败原因:{1}".format(place_date.newarea['casename'],e))
            BasePage(login_web).save_picture('用例异常截图')
            raise e

    @pytest.mark.smoke
    def test_modify_area(self,login_web):
        P_log.info("*******开始执行{0}测试用例******".format(place_date.editarea['casename']))
        First_Page(login_web).manager(5, 'place')
        Area_managerment(login_web).modify_area()
        try:
            P_log.info("*******开始进行{0}测试用例结果校验*********".format(place_date.editarea['casename']))
            assert  Area_managerment(login_web).get_areainfo(1)[0]==place_date.editarea['areaname']
            assert Area_managerment(login_web).get_areainfo(1)[1]==place_date.editarea['areadisc']
            R_log.info("******{0}用例执行成功******".format(place_date.editarea['casename']))
        except Exception as e:
            R_log.info("{0}用例执行失败".format(place_date.editarea['areaname']))
            P_log.error("{0}用例失败,失败原因:{1}".format(place_date.editarea['casename'], e))
            BasePage(login_web).save_picture('用例异常截图')
            raise e

    @pytest.mark.smoke
    def test_delete_area(self,login_web):
        P_log.info("*******开始执行【删除区域】测试用例******")
        First_Page(login_web).manager(5, 'place')
        Area_managerment(login_web).deleteplace(1)
        try:
            P_log.info("*******开始执行【删除区域】测试用例结果校验******")
            assert Area_managerment(login_web).get_infonull(1)=='No Data'
            R_log.info("******【删除区域】测试用例执行成功******")
        except Exception as e:
            R_log.info("【删除区域】测试用例执行失败")
            P_log.error("【删除区域】测试用例失败,失败原因:{1}",e)
            BasePage(login_web).save_picture('用例异常截图')
            raise e

    @pytest.mark.parametrize('data0',place_date.newarea_err)
    def test_newarea_err(self,login_web,data0):
        P_log.info("*******开始执行{0}测试用例******".format(data0['casename']))
        First_Page(login_web).manager(5, 'place')
        if data0['casename']=='新增区域--上级区域为空':
            Area_managerment(login_web).area_Supernull(data0['areaname'], data0['areadisc'])
        else:
            Area_managerment(login_web).new_area(data0['areaname'], data0['areadisc'])
        try:
            P_log.info("*******开始进行{0}测试用例结果校验*********".format(data0['casename']))
            assert Area_managerment(login_web).get_info_err() == data0['errinfo']
            R_log.info("******{0}用例执行成功******".format(data0['casename']))
        except Exception as e:
            R_log.info("{0}用例执行失败".format(data0['casename']))
            P_log.error("{0}用例失败,失败原因:{1}".format(data0['casename'], e))
            BasePage(login_web).save_picture('用例异常截图')
            raise e



    @pytest.mark.smoke
    def test_new_place(self,login_web):
        P_log.info("*******开始执行{0}测试用例******".format(place_date.newplace['casename']))
        First_Page(login_web).manager(5, 'place')
        Area_managerment(login_web).new_place(place_date.newplace['placename'],place_date.newplace['placedisc'])
        try:
           P_log.info("*******开始进行{0}测试用例结果校验*********".format(place_date.newplace['casename']))
           assert Area_managerment(login_web).get_areainfo(2)[0] == place_date.newplace['placename']
           R_log.info("******{0}用例执行成功******".format(place_date.newplace['casename']))
        except Exception as e:
            R_log.info("{0}用例执行失败".format(place_date.newplace['casename']))
            P_log.error("{0}用例失败,失败原因:{1}".format(place_date.newplace['casename'], e))
            BasePage(login_web).save_picture('用例异常截图')
            raise e

    @pytest.mark.smoke
    def test_modify_place(self,login_web):
        P_log.info("*******开始执行{0}测试用例******".format(place_date.editplace['casename']))
        First_Page(login_web).manager(5, 'place')
        Area_managerment(login_web).modify_place()
        try:
            P_log.info("*******开始进行{0}测试用例结果校验*********".format(place_date.editplace['casename']))
            assert Area_managerment(login_web).get_areainfo(3)[0] == place_date.editplace['placename']
            assert Area_managerment(login_web).get_areainfo(3)[1] == place_date.editplace['placedisc']
            R_log.info("******{0}用例执行成功******".format(place_date.editplace['casename']))

        except Exception as e:
            R_log.info("{0}用例执行失败".format(place_date.editplace['casename']))
            P_log.error("{0}用例失败,失败原因:{1}".format(place_date.editplace['casename'], e))
            BasePage(login_web).save_picture('用例异常截图')
            raise e

    @pytest.mark.smoke
    def test_delete_place(self,login_web):
        P_log.info("*******开始执行【删除场所】测试用例******")
        First_Page(login_web).manager(5, 'place')
        Area_managerment(login_web).deleteplace(3)
        try:
            P_log.info("*******开始执行【删除场所】测试用例结果校验******")
            assert Area_managerment(login_web).get_infonull(3) == 'No Data'
            R_log.info("******【删除场所】测试用例执行成功******")
        except Exception as e:
            R_log.info("【删除场所】测试用例执行失败")
            P_log.error("【删除场所】测试用例失败,失败原因:{1}", e)
            BasePage(login_web).save_picture('用例异常截图')
            raise e

    @pytest.mark.parametrize('data1',place_date.newplace_err)
    def test_newpplaceerr(self,login_web,data1):
        P_log.info("*******开始执行{0}测试用例******".format(data1['casename']))
        First_Page(login_web).manager(5, 'place')
        if data1['casename']=='新增场所--场所类型为空':
            Area_managerment(login_web).place_typenull(data1['placename'], data1['placedisc'])
        elif data1['casename']=='新增场所--上级区域为空':
            Area_managerment(login_web).place_Supernull(data1['placename'], data1['placedisc'])
        else:
            Area_managerment(login_web).new_place(data1['placename'], data1['placedisc'])
        try:
            P_log.info("*******开始进行{0}测试用例结果校验*********".format(data1['casename']))
            assert Area_managerment(login_web).get_info_err() == data1['errinfo']
            R_log.info("******{0}用例执行成功******".format(data1['casename']))
        except Exception as e:
            R_log.info("{0}用例执行失败".format(data1['casename']))
            P_log.error("{0}用例失败,失败原因:{1}".format(data1['casename'], e))
            BasePage(login_web).save_picture('用例异常截图')
            raise e

    #根据性质场所/区域查询

    def test_naturesearch(self,login_web):
        P_log.info("*******开始执行【性质查询】测试用例******")
        First_Page(login_web).manager(4, 'place')
        Area_managerment(login_web).search_info()
        listall=Area_managerment(login_web).get_areainfos()
        list_n=list(set(listall[2]))
        try:
            P_log.info("*******开始进行【性质查询】测试用例结果校验*********")
            assert "区域" not in listall[2]
            assert len(list_n)==1
            R_log.info("******【性质查询】用例执行成功******")
        except Exception as e:
            R_log.info("【性质查询】用例执行失败")
            P_log.error("【性质查询】用例执行失败,失败原因：{0}".format(e))
            BasePage(login_web).save_picture('用例异常截图')
            raise e

    #根据类型查询

    def test_typesearch(self,login_web):
        P_log.info("*******开始执行【类型查询】测试用例******")
        First_Page(login_web).manager(4, 'place')
        Area_managerment(login_web).search_info(option="type")
        listall = Area_managerment(login_web).get_areainfos()
        list_n = list(set(listall[3]))
        try:
            P_log.info("*******开始进行【类型查询】测试用例结果校验*********")
            assert "餐饮美食" in listall[3]
            assert len(list_n) == 1#验证查询结果中只存在一个值
            R_log.info("******【类型查询】用例执行成功******")
        except Exception as e:
            R_log.info("【类型查询】用例执行失败")
            P_log.error("【类型查询】用例执行失败,失败原因：{0}".format(e))
            BasePage(login_web).save_picture('用例异常截图')
            raise e








    def test_gettable(self,login_web):
        First_Page(login_web).manager(4, 'place')
        listall=Area_managerment(login_web).get_areainfos()
        P_log.info("获取到的场所名称为：{0},获取到的场所描述为：{1},获取到的场所性质为：{2},获取到的场所类型为：{3}".format(listall[0],listall[1],listall[2],listall[3]))
        print(list(set(listall[2])))
        list_n = list(set(listall[2]))
        print(len(list_n))

if __name__=='__main__':
    pytest.main(['-q','test_place.py'])