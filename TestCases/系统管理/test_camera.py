#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author : Zhuzj
# @file : test_camera.py
# @time : 2020/9/10 16:33
# @Software :PyCharm

from PageObjects.system.camera import *
from PageObjects.index.first_page import First_Page
import TestDatas.系统管理.newcamera  as LD
import pytest

@pytest.mark.usefixtures("login_web")

class Test_Camera():
    @pytest.mark.smoke
    #新增视频流相机
    def test_newvideo(self,login_web):
        First_Page(login_web).manager(3,'camera')
        P_log.info("*******开始执行{0}测试用例******".format(LD.newvideo['casename']))
        Camera(login_web).newvideo(LD.newvideo['devicename'], LD.newvideo['deviceadress'], LD.newvideo['longitude'], LD.newvideo['latitude'])
        try:
            P_log.info("*******开始执行{0}测试用例结果校验******".format(LD.newvideo['casename']))
            assert Camera(login_web).getinfo(LD.newvideo['devicename'])[0]==LD.newvideo['devicename']#设备名称校验正确
            R_log.info("*******{0}测试用例执行成功******".format(LD.newvideo['casename']))
        except Exception as e:
            P_log.info("*******{0}测试用例执行失败******".format(LD.newvideo['casename']))
            R_log.info("*******{0}测试用例执行失败，失败原因{1}******".format(LD.newvideo['casename'],e))
            raise e

    def test_modifyvido(self,login_web):
        First_Page(login_web).manager(3, 'camera')
        P_log.info("*******开始执行【编辑视频流相机】测试用例******")
        Camera(login_web).modifyvideo(LD.newvideo['devicename'],LD.newvideo['SN'])
        try:
            P_log.info("*******开始执行【编辑视频流相机】测试用例结果校验******")
            assert Camera(login_web).getinfo(LD.newvideo['devicename'])[1] == LD.newvideo['SN']#设备SN码校验正确
        except Exception as e:
            P_log.info("*******【编辑视频流相机】测试用例执行失败******")
            R_log.info("*******【编辑视频流相机】测试用例执行失败,失败原因{0}******".format(e))
            raise e




    def test_delvideo(self,login_web):
        First_Page(login_web).manager(3,'camera')
        P_log.info("*******开始执行删除视频流相机测试用例******")
        Camera(login_web).delvideo(LD.newvideo['devicename'])
        try:
            P_log.info("*******开始执行删除视频流相机测试用例结果校验******")
            assert Camera(login_web).getnodata(LD.newvideo['devicename'])=="No Data"
            R_log.info("*******删除视频流相机测试用例执行成功******")
        except Exception as e:
            P_log.info("*******删除视频流相机测试用例执行失败******")
            R_log.info("*******删除视频流相机测试用例执行失败,失败原因{0}******".format(e))
            raise e



if __name__=="__main__":
    pytest.main(['-q', 'test_camera.py'])