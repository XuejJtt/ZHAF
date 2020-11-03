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

newusererr=[{'casename':'手机号码为空',
             'phone':'','name':name,'pwd':pwd,'pwdtwo':pwd,'time':time,'error':'请选择手机号'},
            {'casename':'真实姓名为空',
             'phone':s,'name':'','pwd':pwd,'pwdtwo':pwd,'time':time,'error':'请输入真实姓名'},
            {'casename':'密码为空',
             'phone':s,'name':name,'pwd':'','pwdtwo':pwd,'time':time,'error':'请输入密码'},
            {'casename':'确认密码为空',
             'phone':s,'name':name,'pwd':pwd,'pwdtwo':'','time':time,'error':'两次密码不一致'},
            {'casename': '手机号码小于11位',
             'phone': '185124', 'name': name, 'pwd': pwd, 'pwdtwo': pwd, 'time': time, 'error': '请输入11位手机号'},
            {'casename': '手机号码大于11位',
             'phone': '1851241258652', 'name': name, 'pwd': pwd, 'pwdtwo': pwd, 'time': time, 'error': '请输入11位手机号'},
            {'casename': '手机号码已存在',
             'phone': newuser['phone'], 'name': name, 'pwd': pwd, 'pwdtwo': pwd, 'time': time, 'error': '手机号已存在'},
            {'casename': '真实姓名小于2个字符',
             'phone': s, 'name': 'a', 'pwd': pwd, 'pwdtwo': pwd, 'time': time, 'error': '不少于2个字，不多于7个字'},
            {'casename': '真实姓名大于7个字符',
             'phone': s, 'name': 'a'*8, 'pwd': pwd, 'pwdtwo': pwd, 'time': time, 'error': '不少于2个字，不多于7个字'},
            {'casename': '确认密码输入不一致',
             'phone': s, 'name': name, 'pwd': pwd, 'pwdtwo': '253200', 'time': time,'error': '两次密码不一致'},
            {'casename': '所属组织为空',
             'phone': s, 'name': name, 'pwd': pwd, 'pwdtwo': pwd, 'time': time, 'error': '请选择所属组织'},
            {'casename': '所属角色为空',
             'phone': s, 'name': name, 'pwd': pwd, 'pwdtwo': pwd, 'time': time, 'error': '请选择角色'},
            {'casename': '身份证号码输入非数字字符',
             'phone': s, 'name': name, 'pwd': pwd, 'pwdtwo': pwd, 'time': time, 'cardID':'1523252541112ww','error': '请输入有效身份证号'},
            {'casename': '身份证号码输入非15或18位字符',
             'phone': s, 'name': name, 'pwd': pwd, 'pwdtwo': pwd, 'time': time, 'cardID':'2521','error': '请输入有效身份证号'}
            ]
