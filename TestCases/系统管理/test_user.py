import pytest
from Common.BasePage import BasePage
from PageObjects.登录页面 import login
from PageObjects.首页 import First_Page
from PageObjects.system.user import *
from Common.log import Log
from Common import dir_config
import TestDatas.login_test_datas as LTD

P_log = Log(dir_config.processlog_dir)
R_log = Log(dir_config.resultlog_dir)

@pytest.mark.usefixture("init_web")
class Test_user:
    @pytest.mark.smoke
    def test_newuser(self,init_web):
        P_log.info('*******开始执行新增用户测试用例******')
        login(init_web).login_system(LTD.success_data['username'],LTD.success_data['pwd'])
        First_Page(init_web).manager(2,'user')
        User(init_web).add_user()
        try:
            P_log.info("*******开始进行结果校验*********")
            assert User(init_web).get_user(2) == News.newuser['name']
            R_log.info("******新增用户用例执行成功******")
        except Exception as e:
            R_log.info("新增用户用例执行失败")
            P_log.error("新增用户用例失败,失败原因:{0}".format(e))
            login(init_web).save_picture('用例异常截图')
            raise e

if __name__ == '__main__':
    pytest.main(["-q","test_user.py"])