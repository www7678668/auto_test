# -- coding: utf-8 --
# @Time : 2023-06-09 16:17
# @Author : zhangwen
# @File : load_config.py
# 把每个页面加载元素config的方法放在一个目录下多个class

from Common.utils import Utils

utils = Utils()  # 实例化工具类
logger = Utils().logs  # 实例化logger


# 主页面（有料）
class HomeLoadConfig:
    id_personal_information_agree = utils.get_config("home_page", "bottom_navigation_bar",
                                                     "id_personal_information_agree")  # 个人信息统一按钮
    id_experience_now = utils.get_config("home_page", "bottom_navigation_bar", "id_experience_now")  # 立即体验按钮
    id_my = utils.get_config("home_page", "bottom_navigation_bar", "id_my")  # 我的按钮
    id_match = utils.get_config("home_page", "bottom_navigation_bar", "id_match")  # 比赛按钮
    id_home = utils.get_config("home_page", "bottom_navigation_bar", "id_home")  # 我的有料按钮
    id_video = utils.get_config("home_page", "bottom_navigation_bar", "id_video")  # 视频按钮
    id_headline = utils.get_config("home_page", "bottom_navigation_bar", "id_headline")  # 头条按钮
    id_hot_sale = utils.get_config("home_page", "youliao", "id_hot_sale")  # 热卖
    id_hit_plan = utils.get_config("home_page", "youliao", "id_hit_plan")  # 命中
    id_free_plan = utils.get_config("home_page", "youliao", "id_free_plan")  # 免费
    id_i_know_button = utils.get_config("home_page", "youliao", "id_i_know_button")  # 购买方案提示的我知道啦按钮
    id_pay_now_button = utils.get_config("home_page", "youliao", "id_pay_now_button")  # 列表的立即支付按钮
    id_pay_now_gold_button = utils.get_config("home_page", "youliao", "id_pay_now_gold_button")  # 详情的立即支付按钮
    id_publish_complete = utils.get_config("my_page", "plan", "id_publish_complete")  # 专家福利我怕知道啦按钮
    id_return_button = utils.get_config("my_page", "login", "id_return_button")  # 返回上一页 按钮


