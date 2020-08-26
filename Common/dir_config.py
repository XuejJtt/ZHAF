#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 10:02
# @Author  : Xuej
# @File    : dir_config.py
# @Software: PyCharm

import os

'''
定义框架层级的相对目录位置
'''

#框架的顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

config_dir = os.path.join(base_dir,'Config')

htmltestreport_dir = os.path.join(base_dir,'HtmlTestReport')

logs_dir = os.path.join(base_dir,'Logs')

processlog_dir = os.path.join(base_dir,'logs\\processlog')

resultlog_dir = os.path.join(base_dir,'logs\\resultlog')

screenshots_dir = os.path.join(base_dir,'ScreenShots')

testcases_dir = os.path.join(base_dir,'TestCases')

testdatas_dir = os.path.join(base_dir,'TestDatas')


if __name__ == '__main__':
    print(processlog_dir,resultlog_dir)




