# -- coding: utf-8 --
# @Time : 2023-06-09 15:09
# @Author : zhangwen
# @File : run_all_testcase.py

import pytest
from Common.AllPath import *
if __name__ == '__main__':
    pytest.main(['-s', "-q", '../TestCase', '--alluredir', '../Report/allure-result', "--clean-alluredir"])
    os.system("allure generate {}/allure-result -o {}/allure-report  --clean".format(report_path, report_path))