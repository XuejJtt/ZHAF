#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 14:20
# @Author  : Xuej
# @File    : 首页.py
# @Software: PyCharm
from Common.BasePage import BasePage
import time


class First_Page(BasePage):
    username = '//span[@class="username"]'

    # 获取登录后的用户名
    def get_login_name(self):
        return self.get_text(self.username)
