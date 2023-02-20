# -- coding: utf-8 --
# @Time : 2023-02-11 15:49
# @Author : zhangwen
# @File : test_case_my_page.py
import allure
import pytest,os
from Common.AllPath import *
from PageObject.my_page import MyPage
from Common.utils import Utils
from Common.desired_cap import desired_cap

class TestMapage:
    def setup_class(self):
        self.my_page = MyPage()
        self.logger = self.my_page.logger
        self.my_page.driver = desired_cap().desired_cap()
        self.logger.info("**************用例开始执行**************")

    def teardown_class(self):
        self.logger.info("**************用例执行结束**************")

    @allure.feature("登录成功")
    def test_login(self):
        self.my_page.login_password("13000000000", "abc123456")
        assert self.my_page.get_attr_value("text") != "登录/注册"



if __name__ == '__main__':
    #pytest.main()
    pytest.main(['-s', "-q",'test_case_my_page.py', '--alluredir', '../Report/allure-result'])
    #pytest.main(['-s', "-q", './test_login.py', '--alluredir', '../Report/allure-result'])
    os.system("allure generate {}/allure-result -o {}/allure-report  --clean".format(report_path, report_path))
    a = Utils()
    a.copy_history()
