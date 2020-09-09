#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author : Zhuzj
# @file : test_user.py
# @time : 2020/9/9 17:04
# @Software :PyCharm

import random

i = random.randint(1000, 9999)
s = '1855125' + str(i)
phone = s
name = "自动化"
pwd = "auto654321"
time = "2019-12-18"
#将新增用户时需要输入的内容放入一个字典中
newuser={'phone':s,'name':name,'pwd':pwd,'time':time}

newusererr=[{'casename':'手机号码为空','phone':'','name':name,'pwd':pwd,'pwdtwo':pwd,'time':time,'error':'请选择手机号'},
            {'casename':'真实姓名为空','phone':s,'name':'','pwd':pwd,'pwdtwo':pwd,'time':time,'error':'请输入真实姓名'},
            {'casename':'密码为空','phone':s,'name':name,'pwd':'','pwdtwo':pwd,'time':time,'error':'请输入密码'},
            {'casename':'密码为空','phone':s,'name':name,'pwd':pwd,'pwdtwo':'','time':time,'error':'两次密码不一致'}]