# -- coding: utf-8 --
# @Time : 2023-03-28 9:18
# @Author : zhangwen
# @File : headline_page.py
from appium.webdriver.common.mobileby import MobileBy as By
from PageObject.home_page import HomePage
from Common.utils import Utils

utils = Utils()  # 实例化工具类
logger = Utils().logs  # 实例化logger


# 头条页面的相关操作
class Headline(HomePage):
    id_headline_community = utils.get_config("headline", "invitation", "id_headline_community")  # 切换到社区
    id_publish_invitation_button = utils.get_config("headline", "invitation",
                                                    "id_publish_invitation_button")  # 弹窗提示的去发帖按钮
    id_i_know_button = utils.get_config("headline", "invitation", "id_i_know_button")  # 发帖页面弹窗提示的我知道啦
    id_invitation_title_input_box = utils.get_config("headline", "invitation", "id_invitation_title_input_box")  # 标题
    id_invitation_content_input_box = utils.get_config("headline", "invitation",
                                                       "id_invitation_content_input_box")  # 帖子内容
    xpath_upload_pictures = utils.get_config("headline", "invitation", "xpath_upload_pictures")  # 上传图片
    id_select_pictures = utils.get_config("headline", "invitation", "id_select_pictures")  # 选择图片
    id_select_pictures_confirm_button = utils.get_config("headline", "invitation",
                                                         "id_select_pictures_confirm_button")  # 选择图片确定按钮
    id_select_prefecture = utils.get_config("headline", "invitation", "id_select_prefecture")  # 选择专区
    id_select_prefecture_first = utils.get_config("headline", "invitation", "id_select_prefecture_first")  # 专区第一级
    id_select_prefecture_second = utils.get_config("headline", "invitation", "id_select_prefecture_second")  # 专区第二级
    id_select_topic = utils.get_config("headline", "invitation", "id_select_topic")  # 选择专题
    id_select_topic_name = utils.get_config("headline", "invitation", "id_select_topic_name")  # 选择专题的名字
    id_publish_text_invitation_button = utils.get_config("headline", "invitation",
                                                         "id_publish_text_invitation_button")  # 发布文字帖子按钮
    id_publish_video_invitation = utils.get_config("headline", "invitation",
                                                   "id_publish_video_invitation")  # 切换频帖子按钮
    id_upload_video = utils.get_config("headline", "invitation", "id_upload_video")  # 选择视频
    id_select_video = utils.get_config("headline", "invitation", "id_select_video")  # 选择视频确认按钮
    id_invitation_likes_button = utils.get_config("headline", "invitation", "id_invitation_likes_button")  # 点赞按钮
    id_invitation_remark_button = utils.get_config("headline", "invitation", "id_invitation_remark_button")  # 发布评论按钮
    id_invitation_remark_write_button = utils.get_config("headline", "invitation",
                                                         "id_invitation_remark_write_button")  # 写评论按钮
    id_invitation_remark_input_box = utils.get_config("headline", "invitation",
                                                      "id_invitation_remark_input_box")  # 评论输入框按钮
    id_invitation_remark_publish_button = utils.get_config("headline", "invitation",
                                                           "id_invitation_remark_publish_button")  # 发布评论按钮

    id_go_publish_button = utils.get_config("headline", "invitation", "id_go_publish_button")  # 去发帖按钮

    def __int__(self, driver):
        self.driver = driver

    # 发布文字贴
    def publish_text_invitation(self):
        self.bottom_navigation_bar_change("头条")
        self.element_click(By.ID, self.id_headline_community)
        self.element_click(By.ID, self.id_publish_invitation_button)
        self.element_click(By.ID, self.id_i_know_button)
        self.element_send_keys(By.ID, self.id_invitation_title_input_box, input_text="发个帖子看看20230221")
        self.element_send_keys(By.ID, self.id_invitation_content_input_box, input_text="输入个内容20230221")
        self.element_click(By.XPATH, self.xpath_upload_pictures)
        self.element_click(By.ID, self.id_select_pictures)
        self.element_click(By.ID, self.id_select_pictures_confirm_button)
        self.element_click(By.ID, self.id_select_prefecture)
        self.element_click(By.ID, self.id_select_prefecture_first)
        self.element_click(By.ID, self.id_select_prefecture_second)
        self.element_click(By.ID, self.id_select_topic)
        self.element_click(By.ID, self.id_select_topic_name)
        self.element_click(By.ID, self.id_publish_text_invitation_button)
        logger.info("文字帖发布成功")

    # 发布视频贴
    def publish_video_invitation(self, is_first_publish):
        if is_first_publish == "yes":
            self.bottom_navigation_bar_change("头条")
            self.element_click(By.ID, self.id_headline_community)
            self.element_click(By.ID, self.id_publish_invitation_button)
            self.element_click(By.ID, self.id_i_know_button)
        elif is_first_publish == "no":
            self.element_click(By.ID, self.id_go_publish_button)
        else:
            logger.info("{}的值输入有误".format(is_first_publish))
        self.element_click(By.ID, self.id_publish_video_invitation)
        self.element_click(By.ID, self.id_upload_video)
        self.element_click(By.ID, self.id_select_video)
        self.element_click(By.ID, self.id_select_pictures_confirm_button)
        self.element_send_keys(By.ID, self.id_invitation_title_input_box, input_text="发个视频看看20230221")
        self.element_click(By.ID, self.id_select_prefecture)
        self.element_click(By.ID, self.id_select_prefecture_first)
        self.element_click(By.ID, self.id_select_prefecture_second)
        self.element_click(By.ID, self.id_select_topic)
        self.element_click(By.ID, self.id_select_topic_name)
        self.element_click(By.ID, self.id_publish_text_invitation_button)
        logger.info("视频帖发布成功")

    # 帖子点赞
    def invitation_likes(self):
        self.element_click(By.ID, self.id_invitation_likes_button)
        logger.info("点赞成功")

    # 帖子评论
    def invitation_remark(self):
        self.element_click(By.ID, self.id_invitation_remark_button)
        self.element_click(By.ID, self.id_invitation_remark_write_button)
        self.element_send_keys(By.ID, self.id_invitation_remark_input_box, input_text="给你一个评论")
        self.element_click(By.ID, self.id_invitation_remark_publish_button)
        logger.info("评论成功")
