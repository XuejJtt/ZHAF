#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author : Zhuzj
# @file : user.py
# @time : 2020/9/8 16:04
# @Software :PyCharm

from time import sleep

from selenium.webdriver.common.keys import Keys
from Common.BasePage import BasePage
from selenium.webdriver.common.by import By
import TestDatas.系统管理.newuser as News
import time



class User(BasePage):


    newuser = 'ant-btn-primary'  # 新增用户按钮
    phone = '[placeholder="请输入手机号码"]'  # 手机号码输入框
    name = '[placeholder="请输入真实姓名"]'  # 用户姓名输入框
    pwd = '[placeholder="请输入密码"]'  # 密码
    pwdtwo = '[placeholder="请确认密码"]'  # 确认密码
    depart = 'ant-select-search__field__placeholder'  # 所属组织
    depart_list = 'ant-select-switcher-icon'  # 所属组织下拉框
    depart_checkbox = 'ant-select-tree-checkbox-inner'  # 所属组织下拉选择框
    role = '.ant-modal-content .ant-select-selection__placeholder'  # 所属角色
    role_checkbox = 'ant-select-dropdown-menu-item'  # 角色下拉选择框
    time = 'div .self-data-picker'  # 有效时间选择框
    time_input = '//input[@class="ant-calendar-input "]'  # 有效时间输入框
    city = '[placeholder="请输入所在城市"]' # 所属城市
    cardID='//input[@placeholder="请输入身份证号码"]'#身份证号码
    confirm = '.ant-modal-footer [class="ant-btn ant-btn-primary"]'  # 确定按钮
    search = '[placeholder="请输入用户姓名、手机号"]'  # 用户名/手机号查询输入框
    result = '.ant-table-tbody .ant-table-row-cell-break-word'  # 查询结果列表
    operate = 'table-button'  # 操作按钮
    state = 'ant-switch-inner'  # 账号状态
    delete = '.ant-modal-footer .ant-btn-primary'  # 删除确认
    emptylist='ant-empty-description'#空列表，表示删除成功
    inputnull='ant-form-explain'#输入为空，错误信息
    phone_repeat='//span[text()="手机号已存在"]/..'#手机号码重复


    def add_user(self,phone,name,pwd,pwdtwo,cardID=''):
        self.click(self.newuser, By.CLASS_NAME)  # 点击新增用户按钮
        self.input_text(self.phone,phone,By.CSS_SELECTOR)  # 手机号码
        self.input_text(self.name, name,By.CSS_SELECTOR)  # 真实姓名
        self.input_text(self.pwd, pwd,By.CSS_SELECTOR)  # 密码
        self.input_text(self.pwdtwo, pwdtwo,By.CSS_SELECTOR)  # 确认密码
        self.click(self.depart, By.CLASS_NAME)  # 点击所属组织
        self.click(self.depart_list, By.CLASS_NAME)  # 点击所属组织下拉框
        self.clicks(self.depart_checkbox,By.CLASS_NAME)# 所属组织--选择下拉框中最后一个
        self.click(self.role,By.CSS_SELECTOR)  # 点击所属角色框
        self.clicks(self.role_checkbox, By.CLASS_NAME)# 在所属角色下拉框中选择最后一个
        self.click(self.time,By.CSS_SELECTOR)  # 点击有效时间选择框
        self.input_text(self.time_input, News.newuser['time'], By.XPATH)  # 输入一个有效时间
        self.click(self.city,By.CSS_SELECTOR)# 点击所在城市输入框
        self.input_text(self.cardID,cardID)#输入身份证号码
        self.click(self.confirm,By.CSS_SELECTOR)#点击确定按钮
        time.sleep(2)
        print (News.newuser['phone'])

    def user_departnull(self,phone,name,pwd,pwdtwo):
        self.click(self.newuser, By.CLASS_NAME)  # 点击新增用户按钮
        self.input_text(self.phone,phone,By.CSS_SELECTOR)  # 手机号码
        self.input_text(self.name, name,By.CSS_SELECTOR)  # 真实姓名
        self.input_text(self.pwd, pwd,By.CSS_SELECTOR)  # 密码
        self.input_text(self.pwdtwo, pwdtwo,By.CSS_SELECTOR)  # 确认密码
        self.click(self.role,By.CSS_SELECTOR)  # 点击所属角色框
        self.clicks(self.role_checkbox, By.CLASS_NAME)# 在所属角色下拉框中选择最后一个
        self.click(self.time,By.CSS_SELECTOR)  # 点击有效时间选择框
        self.input_text(self.time_input, News.newuser['time'], By.XPATH)  # 输入一个有效时间
        self.click(self.city,By.CSS_SELECTOR)# 点击所在城市输入框
        self.click(self.confirm,By.CSS_SELECTOR)#点击确定按钮

    def user_rolenull(self, phone, name, pwd, pwdtwo):
        self.click(self.newuser, By.CLASS_NAME)  # 点击新增用户按钮
        self.input_text(self.phone, phone, By.CSS_SELECTOR)  # 手机号码
        self.input_text(self.name, name, By.CSS_SELECTOR)  # 真实姓名
        self.input_text(self.pwd, pwd, By.CSS_SELECTOR)  # 密码
        self.input_text(self.pwdtwo, pwdtwo, By.CSS_SELECTOR)  # 确认密码
        self.click(self.depart, By.CLASS_NAME)  # 点击所属组织
        self.click(self.depart_list, By.CLASS_NAME)  # 点击所属组织下拉框
        self.clicks(self.depart_checkbox, By.CLASS_NAME)  # 所属组织--选择下拉框中最后一个
        self.click(self.time, By.CSS_SELECTOR)  # 点击有效时间选择框
        self.input_text(self.time_input, News.newuser['time'], By.XPATH)  # 输入一个有效时间
        self.click(self.city, By.CSS_SELECTOR)  # 点击所在城市输入框
        self.click(self.confirm, By.CSS_SELECTOR)  # 点击确定按钮



    def modify_user(self):
        em = self.find_element(self.search,By.CSS_SELECTOR)
        em.send_keys(Keys.CONTROL, 'a')  # 模拟键盘操作，输入ctrl+A全选
        self.input_text(self.search, News.newuser['phone'],By.CSS_SELECTOR)  # 输入手机号
        sleep(2)
        self.clicks(self.operate, By.CLASS_NAME)# 点击编辑按钮
        sleep(2)
        self.click(self.time,By.CSS_SELECTOR)  # 点击有效时间选择框
        em = self.find_element(self.time_input, By.XPATH)
        em.send_keys(Keys.CONTROL, 'a')
        self.input_text(self.time_input, '2022-12-18', By.XPATH)  # 输入一个有效时间
        self.click(self.city,By.CSS_SELECTOR)# 点击所在城市输入框
        self.click(self.confirm,By.CSS_SELECTOR)
        time.sleep(2)

    def freeze_user(self):
        em = self.find_element(self.search,By.CSS_SELECTOR)
        em.send_keys(Keys.CONTROL, 'a')  # 模拟键盘操作，输入ctrl+A全选
        self.input_text(self.search, News.newuser['phone'],By.CSS_SELECTOR)  # 输入手机号
        sleep(2)
        self.click(self.state, By.CLASS_NAME)  # 点击 冻结
        time.sleep(2)

    def del_user(self):
        em = self.find_element(self.search,By.CSS_SELECTOR)
        em.send_keys(Keys.CONTROL, 'a')  # 模拟键盘操作，输入ctrl+A全选
        self.input_text(self.search, News.newuser['phone'],By.CSS_SELECTOR)  # 输入手机号
        sleep(2)
        self.clicks(self.operate,By.CLASS_NAME,10,'visible',2)# 点击删除按钮
        self.click(self.delete,By.CSS_SELECTOR)
        time.sleep(2)


    def get_user(self, num):  # 获取用户信息
        em = self.find_element(self.search,By.CSS_SELECTOR)
        em.send_keys(Keys.CONTROL, 'a')  # 模拟键盘操作，输入ctrl+A全选
        self.input_text(self.search, News.newuser['phone'],By.CSS_SELECTOR)  # 输入手机号
        sleep(3)
        els = self.find_elements(self.result,By.CSS_SELECTOR)
        return els[num].text  # 获取查询结果中(2:用户名;4:所属组织;5:用户角色;6:有效期限；7：账号状态)字段文本

    def get_user_null(self):  # 确认删除成功,无用户信息
        em = self.find_element(self.search,By.CSS_SELECTOR)
        em.send_keys(Keys.CONTROL, 'a')  # 模拟键盘操作，输入ctrl+A全选
        self.input_text(self.search, News.newuser['phone'],By.CSS_SELECTOR)  # 输入手机号
        sleep(2)
        return self.get_text(self.emptylist,By.CLASS_NAME)#空列表时，为字段文本为No Data

    def get_errorinfo(self):
        msg=[]
        try:
            phonerepeat=self.get_text(self.phone_repeat,By.XPATH,10)#手机号码重复报错信息
            msg.append(phonerepeat)
        except:
            msg.append(None)
        try:
            errinfo=self.get_text_m(self.inputnull,By.CLASS_NAME,10)#输入为空时的报错信息
            msg.append(errinfo)
        except:
            msg.append(None)
        return msg


