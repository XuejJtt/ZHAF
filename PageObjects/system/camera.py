#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author : Zhuzj
# @file : camera.py
# @time : 2020/9/10 16:35
# @Software :PyCharm

from Common.BasePage import *


class Camera(BasePage):
    area = '//i[@class="anticon anticon-caret-down ant-tree-switcher-icon"]'  # 左侧组织下拉列表
    node = '//span[@class="ant-tree-node-content-wrapper ant-tree-node-content-wrapper-normal"]'  # 下拉列表子节点
    addbt = '//span[text()="新增设备"]/..'  # 新增设备按钮
    dtype = '//div[@class="device-type-icon"]'  # 设备类型，0： 视频流相机，1： 智能抓拍机， 2： GB实时，3： 1400视图库
    nextbt = '//span[text()="下一步"]/..'  # 下一步按钮
    devicename = '//span/*[@placeholder = "请输入设备名称"]'  # 设备名称
    deviceadress = '//span/*[@placeholder = "请输入视频流地址"]'  # 视频流地址
    longitude = '//input[@placeholder = "请输入经度"]'  # 经度
    latitude = '//input[@placeholder = "请输入纬度"]'  # 纬度
    confirm = '//span[text()="确 认"]/..'  # 确认按钮
    SN='//span/*[@placeholder = "请输入SN码"]'#SN码输入框
    search='//input[@placeholder ="请输入设备名称/SN"]'#设备名称搜索框
    getname='//td[@class="ant-table-row-cell-ellipsis"]'#列表设备名称字段
    getSN='//tr[@class="ant-table-row ant-table-row-level-0"]/td[4]'#列表SN码字段
    delt='//span[text()="删除"]/..'#删除文字链接
    modify='//span[text()="编辑"]/..'#编辑文字链接
    nodata='//p[@class="ant-empty-description"]'#查询无数据



    def newvideo(self, devicename, deviceadress, longitude, latitude):
        self.clicks(self.area)  # 点击左侧组织下拉列表
        self.clicks(self.node)  # 选择下拉列表第一个子节点
        self.click(self.addbt)  # 点击新增设备按钮
        self.click(self.dtype)  # 设备类型 选择第一个：视频流相机
        self.click(self.nextbt)  # 点击下一步按钮
        self.input_text(self.devicename, devicename)  # 输入设备名称
        self.input_text(self.deviceadress, deviceadress)  # 输入视频流地址
        self.input_text(self.longitude, longitude)  # 输入经度
        self.input_text(self.latitude, latitude)  # 输入纬度
        self.click(self.nextbt)  # 点击下一步按钮
        self.click(self.confirm)  # 点击确认按钮
        time.sleep(2)
    #修改
    def modifyvideo(self,devicename,sn):
        self.input_text(self.search, devicename)  # 查询输入框输入设备名称
        self.click(self.modify)#点击编辑按钮
        time.sleep(2)
        self.click(self.nextbt)  # 点击下一步按钮
        self.input_text(self.SN,sn)#输入sn码
        self.click(self.confirm)  # 点击确认按钮
        time.sleep(2)

    def delvideo(self,devicename):
        self.input_text(self.search,devicename)#查询输入框输入设备名称
        self.click(self.delt)#点击删除按钮
        self.click(self.confirm)#点击确认按钮
        time.sleep(2)


    def getinfo(self,devicename):
        em = self.find_element(self.search)
        em.send_keys(Keys.CONTROL, 'a')  # 模拟键盘操作，输入ctrl+A全选
        self.input_text(self.search,devicename)#查询输入框输入设备名称
        dn=self.get_text_m(self.getname)#获取设备名称字段
        sn=self.get_text_m(self.getSN)#获取设备SN码字段
        list=[]
        list.append(dn)
        list.append(sn)
        return list





    def getnodata(self,devicename):
        em = self.find_element(self.search)
        em.send_keys(Keys.CONTROL, 'a')  # 模拟键盘操作，输入ctrl+A全选
        self.input_text(self.search,devicename)#查询输入框输入设备名称
        return  self.get_text(self.nodata)#查询无数据校验

