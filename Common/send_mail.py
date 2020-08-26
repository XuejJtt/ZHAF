#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 14:25
# @Author  : Xuej
# @File    : send_mail.py
# @Software: PyCharm

import smtplib
import time
#用于构建邮件内容
from email.mime.text import MIMEText
#用于构建邮件头
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from Common import dir_config,read_cofig



class sendmail():
    def __init__(self,email_from,pwd,email_to,file,tile='自动化测试报告',text='详情见附件，请查收！',type='163',style_path='style.css'):
        '''

        :param email_from: 发件人的地址
        :param pwd: 发件人邮箱密码
        :param email_to: 收件人地址，多个收件人可传入一个列表
        :param file: 附件的路径
        :param tile: 邮件名称
        :param text: 邮件正文
        :param type: 使用哪个邮箱来发送邮件，默认163企业邮箱
        :param style_path: 定制化参数，针对发送html报告，同步发送css样式
        '''
        self.email_from = email_from
        self.pwd = pwd
        self.email_to = email_to
        self.file = file
        self.tile = tile
        self.text = text
        self.type = type
        self.style_path = style_path

    def send(self):
        msg = MIMEMultipart()
        msg["Subject"] = time.strftime('%Y-%m-%d-%H-%M')+self.tile
        msg["To"] = ','.join(self.email_to)
        msg["From"] = self.email_from

        #邮件正文部分
        part = MIMEText(self.text)
        msg.attach(part)

        #邮件附件_html报告
        part = MIMEApplication(open(self.file,'rb').read())
        part.add_header('Content-Disposition','attachment',filename=self.file.split('\\')[-1])
        msg.attach(part)

        #邮件附件_html报告样式CSS
        old = self.file.split('\\')[-1]
        new_style_path = self.file.replace(old,self.style_path)
        part = MIMEApplication(open(new_style_path, 'rb').read())
        part.add_header('Content-Disposition', 'attachment',filename='style.css')
        msg.attach(part)

        #发送邮件
        host ='smtphz.qiye.163.com' if self.type =='163' else 'smtp.qq.com'
        try:
            server = smtplib.SMTP_SSL(host,994,timeout=10)
        except Exception as e:
            print('连接失败',e)

        server.login(self.email_from,self.pwd)
        server.sendmail(self.email_from,self.email_to,msg.as_bytes())
        server.close()



if __name__ == '__main__':
    mes = read_cofig.Read_Config(dir_config.config_dir,'email.yaml').read_yaml()
    print(mes)
    file = 'D:\\UIAutoTest\\ZHAF\\HtmlTestReport\\2020-08-13-10-28-澎思云智慧安防p1.html'

    S = sendmail(mes['from'],mes['pwd'],mes['to'],file)
    S.send()


