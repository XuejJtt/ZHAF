#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/22 11:37
# @Author  : Xuej
# @File    : login.py
# @Software: PyCharm
from Common.BasePage import *


class login(BasePage):
    account='//input[@placeholder="输入用户名"]'
    pwd='//input[@placeholder="输入密码"]'
    login_button='//span[text()="登 录"]/..'
    account_msg='(//div[@class="ant-form-explain"])[1]'
    pwd_msg='(//div[@class="ant-form-explain"])[2]'


    def login_system(self,user,password):
        '''
        登录系统
        :param user: 用户名
        :param password: 密码
        :return:
        '''
        self.input_text(self.account,user)
        self.input_text(self.pwd,password)
        self.click(self.login_button)

    def get_login_msg(self):
        '''
        获取页面登录信息
        '''
        msg = []
        try:
            msg_account = self.get_text(self.account_msg,wait_times=3)
            msg.append(msg_account)
        except:
            msg.append(None)
        try:
            msg_pwd = self.get_text(self.pwd_msg,wait_times=3)
            msg.append(msg_pwd)
        except:
            msg.append(None)
        return msg