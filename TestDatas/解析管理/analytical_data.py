#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 15:23
# @File    : analytical_data.py
# @Software: PyCharm


sum_devices =  {'name':'任务数统计','dec':'检查页面任务数统计是否正常'}

change_place = {'name':'子场所切换','dec':'切换包含子场所和不包含子场所'}

select_place = {'name':'子场所筛选','dec':'验证子场所筛选功能','place':'南京市'}

query_device = {'name':'设备查询','dec':'验证查询功能是否正常','device':'门口内部走廊1'}

query_reset =  {'name':'查询重置','dec':'验证重置按钮是否正常','device':'门口内部走廊1'}

mix_query = {'name':'混合筛选设备类型任务状态','dec':'通过设备类型和任务状态来筛选设备','type':'智能抓拍机','state':'已停止'}

devices_select = [{'name':'设备类型筛选_智能抓拍机','dec':'验证设备类型筛选功能是否正常','type':'智能抓拍机'},
                  {'name':'设备类型筛选_视屏流相机','dec':'验证设备类型筛选功能是否正常','type':'视屏流相机'},
                  {'name':'设备筛选_GB28181','dec':'验证设备类型筛选功能是否正常','type':'GB28181'},
                  {'name':'设备筛选_1400视图库','dec':'验证设备类型筛选功能是否正常','type':'1400视图库'},
                  ]

task_select = [{'name':'任务状态筛选_已停止','dec':'验证任务状态是否正常','state':'已停止'},
               {'name':'任务状态筛选_运行中','dec':'验证任务状态是否正常','state':'运行中'},
               {'name':'任务状态筛选_启动中','dec':'验证任务状态是否正常','state':'启动中'},
               {'name':'任务状态筛选_停止中','dec':'验证任务状态是否正常','state':'停止中'},
               {'name':'任务状态筛选_故障中','dec':'验证任务状态是否正常','state':'故障中'}]

