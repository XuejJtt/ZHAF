#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 14:20
# @Author  : Xuej
# @File    : first_page.py
# @Software: PyCharm
from Common.BasePage import BasePage
from Common.log import Log
from Common.dir_config import *
from selenium.webdriver.common.by import By
import time

#定义resultlog和processlog
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
    edgeIntelligence = '//li[@class=''special ant-menu-item''][1]'
    # 解析管理选择按钮
    analytical = '//li[@class=''special ant-menu-item''][2]'
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

    # 获取登录后的用户名
    def get_login_name(self):
        return self.get_text(self.username)

    def manager(self,num, t):
        P_log.info('点击进入系统管理下的子菜单')
        self.move_mouse(self.mager)  # 鼠标悬停在管理上
        # self.find_elements(self.sysmager)[num].click()  # 点击管理下边的元素进入系统管理
        self.clicks(self.sysmager,By.CSS_SELECTOR,40,'visible',num) # 点击管理下边的元素进入系统管理
        for handle in self.driver.window_handles:  # 获取当前浏览器所有窗口句柄
            self.driver.switch_to.window(handle)  # 得到该窗口的标题栏字符串
            if t in self.driver.title:  # 判断当前窗口是否包含该字符串，如果是，跳出循环
                break

    # 选择主菜单,针对解析管理，边缘智能，单功能的菜单
    def select_item(self,loc):
        """
        @param loc: 需要选择的主菜单
        """
        P_log.info('开始选择系统菜单{0}'.format(loc))
        if loc =='边缘智能':
            self.click(self.edgeIntelligence)
        elif loc =='解析管理':
            self.click(self.analytical)


    # 选择二级菜单
    def select_s_item(self,loc,loc_s):
        P_log.info('开始进入{0}菜单下的{1}子菜单'.format(loc,loc_s))
        if loc =='资源图库':
            self.move_mouse(self.gallery)
            if loc_s=='人脸图库':
                pass
            elif loc_s=='人体':
                pass
            elif loc_s=='机动车':
                pass
            elif loc_s=='非机动车':
                pass
        elif loc =='对象图谱':
            self.move_mouse(self.objectMap)
            if loc_s=='人员档案':
                pass
            elif loc_s=='车辆档案':
                pass
            elif loc_s=='场所档案':
                pass
            elif loc_s=='设备档案':
                pass
        elif loc =='综合布控':
            self.move_mouse(self.deployment)
            if loc_s=='底库管理':
                pass
            elif loc_s=='布控管理':
                pass
            elif loc_s=='告警历史':
                pass
            elif loc_s=='抓获撤销库':
                pass
        elif loc =='技战法':
            self.move_mouse(self.technicalTactics)
            if loc_s=='1V1对比':
                pass
            elif loc_s=='身份鉴别':
                pass
            elif loc_s=='视屏串并':
                pass
            elif loc_s=='跨境追踪':
                pass



