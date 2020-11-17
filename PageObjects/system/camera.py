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

    #视频流相机
    devicename = '//span/*[@placeholder = "请输入设备名称"]'  # 设备名称
    deviceadress = '//span/*[@placeholder = "请输入视频流地址"]'  # 视频流地址
    longitude = '//input[@placeholder = "请输入经度"]'  # 经度
    latitude = '//input[@placeholder = "请输入纬度"]'  # 纬度
    confirm = '//span[text()="确 认"]/..'  # 确认按钮

    # 智能抓拍机
    accessmode = '.ant-form-item-control .ant-select-enabled .ant-select-selection__rendered'  # 接入方式
    modeselect = '//ul[@role="listbox"]/li'  # 接入方式下拉选择 0:ftp  1:ga1400  2:澎思私有协议
    ftpadress = '//input[@placeholder = "请输入FTP地址"]'  # FTP地址
    port = '//input[@placeholder = "请输入端口"]'  # 端口
    usname = '//input[@placeholder = "请输入用户名"]'  # 用户名
    pwd = '//*[@title="密码"]/../following-sibling::*//input'  # 密码
    filepath='//*[@title="文件路径"]/../following-sibling::*//input'#文件路径
    salveIP = '//input[@placeholder = "请输入接入服务器salveIP"]'  # salveIP
    deviceid = '//input[@placeholder = "请输入设备id"]'  # 设备id
    Streamaddress = '//input[@placeholder = "请输入预览流地址"]'  # 预览流地址
    brand = '//div[text()="请选择品牌"]'  # 品牌下拉框
    brandselect = '//li[@class="ant-select-dropdown-menu-item ant-select-dropdown-menu-item-active"]'  # 选择品牌
    mac = '//input[@placeholder = "请输入Mac地址"]'  # mac地址

    # GB实时
    gbnum = '//input[@placeholder = "请输入视频GB编号"]'  # GB编号
    gbaddress = '//input[@placeholder = "请输入GB平台地址"]'  # GB平台地址
    gbid = '//input[@placeholder = "请输入GB平台ID"]'  # GB平台ID
    gbport = '//input[@placeholder = "请输入GB平台端口"]'  # GB平台端口

    #获取页面列表字段
    SN='//span/*[@placeholder = "请输入SN码"]'#SN码输入框
    search='//input[@placeholder ="请输入设备名称/SN"]'#设备名称搜索框
    getname='//td[@class="ant-table-row-cell-ellipsis"]'#列表设备名称字段
    getSN='//tr[@class="ant-table-row ant-table-row-level-0"]/td[4]'#列表SN码字段
    nodata = '//p[@class="ant-empty-description"]'  # 查询无数据

    #操作按钮
    delt='//span[text()="删除"]/..'#删除文字链接
    modify='//span[text()="编辑"]/..'#编辑文字链接


    def newvideo(self, devicename, deviceadress):#新增视频流相机
        self.clicks(self.area)  # 点击左侧组织下拉列表
        self.clicks(self.node)  # 选择下拉列表第一个子节点
        self.click(self.addbt)  # 点击新增设备按钮
        self.click(self.dtype)  # 设备类型 选择第一个：视频流相机
        self.click(self.nextbt)  # 点击下一步按钮
        self.input_text(self.devicename, devicename)  # 输入设备名称
        self.input_text(self.deviceadress, deviceadress)  # 输入视频流地址
        self.input_text(self.longitude, "12")  # 输入经度
        self.input_text(self.latitude, '15')  # 输入纬度
        self.click(self.nextbt)  # 点击下一步按钮
        self.click(self.confirm)  # 点击确认按钮
        time.sleep(2)

    def modifyvideo(self,devicename,sn):#修改视频流相机
        self.input_text(self.search, devicename)  # 查询输入框输入设备名称
        self.click(self.modify)#点击编辑按钮
        time.sleep(2)
        self.click(self.nextbt)  # 点击下一步按钮
        self.input_text(self.SN,sn)#输入sn码
        self.click(self.confirm)  # 点击确认按钮
        time.sleep(2)

    def delvideo(self,devicename):#删除
        self.input_text(self.search,devicename)#查询输入框输入设备名称
        self.click(self.delt)#点击删除按钮
        self.click(self.confirm)#点击确认按钮
        time.sleep(2)


    def newcaptureftp(self,devicename):#新增智能抓拍机/ftp
        self.clicks(self.area)  # 点击左侧组织下拉列表
        self.clicks(self.node)  # 选择下拉列表第一个子节点
        self.click(self.addbt)  # 点击新增设备按钮
        self.clicks(self.dtype,index=1)# 设备类型 选择第一个：智能抓拍机
        self.click(self.nextbt)  # 点击下一步按钮
        self.click(self.accessmode,By.CSS_SELECTOR)#点击接入方式下拉框
        self.clicks(self.modeselect) #选择第一个：ftp
        self.input_text(self.devicename,devicename)#输入设备名称
        self.input_text(self.ftpadress,'10.10.1.122')#输入ftp地址
        self.input_text(self.port,'80')#输入端口号
        self.input_text(self.usname,'admin',type="invisible",scroll=True)#输入用户名
        self.input_text(self.pwd,'password')#输入密码
        self.input_text(self.filepath,'/test/face/camera')#输入文件路径
        self.input_text(self.longitude, "12")  # 输入经度
        self.input_text(self.latitude, '15')  # 输入纬度
        self.click(self.nextbt)  # 点击下一步按钮
        self.click(self.confirm)  # 点击确认按钮
        time.sleep(2)

    def modifyftp(self,devicename,sn):#修改ftp智能抓拍机sn字段
        self.input_text(self.search, devicename)  # 查询输入框输入设备名称
        self.click(self.modify)  # 点击编辑按钮
        time.sleep(2)
        self.click(self.nextbt)  # 点击下一步按钮
        self.input_text(self.SN, sn)  # 输入sn码
        self.click(self.confirm)  # 点击确认按钮
        time.sleep(2)




    def newcapturega1400(self,devicename):#新增智能抓拍机/ga1400
        self.clicks(self.area)  # 点击左侧组织下拉列表
        self.clicks(self.node)  # 选择下拉列表第一个子节点
        self.click(self.addbt)  # 点击新增设备按钮
        self.clicks(self.dtype, index=1)  # 设备类型 选择第二个：智能抓拍机
        self.click(self.nextbt)  # 点击下一步按钮
        self.click(self.accessmode, By.CSS_SELECTOR)  # 点击接入方式下拉框
        self.clicks(self.modeselect,index=1)  # 选择第二个：ga1400
        self.input_text(self.devicename, devicename)  # 输入设备名称
        self.input_text(self.salveIP,'10.10.1.122')# 输入salveIP
        self.input_text(self.deviceid,'104')# 输入设备ID
        self.input_text(self.Streamaddress,'rtsp://10.10.22.33:0000/test.264',type="invisible",scroll=True)#输入预览流地址
        self.input_text(self.longitude,'11')#输入经度
        self.input_text(self.latitude,'12')#输入纬度
        self.click(self.nextbt)  # 点击下一步按钮
        self.click(self.confirm)  # 点击确认按钮
        time.sleep(2)

    def newcaptureprivate(self,devicename):#新增智能抓拍机/澎思私有协议
        self.clicks(self.area)  # 点击左侧组织下拉列表
        self.clicks(self.node)  # 选择下拉列表第一个子节点
        self.click(self.addbt)  # 点击新增设备按钮
        self.clicks(self.dtype, index=1)  # 设备类型 选择第二个：智能抓拍机
        self.click(self.nextbt)  # 点击下一步按钮
        self.click(self.accessmode, By.CSS_SELECTOR)  # 点击接入方式下拉框
        self.clicks(self.modeselect, index=2)  # 选择第三个：澎思私有协议
        self.input_text(self.devicename, devicename)  # 输入设备名称
        self.click(self.brand)#点击品牌下拉框
        self.click(self.brandselect)#品牌下拉框中选择
        self.input_text(self.SN,'sn1256321')#输入SN码
        self.input_text(self.mac,'10.10.10.1',type="invisible",scroll=True)#输入mac地址
        self.click(self.nextbt)  # 点击下一步按钮
        self.click(self.confirm)  # 点击确认按钮
        time.sleep(2)

    def newgb(self,devicename):#新增GB实时相机
        self.clicks(self.area)  # 点击左侧组织下拉列表
        self.clicks(self.node)  # 选择下拉列表第一个子节点
        self.click(self.addbt)  # 点击新增设备按钮
        self.clicks(self.dtype, index=2)  # 设备类型 选择第二个：智能抓拍机
        self.click(self.nextbt)  # 点击下一步按钮
        self.input_text(self.devicename, devicename)  # 输入设备名称
        self.input_text(self.gbnum,'1122')# 输入视频GB编号
        self.input_text(self.gbaddress,'10.10.1.122')# 输入GB平台地址
        self.input_text(self.gbid,'10.10.1.122')# 输入GB平台ID
        self.input_text(self.gbport,'80',type="invisible",scroll=True)# 输入GB平台端口
        self.input_text(self.longitude,'115')#输入经度
        self.input_text(self.latitude,'120')#输入纬度
        self.click(self.nextbt)  # 点击下一步按钮
        self.click(self.confirm)  # 点击确认按钮
        time.sleep(2)

    def getinfo(self,devicename):
        em = self.find_element(self.search)
        em.send_keys(Keys.CONTROL, 'a')  # 模拟键盘操作，输入ctrl+A全选
        self.input_text(self.search,devicename)#查询输入框输入设备名称

        list=[]
        try:
            dn = self.get_text_m(self.getname)  # 获取设备名称字段
            list.append(dn)
        except:
            list.append(None)
        try:
            sn = self.get_text_m(self.getSN)  # 获取设备SN码字段
            list.append(sn)
        except:
            list.append(None)
        return list







    def getnodata(self,devicename):
        em = self.find_element(self.search)
        em.send_keys(Keys.CONTROL, 'a')  # 模拟键盘操作，输入ctrl+A全选
        self.input_text(self.search,devicename)#查询输入框输入设备名称
        return  self.get_text(self.nodata)#查询无数据校验

