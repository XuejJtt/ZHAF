#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/21 16:29
# @Author  : Caoyq
# @File    : library_manage.py
# @Software: PyCharm
import self as self

from Common.BasePage import *

class library_manage(BasePage):
    # 新增底库按钮
    add = '//button[@class="add-repo ant-btn ant-btn-primary"]'
    # 新增输入底库名称
    inputname = '//input[@placeholder = "请填写底库名称"]'
    # 搜索输入底库名称
    searchname= '//input[@placeholder = "请输入底库名称"]'
    # 选择底库类型
    face = '//span[text()="人 脸"]/..'
    body = '//span[text()="人 体"]/..'
    vehicle = '//div[@class="type-select-wrapper"]/button[3]'
    # 新增确定按钮
    submit = '//span[text()="确 定"]/..'
    # 删除确定按钮
    deleteOK = '(//div[@class="ant-modal-footer"])[2]//button[2]'
    # 删除取消按钮
    cancel = '(//div[@class="ant-modal-footer"])[2]//button[1]'
    # 底库名称
    facename ='//div[@class="library-card-name"]'
    bodyname ='(//div[@class="library-card-name"])[2]'
    vehiclename ='(//div[@class="library-card-name"])[3]'
    # 悬浮配置框
    config = '//div[@class ="library-card-option"]'
    # 人脸配置
    faceconfig = '//div[@class ="library-card-option-cover"]/span[1]'
    # 编辑
    edit = '//div[@class ="library-card-option-cover"]/span[2]'
    # 权限配置
    permissionconfig = '//div[@class ="library-card-option-cover"]/span[3]'
    # 删除
    delete = '//div[@class ="library-card-option-cover"]/span[4]'
    # 单个添加
    singleadd = '//span[text()="单个添加"]/..'
    # 批量添加
    batchadd = '//span[text()="批量添加"]/..'
    # 搜索结果数
    searchnumber = '//li[@class="ant-pagination-total-text"]'




    def newadd(self,type,newname): #新增底库确认
        self.click(self.add) #点击新增底库
        self.input_text(self.inputname, newname)  # 输入名称
        time.sleep(2)
        if type == '人脸':
            self.click(self.face)#选择类型
        elif type == '人体':
            self.click(self.body)
        elif type == '机动车':
            self.click(self.vehicle)
        self.click(self.submit)
        time.sleep(2)

    def librarysearch(self,searchname): #输入名称搜索底库
        self.input_text(self.searchname,searchname) #输入属性
        time.sleep(2)

    def librarydelete(self,YorN,searchname): #删除底库数据
        self.input_text(self.searchname, searchname)  # 输入属性
        self.move_mouse(self.config,by=By.XPATH)
        self.click(self.delete)
        time.sleep(2)
        if YorN == 'Yes':
            self.click(self.deleteOK)
        elif YorN == 'No':
            self.click(self.cancel)
        time.sleep(2)