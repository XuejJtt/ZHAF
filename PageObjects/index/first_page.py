#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 14:20
# @Author  : Xuej
# @File    : first_page.py
# @Software: PyCharm
from Common.BasePage import *
from Common.log import Log
from Common.dir_config import *
from selenium.webdriver.common.by import By
import time

# 定义resultlog和processlog
P_log = Log(processlog_dir)
R_log = Log(resultlog_dir)


class First_Page(BasePage):
    # 首页当前用户名
    username = '//span[@class="username"]'
    # 首页管理图标
    mager = 'i[class="menu-icon anticon anticon-setting"]'
    # 管理下的子菜单
    sysmager = '.icon-title'
    # 边缘智能选择按钮
    edgeIntelligence = '(//i[@class="anticon"])[2]'
    # 解析管理选择按钮
    analytical = '(//i[@class="anticon"])[3]'
    # 资源图库
    gallery = '//span[contains(text(),"资源图库")]/parent::span'
    # 人脸图库
    face = '//li[contains(text(),"人脸图库")]'
    # 人体
    body = '//li[contains(text(),"人体图库")]'
    # 机动车
    vehicle = '//li[contains(text(),"机动车图库")]'
    # 非机动车
    nonmotor = '//li[contains(text(),"非机动车图库")]'
    # 对象图谱
    objectMap = '//span[contains(text(),"对象图谱")]/parent::span'
    # 人员档案
    person = '//li[contains(text(),"人员档案")]'
    # 车辆档案
    map_vehcle = '//li[contains(text(),"车辆档案")]'
    # 场所档案
    place = '//li[contains(text(),"场所档案")]'
    # 设备档案
    device = '//li[contains(text(),"设备档案")]'
    # 综合布控
    deployment = '//span[contains(text(),"综合布控")]/parent::span'
    # 底库管理
    library = '//li[contains(text(),"底库管理")]'
    # 布控管理
    surveillance = '//li[contains(text(),"布控管理")]'
    # 告警历史
    alarm = '//li[contains(text(),"告警历史")]'
    # 抓获撤销库
    alarmhandle = '//li[contains(text()," 抓获撤销库 ")]'
    # 技战法
    technicalTactics = '//span[contains(text(),"技战法")]/parent::span'
    # 1V1对比
    versus = '//li[contains(text(),"1v1比对")]'
    # 身份鉴别
    identityAuthentication = 'identityAuthentication'
    # 视屏串并
    videoSeriesParallel = '//li[contains(text(),"视频串并")]'
    # 跨境追踪
    crossBorderTrack = '//li[contains(text(),"跨镜追踪")]'
    # 资源总数
    sum_resources = '//span[contains(text(),"资源总数")]/following-sibling::span'
    # 非机动车数量
    sum_novehcile = '//span[contains(text(),"非机动车")]/following-sibling::span'
    # 机动车数量
    sum_vehcile = '//span[contains(text(),"机动车")]/following-sibling::span'
    # 人脸数量
    sum_face = '//span[contains(text(),"人脸")]/following-sibling::span'
    # 人体数量
    sum_body = '//span[contains(text(),"人体")]/following-sibling::span'
    # 7天标签
    resource_7 = '(//span[contains(text(),"7天")])[1]'
    capture_7 = '(//span[contains(text(),"7天")])[2]'
    alarm_7 = '(//span[contains(text(),"7天")])[3]'
    point_7 = '(//span[contains(text(),"7天")])[4]'
    devices_statistics = '(//span[contains(text(),"统计")])[1]'
    devices_online = '//span[contains(text(),"在线")]'
    二十四小时 = '//span[contains(text(),"24小时")]'
    # 累计标签
    resource_sum = '(//span[contains(text(),"累计")])[1]'
    alarm_sum = '(//span[contains(text(),"累计")])[2]'
    point_sum = '(//span[contains(text(),"累计")])[3]'
    # 资源统计7天下的对象
    face_number = '//div[@class ="face-number"]'
    body_number = '//span[@class ="body-number"]'
    car_number = '//span[@class ="car-number"]'
    uncar_number = '//span[@class="uncar-number"]'

    # 资源统计累计下的对象

    # 设备总览下的对象
    allnumber = '//div[@class="allNumber"]'
    视频流相机总数 = '(//span[@class="page-equipment-body-count"])[1]'
    智能抓拍相机总数 = '(//span[@class="page-equipment-body-count"])[2]'
    GB28181_sum = '(//span[@class="page-equipment-body-count"])[3]'
    视图库总数 = '(//span[@class="page-equipment-body-count"])[4]'
    top_number = '//div[@class="top-num"]'
    视频流相机在线 = '(//span[@class="page-equipment-body-count"])[5]'
    智能抓拍机相机在线 = '(//span[@class="page-equipment-body-count"])[6]'
    GB28181_online = '(//span[@class="page-equipment-body-count"])[7]'
    视图库在线 = '(//span[@class="page-equipment-body-count"])[8]'

    # 档案统计下的对象
    人员档案 = '(//div[@class="archives-number"])[1]'
    场所档案 = '(//div[@class="archives-number"])[3]'
    车辆档案 = '(//div[@class="archives-number"])[2]'
    设备档案 = '(//div[@class="archives-number"])[4]'

    # 布控统计下的对象
    人脸布控 = '(//span[@class="face-legend"])[1]//following-sibling::span'
    人体布控 = '(//span[@class="body-legend"])[1]//following-sibling::span'
    机动车布控 = '(//span[@class="vehicle-legend"])[1]//following-sibling::span'

    # 告警统计下的对象
    告警统计7天人脸 = '(//span[@class="face-legend"])[2]//following-sibling::span'
    告警统计7天人体 = '(//span[@class="body-legend"])[2]//following-sibling::span'
    告警统计7天机动车 = '(//span[@class="vehicle-legend"])[2]//following-sibling::span'
    告警统计累计人脸 = '(//span[@class="face-legend"])[3]//following-sibling::span'
    告警统计累计人体 = '(//span[@class="body-legend"])[3]//following-sibling::span'
    告警统计累计机动车 = '(//span[@class="vehicle-legend"])[3]//following-sibling::span'

    # 点位告警top5下的对象
    ymq = '(//span[contains(text(),"ymq")])[1]/following-sibling::span'
    小会议室 = '(//span[contains(text(),"小会议室门上")])[1]/following-sibling::span'
    门口走廊 = '(//span[contains(text(),"门口内部走廊")])[1]/following-sibling::span'

    ymq_sum = '(//span[contains(text(),"ymq")])[2]/following-sibling::span'
    小会议室累计 = '(//span[contains(text(),"小会议室门上")])[2]/following-sibling::span'
    门口走廊累计 = '(//span[contains(text(),"门口内部走廊")])[2]/following-sibling::span'


    # 资源下的对象
    资源按钮 = '//div[@style="cursor: pointer;"]'
    视屏流相机 = '//div[contains(text(),"视频流相机")]'
    智能抓拍机 = '//div[contains(text(),"智能抓拍机")]'
    GB28181相机 = '//div[contains(text(),"GB28181")]'
    视图库相机 = '//div[contains(text(),"视图库")]'
    在线 = '(//button)[1]'
    离线 = '(//button)[2]'

    地图背景 = '//div[contains(text(),"地图背景")]'
    poi = '//div[contains(text(),"POI")]'
    道路 = '//div[contains(text(),"道路")]'
    行政标注 = '//div[contains(text(),"行政标注")]'


    # 获取登录后的用户名
    def get_login_name(self):
        return self.get_text(self.username)

    # 点击进入系统管理下的子菜单
    def manager(self, num, t):
        P_log.info('点击进入系统管理下的子菜单')
        self.move_mouse(self.mager)  # 鼠标悬停在管理上
        # self.find_elements(self.sysmager)[num].click()  # 点击管理下边的元素进入系统管理
        self.clicks(self.sysmager, By.CSS_SELECTOR, 40, 'visible', num)  # 点击管理下边的元素进入系统管理
        for handle in self.driver.window_handles:  # 获取当前浏览器所有窗口句柄
            self.driver.switch_to.window(handle)  # 得到该窗口的标题栏字符串
            if t in self.driver.title:  # 判断当前窗口是否包含该字符串，如果是，跳出循环
                break

    # 获取资源总数数值
    def get_resouce_num(self, loc):
        if loc == '资源总数':
            return self.get_text(self.sum_resources)
        elif loc == '人脸':
            return self.get_text(self.sum_face)
        elif loc == '人体':
            return self.get_text(self.sum_body)
        elif loc == '机动车':
            return self.get_text(self.sum_vehcile)
        elif loc == '非机动车':
            return self.get_text(self.sum_novehcile)

    # 切换标签
    def select_laber(self, F, S):
        list_1 = ['资源统计', '设备总览', '抓拍趋势', '告警统计', '点位告警']
        list_2 = ['7天', '累计', '在线', '统计', '24小时']
        if F not in list_1:
            P_log.error('一级菜单不在支持列表中')
            raise ValueError('一级菜单不支持')
        if S not in list_2:
            P_log.error('二级菜单不在支持列表中')
            raise ValueError('二级菜单不支持')
        if F == '资源统计':
            if S == '7天':
                self.click(self.resource_7)
            elif S == '累计':
                self.click(self.resource_sum)
        if F == '设备总览':
            if S == '统计':
                self.click(self.devices_statistics)
            elif S == '在线':
                self.click(self.devices_online)
        if F == '抓拍趋势':
            if S == '7天':
                self.click(self.capture_7)
            elif S == '24小时':
                self.click(self.二十四小时)
        if F == '告警统计':
            if S == '7天':
                self.click(self.alarm_7)
            elif S == '累计':
                self.click(self.alarm_sum)
        if F == '点位告警':
            if S == '7天':
                self.click(self.point_7)
            elif S == '累计':
                self.click(self.point_sum)

    # 选择主菜单,针对解析管理，边缘智能，单功能的菜单
    def select_item(self, loc):
        """
        @param loc: 需要选择的主菜单
        """
        P_log.info('开始选择系统菜单{0}'.format(loc))
        if loc == '边缘智能':
            self.click(self.edgeIntelligence)
        elif loc == '解析管理':
            self.click(self.analytical)

    # 选择二级菜单
    def select_s_item(self, loc, loc_s):
        P_log.info('开始进入{0}菜单下的{1}子菜单'.format(loc, loc_s))
        if loc == '资源图库':
            self.move_mouse(self.gallery)
            if loc_s == '人脸图库':
                self.click(self.face)
            elif loc_s == '人体':
                self.click(self.body)
            elif loc_s == '机动车':
                self.click(self.vehicle)
            elif loc_s == '非机动车':
                self.click(self.nonmotor)
        elif loc == '对象图谱':
            self.move_mouse(self.objectMap)
            if loc_s == '人员档案':
                self.click(self.person)
            elif loc_s == '车辆档案':
                self.click(self.map_vehcle)
            elif loc_s == '场所档案':
                self.click(self.place)
            elif loc_s == '设备档案':
                self.click(self.device)
        elif loc == '综合布控':
            self.move_mouse(self.deployment)
            if loc_s == '底库管理':
                self.click(self.library)
            elif loc_s == '布控管理':
                self.click(self.surveillance)
            elif loc_s == '告警历史':
                self.click(self.alarm)
            elif loc_s == '抓获撤销库':
                self.click(self.alarmhandle)
        elif loc == '技战法':
            self.move_mouse(self.technicalTactics)
            if loc_s == '1V1对比':
                self.click(self.versus)
            elif loc_s == '身份鉴别':
                self.click(self.identityAuthentication)
            elif loc_s == '视屏串并':
                self.click(self.videoSeriesParallel)
            elif loc_s == '跨境追踪':
                self.click(self.crossBorderTrack)
