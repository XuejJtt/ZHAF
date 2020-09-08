#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author : Zhuzj
# @file : place.py
# @time : 2020/9/8 16:04
# @Software :PyCharm

from PageObjects.首页 import *
import TestDatas.newplace as place_date


class Area_managerment(BasePage):
    add='add-place-btn'#新增按钮
    wrapper='.option-wrapper .ant-btn-primary'#新增区域/场所按钮
    area_text='.ant-form-item-children .ant-input'#输入区域（区域）名称/描述
    Superior_list='.ant-form-item-children .ant-select-arrow-icon'# 点击上级区域下拉框
    Superior_area='ant-select-tree-title'# 选择上级区域
    primary='.ant-modal-footer .ant-btn-primary'#确定按钮
    place_type='div[class="ant-select-selection__placeholder"]'#场所类型
    place_list='ant-select-dropdown-menu-item'#场所类型下拉框
    name_search='[placeholder="请输入名称"]'#名称搜索框
    result_name='.ant-table-tbody [class="ant-table-row-cell-ellipsis ant-table-row-cell-break-word"]'#区域名称


    def new_area(self):  # 新建区域
        self.click(self.add,By.CLASS_NAME)# 点击新增按钮
        self.clicks(self.wrapper,By.CSS_SELECTOR)# 点击新增区域按钮
        self.input_text_m(self.area_text,place_date.newarea['areaname'],By.CSS_SELECTOR)# 输入区域名称
        self.input_text_m(self.area_text, place_date.newarea['areadisc'],By.CSS_SELECTOR,10,'visible',False,1)  # 输入区域描述
        self.click(self.Superior_list,By.CSS_SELECTOR)# 点击上级区域下拉框
        self.click(self.Superior_area,By.CLASS_NAME) # 选择上级区域
        self.click(self.primary,By.CSS_SELECTOR)# 点击确定按钮

    def new_place(self):
        self.click(self.add, By.CLASS_NAME)  # 点击新增按钮
        self.clicks(self.wrapper,By.CSS_SELECTOR,10,'visible',1)# 点击新增场所按钮
        self.input_text_m(self.area_text,place_date.newplace['placename'],By.CSS_SELECTOR)# 输入场所名称
        self.click(self.place_type,By.CSS_SELECTOR) # 点击场所类型
        self.clicks(self.place_list,By.CLASS_NAME) # 选择下拉列表中的第一个
        self.input_text_m(self.area_text, place_date.newplace['placedisc'], By.CSS_SELECTOR, 10, 'visible', False, 1)#输入场所描述
        self.clicks(self.Superior_list,By.CSS_SELECTOR,10,'visible',1)#点击上级区域下拉框
        self.click(self.Superior_area,By.CLASS_NAME)#选择上级区域
        self.click(self.primary, By.CSS_SELECTOR)  # 点击确定按钮


    def get_areainfo(self):

        self.input_text(self.name_search,place_date.newarea['areaname'],By.CSS_SELECTOR)#在搜索框中输入名称
        name=self.get_text(self.result_name,By.CSS_SELECTOR)#区域名称
        return name

    def get_placeinfo(self):
        self.input_text(self.name_search, place_date.newplace['placename'], By.CSS_SELECTOR)  # 在搜索框中输入名称
        name = self.get_text(self.result_name, By.CSS_SELECTOR)  # 区域名称
        return name