# -- coding: utf-8 --
# @Time : 2023-02-15 18:20
# @Author : zhangwen
# @File : test_login.py
import allure
import pytest
import pytest, os, sys
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
from Common.AllPath import *
#from PageObject.my_page import MyPage
from Common.utils import Utils
#from Common.desired_cap import DesiredCap

class TestMapage2:
    def setup_class(self):
        # self.my_page = MyPage()
        # self.my_page.driver = desired_cap().desired_cap()
        pass

    def teardown_class(self):
        print("结束")

    @allure.feature("测试两个55文件")
    def test_ggogo1(self):
        assert 5==5

    @allure.feature("测试san个文件")
    def test_ggogo2(self):
        assert 5 == 6

    @allure.feature("测试sn个文件")
    def test_ggogo3(self):
        assert 5 == 8

    @allure.feature("测试sn个文件")
    def test_ggogo4(self):
        assert 5 == 8


if __name__ == '__main__':
    pytest.main(['-s', "-q", 'test_login.py', '--alluredir', '../Report/allure-result'])
    os.system("allure generate {}/allure-result -o {}/allure-report  --clean".format(report_path, report_path))

    #pytest.main(['-s', "-q", 'test_case_my_page.py', '--alluredir', '../Report/allure-result'])
    # pytest.main(['-s', "-q", './test_login.py', '--alluredir', '../Report/allure-result'])
    #os.system("allure generate {}/allure-result -o {}/allure-report  --clean".format(report_path, report_path))
    a = Utils()
    a.copy_history()

# pytest -sv .\TestCase\test_login.py --alluredir /.\Report\allure-result --clean-alluredir
#
#pytest -sv .\TestCase\test_login.py --alluredir .\Report\allure-result --clean-alluredir


# allure generate .\Report\allure-result -o .\Report\allure-report  --clean