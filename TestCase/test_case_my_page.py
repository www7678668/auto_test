# -- coding: utf-8 --
# @Time : 2023-02-11 15:49
# @Author : zhangwen
# @File : tes
# t_case_my_page.py

import pytest, os, sys
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
sys.path.append("C:\\Users\\Administrator\\AppData\\Roaming\\Python\\Python37\\site-packages")
from Common.desired_cap import DesiredCap
from Common.AllPath import *
from PageObject.my_page import MyPage
from PageObject.headline_page import Headline
from Common.utils import Utils
import allure


class TestMapage:
    def setup_class(self):
        self.my_page = MyPage()
        self.my_page.driver = DesiredCap.desired_cap()
        self.utils = Utils()  # 实例化工具类
        self.logger = self.utils.logs  # 实例化logger
        self.headline_page = Headline()
        self.headline_page.driver = self.my_page.driver
        self.logger.info("**************用例开始执行**************")

    def teardown_class(self):
        self.logger.info("**************用例执行结束**************")
    #
    # @allure.feature("登录密码错误，登录失败")
    # def test_login_password_error(self):
    #     self.my_page.login_password("13000000011", "abc12456")
    #     assert self.my_page.get_qq_login_value() is not None
    #
    # @allure.feature("登录账号错误，登录失败")
    # def test_login_account_error(self):
    #     self.my_page.login_password("23000000011", "abc123456", is_first_login = "no")
    #     assert self.my_page.get_qq_login_value() is not None
    #
    #
    #
    # @allure.feature("登录账号密码错误，登录失败")
    # def test_login_account_password_error(self):
    #     self.my_page.login_password("33000000011", "ab555c123456")
    #     assert self.my_page.get_qq_login_value() is not None


    @allure.feature("账号密码正确，登录成功")
    def test_login_success(self):
        self.my_page.login_password("13000000015", "abc123456")
        assert self.my_page.get_user_value() != "登录/注册"
    #
    # @allure.feature("发布一个竞足免费方案")
    # def test_publish_free_plan(self):
    #     self.my_page.publish_plan(
    #         play_type="竞足",
    #         play_way="胜平负",
    #         match_count=1,
    #         play_price=0,
    #         mian=1,
    #         secondary=2,
    #         plan_title="发布一个竞足免费方案---66666",
    #         recommend_reason="推荐",
    #         expert_analyse_content="555")
    #     print(self.my_page.get_publish_success_value())
    #     assert self.my_page.get_publish_success_value() == "发布成功"
    #
    # @allure.feature("发布一个北单专家福利方案")
    # def test_publish_pay_plan(self):
    #     self.my_page.click_complete_button()
    #     self.my_page.publish_plan(
    #         first="no",
    #         play_type="北单",
    #         play_way="胜负过关",
    #         match_count=2,
    #         play_price=38,
    #         mian=1,
    #         secondary=2,
    #         expert_benefits_type="现金",
    #         is_no_limit_number="no",
    #         plan_title="发布一个北单专家福利方案---66666",
    #         recommend_reason="推荐",
    #         expert_analyse_content="555")
    #     print(self.my_page.get_publish_success_value())
    #     assert self.my_page.get_publish_success_value() == "发布成功"
    #
    # @allure.feature("发布一个竞篮付费方案")
    # def test_publish_benefits_plan(self):
    #     self.my_page.click_complete_button()
    #     self.my_page.publish_plan(
    #         first="no",
    #         play_type="竞篮",
    #         play_way="大小分",
    #         match_count=1,
    #         play_price=38,
    #         mian=1,
    #         secondary=2,
    #         plan_title="发布一个竞篮付费方案---66666",
    #         recommend_reason="推荐",
    #         expert_analyse_content="555")
    #     print(self.my_page.get_publish_success_value())
    #     assert self.my_page.get_publish_success_value() == "发布成功"
    #
    # @allure.feature("发布一个竞足其他玩法方案")
    # def test_publish_other_plan(self):
    #     self.my_page.click_complete_button()
    #     self.my_page.publish_plan(
    #         first="no",
    #         play_type="竞足",
    #         play_way="胜平负",
    #         match_count=3,
    #         play_price=88,
    #         score_type=1,
    #         score_value1=2,
    #         score_value2=3,
    #         goal1=1,
    #         goal2=7,
    #         plan_title="发布一个竞足其他玩法方案---66666",
    #         recommend_reason="推荐",
    #         expert_analyse_content="555")
    #     print(self.my_page.get_publish_success_value())
    #     assert self.my_page.get_publish_success_value() == "发布成功"
    #
    #
    # @allure.feature("购买一个方案")
    # def test_buy_plan(self):
    #     self.my_page.click_complete_button()
    #     self.my_page.return_my_page()
    #     self.my_page.logout_my_page()
    #     self.my_page.login_password("13000000000", "abc123456", is_first_login="no")
    #     self.home_page.bottom_navigation_bar_change("有料")
    #     self.my_page.buy_plan(1, is_expert_benefits="no")

    @allure.feature("发布一个图文帖子")
    def test_publish_text_invitation(self):
        self.headline_page.bottom_navigation_bar_change("头条")
        self.headline_page.publish_text_invitation()

    @allure.feature("发布一个视频帖子")
    def test_publish_video_invitation(self):
        self.headline_page.publish_video_invitation(is_first_publish="no")


if __name__ == '__main__':
    # pytest.main()
    pytest.main(['-s', "-q", 'test_case_my_page.py', '--alluredir', '../Report/allure-result', "--clean-alluredir"])
    # pytest.main(['-s', "-q", './test_login.py', '--alluredir', '../Report/allure-result'])
    os.system("allure generate {}/allure-result -o {}/allure-report  --clean".format(report_path, report_path))

    a = Utils()
    a.copy_history()

