#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author : Zhuzj
# @file : newcamera.py
# @time : 2020/9/10 17:59
# @Software :PyCharm
import random
i=random.randint(1,1000)
videoadress='rtsp://10.10.1.10:0000/test.264'
ftpadress='10.10.1.221'
port='21'
username='admin'
password='password'
filepath='/test/face/camera'
longitude='118'
latitude='25'
SN='SNauto'+str(i)
#新增视频流相机
newvideo={'casename':'新增视频流相机','devicename':'视频流相机设备'+str(i),'deviceadress':videoadress,'longitude':'118','latitude':'25','SN':SN}

#新增智能抓拍机/ftp
newcapture_ftp={'casename':'新增ftp智能抓拍机','devicename':'智能抓拍机ftp'+str(i)}

#新增智能抓拍机/ga1400
newcapture_ga1400={'casename':'新增ga1400智能抓拍机','devicename':'智能抓拍机ga1400'+str(i)}

#新增智能抓拍机/澎思私有协议
newcapture_private={'casename':'新增澎思私有协议智能抓拍机','devicename':'智能抓拍机澎思私有协议'+str(i)}

#新增GB实时相机
newGB={'casename':'新增GB实时相机','devicename':'GB实时'+str(i)}