# 我的页面
class MyLoadConfig:
    id_go_logon_button = utils.get_config("my_page", "login", "id_go_logon_button")  # 去登录按钮
    id_verification_code_login = utils.get_config("my_page", "login", "id_verification_code_login")  # 验证码登录按钮
    id_phone_input_box = utils.get_config("my_page", "login", "id_phone_input_box")  # 手机号输入框
    id_verification_Code = utils.get_config("my_page", "login", "id_verification_Code")  # 验证码输入框
    id_send_verification_code_button = utils.get_config("my_page", "login",
                                                        "id_send_verification_code_button")  # 验证码发送按钮
    id_account_password_login = utils.get_config("my_page", "login", "id_account_password_login")  # 切换账号密码登录按钮
    id_password_input_box = utils.get_config("my_page", "login", "id_password_input_box")  # 密码输入框按钮
    id_agree_Privacy_user_agreement_tick_box = utils.get_config("my_page", "login",
                                                                "id_agree_Privacy_user_agreement_tick_box")  # 同意隐私协议按钮
    id_login_button = utils.get_config("my_page", "login", "id_login_button")  # 登录按钮
    id_setting_button = utils.get_config("my_page", "login", "id_setting_button")  # 设置按钮
    id_logout_button = utils.get_config("my_page", "login", "id_logout_button")  # 退出登录按钮
    id_my_is_expert_button = utils.get_config("my_page", "plan", "id_my_is_expert_button")  # 我是专家按钮
    id_publish_plan_button = utils.get_config("my_page", "plan", "id_publish_plan_button")  # 立即发布按钮
    id_plan_description_not_reminding_tick_box = utils.get_config("my_page", "plan",
                                                                  "id_plan_description_not_reminding_tick_box")  # 发布说明不再提醒选择选择框
    id_plan_description_now_publish_button = utils.get_config("my_page", "plan",
                                                              "id_plan_description_now_publish_button")  # 发布说明的立即发布按钮
    id_i_know_button = utils.get_config("my_page", "plan", "id_i_know_button")  # 首次发布方案提示的我知道啦按钮
    id_select_match_button = utils.get_config("my_page", "plan", "id_select_match_button")  # 选择比赛按钮
    id_select_jingzu = utils.get_config("my_page", "plan", "id_select_jingzu")  # 选择竞足
    id_select_beidan = utils.get_config("my_page", "plan", "id_select_beidan")  # 选择北单
    id_select_jinglan = utils.get_config("my_page", "plan", "id_select_jinglan")  # 选择竞篮
    xpath_first_match = utils.get_config("my_page", "plan", "xpath_first_match")  # 选择第一场比赛
    id_first_result = utils.get_config("my_page", "plan", "id_first_result")  # 选择第一个推荐结果
    # id_second_result = utils.get_config("my_page", "plan", "id_second_result")  # 选择第二个推荐结果
    # id_third_result = utils.get_config("my_page", "plan", "id_third_result")  # 选择第三个推荐结果
    id_odds = utils.get_config("my_page", "plan", "id_odds")  # 赔率
    id_other_play = utils.get_config("my_page", "plan", "id_other_play")  # 其他玩法
    id_other_play_goal = utils.get_config("my_page", "plan", "id_other_play_goal")  # 其他玩法总比分
    id_other_play_confirm = utils.get_config("my_page", "plan", "id_other_play_confirm")  # 其他玩法弹窗确认按钮
    id_other_play_close = utils.get_config("my_page", "plan", "id_other_play_close")  # 其他玩法关闭按钮
    id_first_no_hit_refund_radio = utils.get_config("my_page", "plan", "id_first_no_hit_refund_radio")  # 首单不中退
    id_no_hit_refund_radio = utils.get_config("my_page", "plan", "id_no_hit_refund_radio")  # 不中退
    text_expert_benefits_cash = utils.get_config("my_page", "plan", "text_expert_benefits_cash")  # 专家福利现金
    text_expert_benefits_prize = utils.get_config("my_page", "plan", "text_expert_benefits_prize")  # 专家福利实物
    id_select_reward_button = utils.get_config("my_page", "plan", "id_select_reward_button")  # 专家福利选择福利按钮
    id_select_reward = utils.get_config("my_page", "plan", "id_select_reward")  # 专家福利的奖励
    id_expert_benefits_limit_number = utils.get_config("my_page", "plan",
                                                       "id_expert_benefits_limit_number")  # 专家福利限制人数
    id_expert_benefits_no_limit_number = utils.get_config("my_page", "plan",
                                                          "id_expert_benefits_no_limit_number")  # 专家福利不限制人数
    id_join_number_button = utils.get_config("my_page", "plan", "id_join_number_button")  # 专家福利添加参与人数按钮
    id_join_number_input_box = utils.get_config("my_page", "plan", "id_join_number_input_box")  # 专家福利参与人数
    id_join_number_confirm_button = utils.get_config("my_page", "plan",
                                                     "id_join_number_confirm_button")  # 专家福利选择人数后的确认按钮
    id_plan_title = utils.get_config("my_page", "plan", "id_plan_title")  # 方案标题框
    id_two_input_box = utils.get_config("my_page", "plan", "id_two_input_box")  # 二次弹出输入窗
    id_input_affirm_box = utils.get_config("my_page", "plan", "id_input_affirm_box")  # 二次弹出输入窗的确认按钮
    id_recommend_reason = utils.get_config("my_page", "plan", "id_recommend_reason")  # 推荐理由
    id_expert_analyse_content = utils.get_config("my_page", "plan", "id_expert_analyse_content")  # 专家分析内容框
    id_publish_button = utils.get_config("my_page", "plan", "id_publish_button")  # 立即发布按钮
    id_publish_success = utils.get_config("my_page", "plan", "id_publish_success")  # 发布完成按钮
    id_publish_complete = utils.get_config("my_page", "plan", "id_publish_complete")  # 发布完成按钮
    id_return_button = utils.get_config("my_page", "login", "id_return_button")  # 返回上一页 按钮
    id_logout_confirm_button = utils.get_config("my_page", "login", "id_logout_confirm_button")  # 退出登录确认按钮
    id_login_qq = utils.get_config("my_page", "plan", "id_login_qq")  # QQd登录按钮
    third_odds = None


# 头条页面
class HeadLoadConfig:
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
