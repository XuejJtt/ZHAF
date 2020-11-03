#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author : Zhuzj
# @file : place.py
# @time : 2020/9/8 16:04
# @Software :PyCharm

from PageObjects.index.first_page import *
import TestDatas.系统管理.newplace as place_date
from selenium.webdriver.common.keys import Keys
from time import sleep


class Area_managerment(BasePage):
    list1 = []
    list1.append(place_date.newarea['areaname'])  # 新增区域 区域名称
    list1.append(place_date.editarea['areaname'])  # 修改区域 区域名称
    list1.append(place_date.newplace['placename'])  # 新增场所 场所名称
    list1.append(place_date.editplace['placename'])  # 修改场所 场所名称

    add='add-place-btn'#新增按钮
    wrapper='.option-wrapper .ant-btn-primary'#新增区域/场所按钮
    area_text='.ant-form-item-children .ant-input'#输入区域（场所）名称/描述
    Superior_list='.ant-form-item-children .ant-select-arrow-icon'# 点击上级区域下拉框
    Superior_area='ant-select-tree-title'# 选择上级区域
    primary='.ant-modal-footer .ant-btn-primary'#确定按钮
    place_type='div[class="ant-select-selection__placeholder"]'#场所类型
    place_list='ant-select-dropdown-menu-item'#场所类型下拉框
    name_search='[placeholder="请输入名称"]'#名称搜索框
    edit_button='//*[@class="ant-btn ant-btn-link"]'#操作按钮 0：编辑  1：分配设备  2：删除  3：上移  4：下移
    edit_areaname='//input[@placeholder="请输入"]'#修改区域名称
    edit_areadis='//textarea[@placeholder="请输入"]'#修改区域描述
    edit_confirm='//span[text()="确 定"]/..'#确定按钮
    result_name='.ant-table-tbody [class="ant-table-row-cell-ellipsis ant-table-row-cell-break-word"]'#区域名称
    result_dis='.ant-table-tbody [class="ant-table-row-cell-ellipsis"]'#区域描述
    emptylist = 'ant-empty-description'  # 空列表，表示删除成功
    area_errinfo='//div[@class="ant-form-explain"]'#区域（场所名称）错误提示语


    def new_area(self,areaname,areadisc):  # 新建区域
        self.click(self.add,By.CLASS_NAME)# 点击新增按钮
        self.clicks(self.wrapper,By.CSS_SELECTOR)# 点击新增区域按钮
        self.input_text_m(self.area_text, areaname, By.CSS_SELECTOR)  # 输入区域名称
        self.input_text_m(self.area_text, areadisc, By.CSS_SELECTOR, 10, 'visible', False,1)  # 输入区域描述
        self.click(self.Superior_list,By.CSS_SELECTOR)# 点击上级区域下拉框
        self.click(self.Superior_area,By.CLASS_NAME) # 选择上级区域
        self.click(self.primary,By.CSS_SELECTOR)# 点击确定按钮

    def area_Supernull(self,areaname,areadisc):  # 新建区域--上级区域为空
        self.click(self.add,By.CLASS_NAME)# 点击新增按钮
        self.clicks(self.wrapper,By.CSS_SELECTOR)# 点击新增区域按钮
        self.input_text_m(self.area_text, areaname, By.CSS_SELECTOR)  # 输入区域名称
        self.input_text_m(self.area_text, areadisc, By.CSS_SELECTOR, 10, 'visible', False,1)  # 输入区域描述
        self.click(self.primary,By.CSS_SELECTOR)# 点击确定按钮

    def modify_area(self):#修改区域名称和区域描述
        em=self.find_element(self.name_search,By.CSS_SELECTOR)
        em.send_keys(Keys.CONTROL,'a')
        self.input_text(self.name_search, place_date.newarea['areaname'], By.CSS_SELECTOR)  # 在搜索框中输入名称
        self.clicks(self.edit_button,By.XPATH,10,'visible',0)#点击编辑按钮
        em=self.find_element(self.edit_areaname)
        em.send_keys(Keys.CONTROL,'a')
        self.input_text(self.edit_areaname,place_date.editarea['areaname'])#修改区域名称
        em=self.find_element(self.edit_areadis)
        em.send_keys(Keys.CONTROL,'a')
        self.input_text(self.edit_areadis,place_date.editarea['areadisc'])#修改区域描述
        self.click(self.edit_confirm)#点击确定按钮

    def deleteplace(self,n):#新增场所/区域
        em = self.find_element(self.name_search, By.CSS_SELECTOR)
        em.send_keys(Keys.CONTROL, 'a')
        self.input_text(self.name_search,Area_managerment.list1[n],By.CSS_SELECTOR)# 在搜索框中输入名称
        self.clicks(self.edit_button,By.XPATH,10,'visible',2)#点击删除按钮
        self.click(self.edit_confirm)#点击删除确认框中确定按钮


    def new_place(self,placename,placedisc):#新增场所
        self.click(self.add, By.CLASS_NAME)  # 点击新增按钮
        self.clicks(self.wrapper,By.CSS_SELECTOR,10,'visible',1)# 点击新增场所按钮
        self.input_text_m(self.area_text,placename,By.CSS_SELECTOR)# 输入场所名称
        self.click(self.place_type,By.CSS_SELECTOR) # 点击场所类型
        self.clicks(self.place_list,By.CLASS_NAME) # 选择下拉列表中的第一个
        self.input_text_m(self.area_text, placedisc, By.CSS_SELECTOR, 10, 'visible', False, 1)#输入场所描述
        self.clicks(self.Superior_list,By.CSS_SELECTOR,10,'visible',1)#点击上级区域下拉框
        self.click(self.Superior_area,By.CLASS_NAME)#选择上级区域
        self.click(self.primary, By.CSS_SELECTOR)  # 点击确定按钮

    def place_typenull(self,placename,placedisc):#新增场所---场所类型为空
        self.click(self.add, By.CLASS_NAME)  # 点击新增按钮
        self.clicks(self.wrapper,By.CSS_SELECTOR,10,'visible',1)# 点击新增场所按钮
        self.input_text_m(self.area_text,placename,By.CSS_SELECTOR)# 输入场所名称
        self.input_text_m(self.area_text, placedisc, By.CSS_SELECTOR, 10, 'visible', False, 1)#输入场所描述
        self.clicks(self.Superior_list,By.CSS_SELECTOR,10,'visible',1)#点击上级区域下拉框
        self.click(self.Superior_area,By.CLASS_NAME)#选择上级区域
        self.click(self.primary, By.CSS_SELECTOR)  # 点击确定按钮

    def place_Supernull(self,placename,placedisc):#新增场所---上级区域为空
        self.click(self.add, By.CLASS_NAME)  # 点击新增按钮
        self.clicks(self.wrapper,By.CSS_SELECTOR,10,'visible',1)# 点击新增场所按钮
        self.input_text_m(self.area_text,placename,By.CSS_SELECTOR)# 输入场所名称
        self.click(self.place_type, By.CSS_SELECTOR)  # 点击场所类型
        self.clicks(self.place_list, By.CLASS_NAME)  # 选择下拉列表中的第一个
        self.input_text_m(self.area_text, placedisc, By.CSS_SELECTOR, 10, 'visible', False, 1)#输入场所描述
        self.click(self.primary, By.CSS_SELECTOR)  # 点击确定按钮

    def modify_place(self):#修改场所名称和场所描述
        em = self.find_element(self.name_search, By.CSS_SELECTOR)
        em.send_keys(Keys.CONTROL, 'a')
        self.input_text(self.name_search,place_date.newplace['placename'],By.CSS_SELECTOR)# 在搜索框中输入名称
        self.clicks(self.edit_button, By.XPATH, 10, 'visible', 0)  # 点击编辑按钮
        em = self.find_elements(self.area_text,By.CSS_SELECTOR)
        em[0].send_keys(Keys.CONTROL, 'a')
        self.input_text_m(self.area_text, place_date.editplace['placename'], By.CSS_SELECTOR)  # 修改场所名称
        em[1].send_keys(Keys.CONTROL, 'a')
        self.input_text_m(self.area_text, place_date.editplace['placedisc'], By.CSS_SELECTOR, 10, 'visible', False, 1)  # 修改场所描述
        self.click(self.primary, By.CSS_SELECTOR)  # 点击确定按钮



    def get_areainfo(self,n):

        em = self.find_element(self.name_search,By.CSS_SELECTOR)
        em.send_keys(Keys.CONTROL, 'a')

        # 在搜索框中输入名称 list1 0:新增 区域名称 1：修改 区域名称  2：新增 场所名称  3：修改 场所名称
        self.input_text(self.name_search,Area_managerment.list1[n],By.CSS_SELECTOR)
        name=self.get_text(self.result_name,By.CSS_SELECTOR)#区域名称
        dis=self.get_text(self.result_dis,By.CSS_SELECTOR)#区域描述
        list=[]
        list.append(name)
        list.append(dis)
        return list

    def get_info_err(self):

        return self.get_text(self.area_errinfo)#获取错误提示语

    def get_infonull(self,n):
        em = self.find_element(self.name_search, By.CSS_SELECTOR)
        em.send_keys(Keys.CONTROL, 'a')  # 模拟键盘操作，输入ctrl+A全选
        self.input_text(self.name_search, Area_managerment.list1[n], By.CSS_SELECTOR)  # 在搜索框中输入名称
        sleep(2)
        return self.get_text(self.emptylist, By.CLASS_NAME)  # 空列表时，为字段文本为No Data