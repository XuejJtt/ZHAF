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
    def test_newvideo(self,login_web):#新增视频流相机
        First_Page(login_web).manager(3,'camera')
        P_log.info("*******开始执行{0}测试用例******".format(LD.newvideo['casename']))
        Camera(login_web).newvideo(LD.newvideo['devicename'], LD.newvideo['deviceadress'])
        try:
            P_log.info("*******开始执行{0}测试用例结果校验******".format(LD.newvideo['casename']))
            assert Camera(login_web).getinfo(LD.newvideo['devicename'])[0]==LD.newvideo['devicename']#设备名称校验正确
            R_log.info("*******{0}测试用例执行成功******".format(LD.newvideo['casename']))
        except Exception as e:
            P_log.info("*******{0}测试用例执行失败******".format(LD.newvideo['casename']))
            R_log.info("*******{0}测试用例执行失败，失败原因{1}******".format(LD.newvideo['casename'],e))
            raise e


    @pytest.mark.smoke
    def test_modifyvido(self,login_web): # 修改视频流相机
        First_Page(login_web).manager(3, 'camera')
        P_log.info("*******开始执行【编辑视频流相机】测试用例******")
        Camera(login_web).modifyvideo(LD.newvideo['devicename'],LD.newvideo['SN'])
        try:
            P_log.info("*******开始执行【编辑视频流相机】测试用例结果校验******")
            assert Camera(login_web).getinfo(LD.newvideo['devicename'])[1] == LD.newvideo['SN']#设备SN码校验正确
            R_log.info("*******【编辑视频流相机】测试用例执行成功******")
        except Exception as e:
            P_log.info("*******【编辑视频流相机】测试用例执行失败******")
            R_log.info("*******【编辑视频流相机】测试用例执行失败,失败原因{0}******".format(e))
            raise e

    def test_newcapture_ftp(self,login_web):#新增智能抓拍机/ftp
        pass

    @pytest.mark.smoke
    def test_newcapture_ga1400(self,login_web):#新增智能抓拍机/ga1400
        First_Page(login_web).manager(3,'camera')
        P_log.info("*******开始执行【{0}】测试用例******".format(LD.newcapture_ga1400['casename']))
        Camera(login_web).newcapturega1400(LD.newcapture_ga1400['devicename'])
        try:
            P_log.info("*******开始执行【{0}】测试用例结果校验******".format(LD.newcapture_private['casename']))
            assert Camera(login_web).getinfo(LD.newcapture_ga1400['devicename'])[0] == LD.newcapture_ga1400['devicename']  # 设备名称校验正确
            R_log.info("*******【{0}】测试用例执行成功******".format(LD.newcapture_ga1400['casename']))
        except Exception as e:
            P_log.info("*******【{0}】测试用例执行失败******".format(LD.newcapture_ga1400['casename']))
            R_log.info("*******【{0}】测试用例执行失败，失败原因{1}******".format(LD.newcapture_ga1400['casename'], e))

    @pytest.mark.smoke
    def test_newcapture_private(self,login_web):#新增智能抓拍机/澎思私有协议
        First_Page(login_web).manager(3, 'camera')
        P_log.info("*******开始执行【{0}】测试用例******".format(LD.newcapture_private['casename']))
        Camera(login_web).newcaptureprivate(LD.newcapture_private['devicename'])
        try:
            P_log.info("*******开始执行【{0}】测试用例结果校验******".format(LD.newcapture_private['casename']))
            assert Camera(login_web).getinfo(LD.newcapture_private['devicename'])[0] == LD.newcapture_private[
                'devicename']  # 设备名称校验正确
            R_log.info("*******【{0}】测试用例执行成功******".format(LD.newcapture_private['casename']))
        except Exception as e:
            P_log.info("*******【{0}】测试用例执行失败******".format(LD.newcapture_private['casename']))
            R_log.info("*******【{0}】测试用例执行失败，失败原因{1}******".format(LD.newcapture_private['casename'], e))

    def test_modifycapture_ftp(self,login_web):#修改智能抓拍机/ftp
        pass

    def test_modifycapture_ga1400(self,login_web):#修改智能抓拍机/ga1400
        pass

    def test_modifycapture_private(self,login_web):#修改智能抓拍机/澎思私有协议
        pass

    @pytest.mark.smoke
    def test_newGB(self,login_web):#新增GB实时
        First_Page(login_web).manager(3, 'camera')
        P_log.info("*******开始执行【{0}】测试用例******".format(LD.newGB['casename']))
        Camera(login_web).newgb(LD.newGB['devicename'])
        try:
            P_log.info("*******开始执行【{0}】测试用例结果校验******".format(LD.newGB['casename']))
            assert Camera(login_web).getinfo(LD.newGB['devicename'])[0] == LD.newGB['devicename']  # 设备名称校验正确

            R_log.info("*******【{0}】测试用例执行成功******".format(LD.newGB['casename']))
        except Exception as e:
            P_log.info("*******【{0}】测试用例执行失败******".format(LD.newGB['casename']))
            R_log.info("*******【{0}】测试用例执行失败，失败原因{1}******".format(LD.newGB['casename'], e))

    def test_modifyGB(self,login_web):#修改GB实时
        pass

    @pytest.mark.smoke
    def test_delvideo(self,login_web):# 删除相机
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