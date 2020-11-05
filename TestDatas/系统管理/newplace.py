#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author : Zhuzj
# @file : newplace.py
# @time : 2020/9/8 16:04
# @Software :PyCharm

import random
i= random.randint(1,1000)
#新增区域
newarea={'casename':'新增区域','areaname':'autotestarea'+str(i),'areadisc':'autotest区域描述'}
#修改区域
editarea={'casename':'修改区域','areaname':'editarea'+str(i),'areadisc':'edit区域描述'}

#新增区域异常场景
newarea_err=[{'casename':'新增区域--区域名称为空','areaname':'',
              'areadisc':'区域名称为空','errinfo':'请输入区域名称'},

             {'casename':'新增区域--区域名称超长','areaname':'区域名称超长'*10,
              'areadisc':'区域名称大于50个字符','errinfo':'请输入1到50个字符'},

             {'casename':'新增区域--上级区域为空','areaname':'上级区域为空',
              'areadisc':'上级区域为空','errinfo':'请选择父节点'}]

#新增场所
newplace={'casename':'新增场所','placename':'autotestplace'+str(i),'placedisc':'仙鹤新天地广场'}
#修改场所
editplace={'casename':'修改场所','placename':'editplace'+str(i),'placedisc':'edit场所描述'}

#新增场所异常场景
newplace_err=[{'casename':'新增场所--场所名称为空','placename':'',
               'placedisc':'仙鹤新天地广场','errinfo':'请输入场所名称'},

              {'casename':'新增场所--场所名称超长','placename':'场所名称超长'*10,
               'placedisc':'仙鹤新天地广场','errinfo':'请输入1到50个字符'},

              {'casename':'新增场所--场所类型为空','placename':'场所类型为空',
               'placedisc':'仙鹤新天地广场','errinfo':'请输选择场所类型'},

              {'casename': '新增场所--上级区域为空', 'placename': '上级区域为空',
               'placedisc': '仙鹤新天地广场', 'errinfo': '请选择上级区域'}]
