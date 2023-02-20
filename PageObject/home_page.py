# -- coding: utf-8 --
# @Time : 2023-02-07 9:37
# @Author : zhangwen
# @File : home_page.py
from Common.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy as By
from Common.utils import Utils
import configparser

utils = Utils()  # 实例化工具类
logger = Utils().logs  # 实例化logger


#主页面(有料)操作封装
class HomePage(BasePage):
    personal_information_agree = utils.get_config("home_page", "bottom_navigation_bar",
                                                 "personal_information_agree")  # 个人信息统一按钮
    experience_now = utils.get_config("home_page", "bottom_navigation_bar", "experience_now")  # 立即体验按钮
    my = utils.get_config("home_page", "bottom_navigation_bar", "my")  # 我的按钮
    match = utils.get_config("home_page", "bottom_navigation_bar", "match")  # 比赛按钮
    home = utils.get_config("home_page", "bottom_navigation_bar", "home")  # 我的有料按钮
    video = utils.get_config("home_page", "bottom_navigation_bar", "video")  # 视频按钮
    headline = utils.get_config("home_page", "bottom_navigation_bar", "headline")  # 头条按钮
    def __int__(self, driver):
        self.driver = driver


    #点击我的
    def click_my_button(self):
        self.element_click(By.ID)

if __name__ == '__main__':
    pass