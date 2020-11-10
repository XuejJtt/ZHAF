#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/14 14:55
# @File    : test_resource.py
# @Software: PyCharm

import pytest
from Common.log import Log
from Common import dir_config
from PageObjects.index.first_page import First_Page
import time
from TestDatas.辖区总览 import resource_data as T
from Common.Compare import GraphicalLocator as G

P_log = Log(dir_config.processlog_dir)
R_log = Log(dir_config.resultlog_dir)


@pytest.mark.usefixtures("login_web")
class Test_resource:

    @pytest.mark.somke
    def test_sum_resource(self,login_web):
        self.test_sum_resource.__func__.__doc__ = T.sum_resource['dec']
        P_log.info("*******开始执行{0}测试用例******".format(T.sum_resource['name']))
        sum_resource = First_Page(login_web).get_resouce_num('资源总数').replace(',','')
        sum_face = First_Page(login_web).get_resouce_num('人脸').replace(',','')
        sum_body = First_Page(login_web).get_resouce_num('人体').replace(',','')
        sum_vehcle = First_Page(login_web).get_resouce_num('机动车').replace(',','')
        sum_novehcle = First_Page(login_web).get_resouce_num('非机动车').replace(',','')
        try:
            P_log.info("*******开始进行结果校验*********")
            assert int(sum_resource) == int(sum_body)+int(sum_face)+int(sum_vehcle)+int(sum_novehcle)
            R_log.info("{0}用例执行成功".format(T.sum_resource['name']))
        except Exception as e:
            R_log.info("{0}用例执行失败".format(T.sum_resource['name']))
            P_log.error("{0}用例失败原因:{1}".format(T.sum_resource['name'], e))
            First_Page(login_web).save_picture('用例异常截图')
            raise e

    @pytest.mark.somke
    def test_resource_7days(self,login_web):
        self.test_resource_7days.__func__.__doc__ = T.resource_7days['dec']
        P_log.info("*******开始执行{0}测试用例******".format(T.resource_7days['name']))
        try:
            人脸 = First_Page(login_web).get_text(First_Page.face_number)
            人体 = First_Page(login_web).get_text(First_Page.body_number)
            机动车 = First_Page(login_web).get_text(First_Page.car_number)
            非机动车 = First_Page(login_web).get_text(First_Page.uncar_number)
            P_log.info("资源统计下人脸的数量是:{0}".format(人脸))
            P_log.info("资源统计下人体的数量是:{0}".format(人体))
            P_log.info("资源统计下机动车的数量是:{0}".format(机动车))
            P_log.info("资源统计下非机动车的数量是:{0}".format(非机动车))
            R_log.info("{0}用例执行成功".format(T.resource_7days['name']))
        except Exception as e:
            R_log.info("{0}用例执行失败".format(T.resource_7days['name']))
            P_log.error("{0}用例失败原因:{1}".format(T.resource_7days['name'], e))
            First_Page(login_web).save_picture('用例异常截图')
            raise e

    @pytest.mark.somke
    def test_resource_total(self,login_web,flag=True):
        self.test_resource_total.__func__.__doc__ = T.resource_total['dec']
        P_log.info("*******开始执行{0}测试用例******".format(T.resource_total['name']))
        try:
            First_Page(login_web).select_laber('资源统计','累计')
            R_log.info("{0}用例执行成功".format(T.resource_total['name']))
            time.sleep(3)
        except Exception as e:
            R_log.info("{0}用例执行失败".format(T.resource_total['name']))
            P_log.error("{0}用例失败原因:{1}".format(T.resource_total['name'], e))
            First_Page(login_web).save_picture('用例异常截图')
            raise e

    @pytest.mark.somke
    def test_devices_total(self,login_web):
        self.test_devices_total.__func__.__doc__ = T.devices_total['dec']
        P_log.info("*******开始执行{0}测试用例******".format(T.devices_total['name']))
        try:
            设备总数 = First_Page(login_web).get_text(First_Page.allnumber)
            视频流相机 = First_Page(login_web).get_text(First_Page.视频流相机总数)
            智能抓拍机 = First_Page(login_web).get_text(First_Page.智能抓拍相机总数)
            GB28181 = First_Page(login_web).get_text(First_Page.GB28181_sum)
            视图库 = First_Page(login_web).get_text(First_Page.视图库总数)
            assert int(设备总数) == int(视频流相机) + int(智能抓拍机) + int(GB28181) + int(视图库)
        except Exception as e:
            R_log.info("{0}用例执行失败".format(T.devices_total['name']))
            P_log.error("{0}用例失败原因:{1}".format(T.devices_total['name'], e))
            First_Page(login_web).save_picture('用例异常截图')
            raise e

    @pytest.mark.somke
    def test_devices_online(self,login_web):
        self.test_devices_online.__func__.__doc__ = T.devices_online['dec']
        P_log.info("*******开始执行{0}测试用例******".format(T.devices_online['name']))
        try:
            First_Page(login_web).select_laber('设备总览','在线')
            top_number = First_Page(login_web).get_text(First_Page.top_number)
            视屏流相机在线 = First_Page(login_web).get_text(First_Page.视频流相机在线)
            智能抓拍机在线 = First_Page(login_web).get_text(First_Page.智能抓拍机相机在线)
            GB28181 = First_Page(login_web).get_text(First_Page.GB28181_online)
            视图库在线 = First_Page(login_web).get_text(First_Page.视图库在线)

        except Exception as e:
            R_log.info("{0}用例执行失败".format(T.devices_online['name']))
            P_log.error("{0}用例失败原因:{1}".format(T.devices_online['name'], e))
            First_Page(login_web).save_picture('用例异常截图')
            raise e

    @pytest.mark.somke
    def test_archives_statistics(self,login_web):
        self.test_archives_statistics.__func__.__doc__ = T.archives_statistics['dec']
        P_log.info("*******开始执行{0}测试用例******".format(T.archives_statistics['name']))
        try:
            人员档案 = First_Page(login_web).get_text(First_Page.人员档案)
            场所档案 = First_Page(login_web).get_text(First_Page.场所档案)
            车辆档案 = First_Page(login_web).get_text(First_Page.车辆档案)
            设备档案 = First_Page(login_web).get_text(First_Page.设备档案)
        except Exception as e:
            R_log.info("{0}用例执行失败".format(T.archives_statistics['name']))
            P_log.error("{0}用例失败原因:{1}".format(T.archives_statistics['name'], e))
            First_Page(login_web).save_picture('用例异常截图')
            raise e

    @pytest.mark.somke
    def test_monitor_statistics(self,login_web):
        self.test_monitor_statistics.__func__.__doc__ = T.monitor_statistics['dec']
        P_log.info("*******开始执行{0}测试用例******".format(T.monitor_statistics['name']))
        try:
            人脸布控 = First_Page(login_web).get_text(First_Page.人脸布控)
            人体布控 = First_Page(login_web).get_text(First_Page.人体布控)
            机动车布控 = First_Page(login_web).get_text(First_Page.机动车布控)
        except Exception as e:
            R_log.info("{0}用例执行失败".format(T.monitor_statistics['name']))
            P_log.error("{0}用例失败原因:{1}".format(T.monitor_statistics['name'], e))
            First_Page(login_web).save_picture('用例异常截图')
            raise e

    @pytest.mark.somke
    def test_alarm_7days(self,login_web):
        self.test_alarm_7days.__func__.__doc__ = T.alarm_7days['dec']
        P_log.info("*******开始执行{0}测试用例******".format(T.alarm_7days['name']))
        try:
            First_Page(login_web).select_laber('告警统计', '累计')
            告警统计7天人脸 = First_Page(login_web).get_text(First_Page.告警统计7天人脸)
            告警统计7天人体 = First_Page(login_web).get_text(First_Page.告警统计7天人体)
            告警统计7天机动车 = First_Page(login_web).get_text(First_Page.告警统计7天机动车)
        except Exception as e:
            R_log.info("{0}用例执行失败".format(T.alarm_7days['name']))
            P_log.error("{0}用例失败原因:{1}".format(T.alarm_7days['name'], e))
            First_Page(login_web).save_picture('用例异常截图')
            raise e

    @pytest.mark.somke
    def test_alarm_total(self,login_web):
        self.test_alarm_total.__func__.__doc__ = T.alarm_total['dec']
        P_log.info("*******开始执行{0}测试用例******".format(T.alarm_total['name']))
        try:
            First_Page(login_web).select_laber('告警统计', '累计')
            告警统计累计人脸 = First_Page(login_web).get_text(First_Page.告警统计累计人脸)
            告警统计累计人体 = First_Page(login_web).get_text(First_Page.告警统计累计人体)
            告警统计累计机动车 = First_Page(login_web).get_text(First_Page.告警统计累计机动车)
        except Exception as e:
            R_log.info("{0}用例执行失败".format(T.alarm_total['name']))
            P_log.error("{0}用例失败原因:{1}".format(T.alarm_total['name'], e))
            First_Page(login_web).save_picture('用例异常截图')
            raise e

    @pytest.mark.somke
    def test_alarm_top5_7days(self,login_web):
        self.test_alarm_top5_7days.__func__.__doc__ = T.top5_7dayas['dec']
        P_log.info("*******开始执行{0}测试用例******".format(T.top5_7dayas['name']))
        try:
            会议室门 = First_Page(login_web).get_text(First_Page.小会议室)
            ymq = First_Page(login_web).get_text(First_Page.ymq)
            门口走廊 = First_Page(login_web).get_text(First_Page.门口走廊)
        except Exception as e:
            R_log.info("{0}用例执行失败".format(T.top5_7dayas['name']))
            P_log.error("{0}用例失败原因:{1}".format(T.top5_7dayas['name'], e))
            First_Page(login_web).save_picture('用例异常截图')
            raise e

    @pytest.mark.somke
    def test_alarm_top5_sum(self, login_web):
        self.test_alarm_top5_sum.__func__.__doc__ = T.top5_sum['dec']
        P_log.info("*******开始执行{0}测试用例******".format(T.top5_sum['name']))
        try:
            First_Page(login_web).select_laber('点位告警', '累计')
            会议室门 = First_Page(login_web).get_text(First_Page.小会议室累计)
            ymq = First_Page(login_web).get_text(First_Page.ymq_sum)
            门口走廊 = First_Page(login_web).get_text(First_Page.门口走廊累计)
        except Exception as e:
            R_log.info("{0}用例执行失败".format(T.top5_sum['name']))
            P_log.error("{0}用例失败原因:{1}".format(T.top5_sum['name'], e))
            First_Page(login_web).save_picture('用例异常截图')
            raise e



    @pytest.mark.parametrize('data',T.resource_select)
    @pytest.mark.somke
    def test_resource_select(self,login_web,data):
        self.test_resource_select.__func__.__doc__ = data['dec']
        P_log.info("*******开始执行{0}测试用例******".format(data['name']))
        try:
            First_Page(login_web).click(First_Page.资源按钮)
            time.sleep(1)
            d = First_Page.__dict__
            # 字典解析式
            dic = {key:d[key] for key in d if "_" not in d}
            First_Page(login_web).click(dic[data['object']])
            #图像比对
            src = First_Page(login_web).save_picture('src')
            time.sleep(1)
            res = G(data['pic']).find_and_check(src)
            assert res

        except Exception as e:
            R_log.info("{0}用例执行失败".format(data['name']))
            P_log.error("{0}用例失败原因:{1}".format(data['name'], e))
            First_Page(login_web).save_picture('用例异常截图')
            raise e


