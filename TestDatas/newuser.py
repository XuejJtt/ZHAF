import random

i = random.randint(1000, 9999)
s = '1855125' + str(i)
phone = s
name = "自动化"
pwd = "auto654321"
time = "2019-12-18"
#将新增用户时需要输入的内容放入一个字典中
newuser={'phone':s,'name':name,'pwd':pwd,'time':time}