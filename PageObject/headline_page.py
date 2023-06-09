# -- coding: utf-8 --
# @Time : 2023-03-28 9:18
# @Author : zhangwen
# @File : headline_page.py
from appium.webdriver.common.mobileby import MobileBy as By
from PageObject.home_page import HomePage
from Common.utils import Utils
from PageObject.load_config import HeadLoadConfig

utils = Utils()  # 实例化工具类
logger = Utils().logs  # 实例化logger


# 头条页面的相关操作
class Headline(HomePage):
    def __int__(self, driver):
        self.driver = driver

    # 发布文字贴
    def publish_text_invitation(self):
        self.bottom_navigation_bar_change("头条")
        self.element_click(By.ID, HeadLoadConfig.id_headline_community)
        self.element_click(By.ID, HeadLoadConfig.id_publish_invitation_button)
        self.element_click(By.ID, HeadLoadConfig.id_i_know_button)
        self.element_send_keys(By.ID, HeadLoadConfig.id_invitation_title_input_box, input_text="发个帖子看看20230221")
        self.element_send_keys(By.ID, HeadLoadConfig.id_invitation_content_input_box, input_text="输入个内容20230221")
        self.element_click(By.XPATH, HeadLoadConfig.xpath_upload_pictures)
        self.element_click(By.ID, HeadLoadConfig.id_select_pictures)
        self.element_click(By.ID, HeadLoadConfig.id_select_pictures_confirm_button)
        self.element_click(By.ID, HeadLoadConfig.id_select_prefecture)
        self.element_click(By.ID, HeadLoadConfig.id_select_prefecture_first)
        self.element_click(By.ID, HeadLoadConfig.id_select_prefecture_second)
        self.element_click(By.ID, HeadLoadConfig.id_select_topic)
        self.element_click(By.ID, HeadLoadConfig.id_select_topic_name)
        self.element_click(By.ID, HeadLoadConfig.id_publish_text_invitation_button)
        logger.info("文字帖发布成功")

    # 发布视频贴
    def publish_video_invitation(self, is_first_publish):
        if is_first_publish == "yes":
            self.bottom_navigation_bar_change("头条")
            self.element_click(By.ID, HeadLoadConfig.id_headline_community)
            self.element_click(By.ID, HeadLoadConfig.id_publish_invitation_button)
            self.element_click(By.ID, HeadLoadConfig.id_i_know_button)
        elif is_first_publish == "no":
            self.element_click(By.ID, HeadLoadConfig.id_go_publish_button)
        else:
            logger.info("{}的值输入有误".format(is_first_publish))
        self.element_click(By.ID, HeadLoadConfig.id_publish_video_invitation)
        self.element_click(By.ID, HeadLoadConfig.id_upload_video)
        self.element_click(By.ID, HeadLoadConfig.id_select_video)
        self.element_click(By.ID, HeadLoadConfig.id_select_pictures_confirm_button)
        self.element_send_keys(By.ID, HeadLoadConfig.id_invitation_title_input_box, input_text="发个视频看看20230221")
        self.element_click(By.ID, HeadLoadConfig.id_select_prefecture)
        self.element_click(By.ID, HeadLoadConfig.id_select_prefecture_first)
        self.element_click(By.ID, HeadLoadConfig.id_select_prefecture_second)
        self.element_click(By.ID, HeadLoadConfig.id_select_topic)
        self.element_click(By.ID, HeadLoadConfig.id_select_topic_name)
        self.element_click(By.ID, HeadLoadConfig.id_publish_text_invitation_button)
        logger.info("视频帖发布成功")

    # 帖子点赞
    def invitation_likes(self):
        self.element_click(By.ID, HeadLoadConfig.id_invitation_likes_button)
        logger.info("点赞成功")

    # 帖子评论
    def invitation_remark(self):
        self.element_click(By.ID, HeadLoadConfig.id_invitation_remark_button)
        self.element_click(By.ID, HeadLoadConfig.id_invitation_remark_write_button)
        self.element_send_keys(By.ID, HeadLoadConfig.id_invitation_remark_input_box, input_text="给你一个评论")
        self.element_click(By.ID, HeadLoadConfig.id_invitation_remark_publish_button)
        logger.info("评论成功")
