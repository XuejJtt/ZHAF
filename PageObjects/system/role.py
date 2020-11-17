#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author : Zhuzj
# @file : role.py
# @time : 2020/11/10 14:05
# @Software :PyCharm

from Common.BasePage import *
from selenium.webdriver.common.keys import Keys
import time


class role_manage(BasePage):
    #新增角色
    addbt='//img[@class="add-button"]'
    角色名='//input[@class="ant-input"]'#角色名称/角色描述
    conform='//span[text()="确 认"]/..'#确认按钮
    editbt='//span[text()="编 辑"]/..'#编辑按钮
    delbt='//span[text()="删 除"]/..'#删除按钮
    delconform='//span[text()="确 定"]/..'#删除确认按钮

    #获取列表中所有角色名称/描述
    getrolename='//*[@class="role-list-item-info"]/span[1]'
    getroledisc='//*[@class="role-list-item-info"]/span[2]'

    def new_role(self,rolename,roledisc):
        self.click(self.addbt)#点击新增按钮
        self.input_text_m(self.角色名,rolename,index=0)#输入角色名称
        self.input_text_m(self.角色名,roledisc,index=1)#输入角色描述
        self.click(self.conform)#点击确认按钮
        self.refresh()  # 页面刷新

    def modify_role(self,rolenamebef,rolenameaft,roledisc):
        self.click(locator="//span[@title='{0}']/..".format(rolenamebef))#点击需要修改的角色(修改前角色名)
        self.click(self.editbt)#点击编辑按钮
        self.input_text_m(self.角色名,text=(Keys.CONTROL, 'a'),index=0)# 模拟键盘操作，输入ctrl+A全选
        self.input_text_m(self.角色名, rolenameaft, index=0)  # 输入角色名称（修改后角色名）
        self.input_text_m(self.角色名, text=(Keys.CONTROL, 'a'), index=1)  # 模拟键盘操作，输入ctrl+A全选
        self.input_text_m(self.角色名, roledisc, index=1)  # 输入角色描述
        self.click(self.conform)#点击确认按钮
        self.refresh()#页面刷新


    def del_role(self,rolename):
        self.click(locator="//span[@title='{0}']/..".format(rolename))  # 点击需要删除的角色（修改后的角色名）
        self.click(self.delbt)#点击删除按钮
        self.click(self.delconform)#点击确定按钮




    def getroletext(self):
        list1=[]
        list2=[]
        em1 = self.find_elements(self.getrolename)
        em2 = self.find_elements(self.getroledisc)
        count=len(em1)#获取列表中数据总数

        """
        分别取出所有的角色名和角色描述，存放于列表中
        """
        for n in range(count):
            name = em1[n].text
            list1.append(name)
            disc = em2[n].text
            list2.append(disc)
        # info= dict(zip(list1,list2))


        return list1,list2




