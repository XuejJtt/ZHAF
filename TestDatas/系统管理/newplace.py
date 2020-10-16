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
#新增场所
newplace={'casename':'新增场所','placename':'autotestplace'+str(i),'placedisc':'仙鹤新天地广场'}
#修改区域
editplace={'casename':'修改场所','placename':'editplace'+str(i),'placedisc':'edit场所描述'}