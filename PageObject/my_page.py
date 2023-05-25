# -- coding: utf-8 --
# @Time : 2023-02-07 10:31
# @Author : zhangwen
# @File : my_page.py
import time

from appium.webdriver.common.mobileby import MobileBy as By

from Common.utils import Utils
from PageObject.home_page import HomePage
from Common.desired_cap import DesiredCap

utils = Utils()  # 实例化工具类
logger = Utils().logs


# 我的页面所有操作
class MyPage(HomePage):
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

    def __int__(self, driver):
        self.driver = driver

    # 进入登录页面
    def go_login_page(self, is_first_login):
        if is_first_login != "no":
            self.element_click(By.ID, HomePage.id_personal_information_agree)  # 点击同意隐私协议
            self.left_slide(2)  # 左滑两次
            self.element_click(By.ID, HomePage.id_experience_now)
            self.element_click(By.ID, self.id_my)
            self.element_click(By.ID, self.id_go_logon_button)
        else:
            logger.info("不是第一次登录")

    # 密码登录
    def login_password(self, account, password, is_first_login=None):
        self.go_login_page(is_first_login)
        self.element_click(By.ID, self.id_account_password_login)
        self.element_send_keys(By.ID, self.id_phone_input_box, input_text=account)  # 账号输入
        self.element_send_keys(By.ID, self.id_password_input_box, input_text=password)  # 密码输入
        self.element_click(By.ID, self.id_agree_Privacy_user_agreement_tick_box)
        self.element_click(By.ID, self.id_login_button)
        logger.info("登录账号:{} 密码：{}".format(account, password))

    # 验证码登录
    def login_verification_code(self, account, verification_code, is_first_login=None):
        self.go_login_page(is_first_login)
        self.element_send_keys(By.ID, self.id_phone_input_box, input_text=account)
        self.element_click(By.ID, self.id_send_verification_code_button)
        self.element_send_keys(By.ID, self.id_verification_Code, input_text=verification_code)
        if is_first_login != "no":  # 第一次点击，非第一次不需要点同意
            self.element_click(By.ID, self.id_agree_Privacy_user_agreement_tick_box)
        else:
            logger.info("非第一次登录")
        self.element_click(By.ID, self.id_login_button)
        logger.info("登录账号:{} 验证码：{}".format(account, verification_code))

    # 获取登录页面的QQ登录元素id, 存在则说明登录失败，不存在说明登录成功
    def get_qq_login_value(self):
        attribute_value = self.get_attribute_value("resourceId", By.ID, self.id_login_qq)
        logger.info("用户信息的value为：" + attribute_value)
        return attribute_value

    # 获取用户信息的value, 未登录显示：登录/注册，登录成功显示用户id
    def get_user_value(self):
        attribute_value = self.get_attribute_value("resourceId", By.ID, self.id_go_logon_button)
        logger.info("用户信息的value为：" + attribute_value)
        return attribute_value

    # 选择第几场比赛发布方案
    def select_match_number(self, match_count):
        """
        xpath定位元素，改变的一组元素的下标的值，下标为我们的参数 match_count
        第一场比赛从2开始，所以match_count需要默认加1
        默认选择第一场比赛
        """
        match_count = match_count + 1  # 默认值从0开始，需要加1
        xpath_match_number_element1 = '//*[@resource-id="com.inkr.sport:id/recyclerView"]' \
                                      '/android.view.ViewGroup[{}]'.format(match_count)
        self.element_click(By.XPATH, xpath_match_number_element1)
        try:
            # 获取选择比赛草稿箱按钮text的值，正常说明选择比赛成功，异常就加1再去点击
            self.get_attribute_value("text", By.ID, "com.inkr.sport:id/tvDraft")
        except Exception as e:
            match_count = match_count + 1
            xpath_match_number_element2 = '//*[@resource-id="com.inkr.sport:id/recyclerView"]' \
                                          '/android.view.ViewGroup[{}]'.format(match_count)
            self.element_click(By.XPATH, xpath_match_number_element2)

    # 选择北单，竞足，竞篮玩法
    def select_play_type(self, play_type="北单", match_count=1, play_way="胜平负"):
        """
        :param play_type:  选择北单，竞足，竞篮玩法
        :param match_count: 第几场比赛
        :param play_way:   北单，竞足，竞篮玩法的方式，胜平负，带下分，胜负，让球胜负。。。
        :return:
        """
        if play_type == "北单":
            self.select_match_number(match_count=match_count)  # 点击北单标签
            if play_way is not None:
                self.element_click(By.XPATH, "//*[@text='{}']".format(play_way))  # 选择北单的玩法
            else:
                logger.info("选择玩法错误")
        elif play_type == "竞足":
            self.element_click(By.ID, self.id_select_jingzu)
            self.select_match_number(match_count=match_count)  # 点击竞足标签
            if play_way is not None:
                self.element_click(By.XPATH, "//*[@text='{}']".format(play_way))  # 选择竞足的玩法
            else:
                logger.info("选择玩法错误")
        elif play_type == "竞篮":
            self.element_click(By.ID, self.id_select_jinglan)  # 点击竞篮标签
            try:
                self.select_match_number(match_count=match_count)  # 竞篮没有比赛的时候，默认选择北单的比赛
            except:
                self.element_click(By.ID, self.id_select_beidan)
                self.select_match_number(match_count=match_count)
                self.element_click(By.XPATH, "//*[@text='{}']".format(play_way))  # 选择竞篮的玩法
                logger.info("选择竞篮失败，默认选择北单")
            if play_way is not None:
                self.element_click(By.XPATH, "//*[@text='{}']".format(play_way))
            else:
                logger.info("选择玩法错误")
        else:
            logger.error("输入玩法类型错误：{}".format(play_type))
        logger.info("选择的玩法类型：{}，选择了第{}场比赛，选择的玩法方式：{}".format(play_type, match_count, play_way))

    # 选择玩法推荐结果，包含主推次推
    def get_main_secondary_results(self, main=None, secondary=None):
        """
        获取第一个结果（first_odds），第二个结果（second_odds），第三个结果（third_odds）的赔率
        :param main: 主推的位置（1（主胜）, 2（平），3（客胜））
        :param secondary: 次推的位置（1（主胜）, 2（平），3（客胜））
        :param number:只有一个的时候选择，默认选择第一个结果，可设置第几个
        :return: 不能选择主推次推则则单选
        """
        if main is None and secondary is None:
            self.element_click(By.ID, self.id_first_result)  # 不能选择主推次推的情况，默认选择第一个
            logger.info("没有选择主推次推，单选一个结果")
        else:
            first_odds = float(self.find_elements(By.ID, self.id_odds)[1].get_attribute("text"))  # 获取第一个结果赔率
            second_odds = float(self.find_elements(By.ID, self.id_odds)[2].get_attribute("text"))  # 获取第二个结果赔率
            try:
                # 获取第三个结果赔率，为空则不能选择主推次推
                self.third_odds = float(self.find_elements(By.ID, self.id_odds)[3].get_attribute("text"))
            except Exception as e:
                logger.error("获取第三个元素失败，原因{}，默认选择第一个推荐结果".format(e))
            if self.third_odds is None:
                logger.info("不能选择主推次推1")
                self.element_click(By.ID, self.id_first_result)
            elif main == secondary:
                logger.info("主推次推不能选择同一个")
                self.element_click(By.ID, self.id_first_result)
            elif (first_odds >= 2.1) + (second_odds >= 2.1) + (
                    self.third_odds >= 2.1) >= 2:  # 如果三个赔率其中两个大于2.1，则可以选择主推次推
                n = 0
                odds_seat = []
                for i in (first_odds, second_odds, self.third_odds):  # 判断三个中，哪两个的值大于2.1
                    n = n + 1
                    if i > 2.1:
                        odds_seat.append(n)  # 把大于2.1的值的位置放在一个列表中
                if main in odds_seat and secondary in odds_seat:  # 主推次推的位置,两个值都在列表中（都大于2.1）
                    self.elements_click(By.ID, self.id_odds, number=main)
                    self.elements_click(By.ID, self.id_odds, number=secondary)
                else:
                    logger.info("不能选择主推次推2")
                    self.element_click(By.ID, self.id_first_result)
            else:
                logger.info("不能选择主推次推3")
                self.element_click(By.ID, self.id_first_result)

    # 获取其他玩法xpath定位其他玩法元素
    def get_other_play(self, score_type, score_value):
        """
        :param score_type:  其他玩法的比分玩法类型 1：主胜  2：平 3：客胜
        :param score_value:  选择第几个比分
        :return:
        """
        if score_value != None:
            xpth_score_element = '//*[@resource-id="com.inkr.sport:id/llOdds"]''/android.view.ViewGroup[{}]/androidx.' \
                                 'recyclerview.widget.RecyclerView[1]/android.view.ViewGroup[{}]'.format(score_type,
                                                                                                         score_value)

            return xpth_score_element
        else:
            return "score_value为空，不做任何操作"

    # 选择其他玩法
    def select_other_play(self, score_type=None,
                          score_value1=None,
                          score_value2=None,
                          goal1=None,
                          goal2=None):
        """
        :param score_type: 比分玩法类型 1：主胜  2：平 3：客胜
        :param score_value1:  第一个比分，0 1 2 3 4.。。代表比分对应的位置
        :param score_value2:  第二个比分
        :param goal1:  第一个总进球。0 1 2 3 4.。。代表总进球对应的位置
        :param goal2: 第二个总进球
        :return:
        """
        if score_type == None:
            logger.info("不选择其他玩法")
        else:
            self.element_click(By.ID, self.id_other_play)  # 点击比分，根据比分和进球参数是否为空，来选择对应的其他的玩法
            if score_value1 != None:  # score_value1不为空，则选择第一个比分，可根据参数选择第一个还是两个，为空不会操作点击
                xpth_score_element1 = self.get_other_play(score_type, score_value1)
                self.element_click(By.XPATH, xpth_score_element1)
            if score_value2 != None:  # score_value2不为空，则选择第二个比分
                xpth_score_element2 = self.get_other_play(score_type, score_value2)
                self.element_click(By.XPATH, xpth_score_element2)
            if score_value1 == None and score_value2 == None:  # 如果都为空，点击关闭按钮
                self.element_click(By.ID, self.id_other_play_close)
                logger.info("没有选择比分玩法")
            else:  # 不是都为空，点击确认按钮
                self.element_click(By.ID, self.id_other_play_confirm)
                logger.info("总比分玩法选择成功")
            self.element_click(By.ID, self.id_other_play)  # 点击进球
            if goal1 != None:  # goal1不为空，则选择第第一个进球
                self.elements_click(By.ID, self.id_other_play_goal, number=goal1)
            if goal2 != None:  # goal2如果不为空，则选择第第二个进球
                self.elements_click(By.ID, self.id_other_play_goal, number=goal2)
            if goal1 == None and goal2 == None:  # 如果都为空，点击关闭按钮
                self.element_click(By.ID, self.id_other_play_close)
                logger.info("没有选择总进球玩法")
            else:  # 不是都为空，点击确认按钮
                self.element_click(By.ID, self.id_other_play_confirm)
                logger.info("总进球玩法选择成功")
            logger.info("其他玩法选择完成")

    # 选择促销规则
    def select_promotion_Information(self, promotion_type=None):
        """
        :param promotion_type: 促销类型： 0 首单不中退  1 不中退
        :return:
        """
        if promotion_type == None:
            logger.info("不选择促销信息")
        elif promotion_type == 0:
            self.element_click(By.ID, self.id_first_no_hit_refund_radio)
        elif promotion_type == 1:
            self.element_click(By.ID, self.id_no_hit_refund_radio)
        else:
            logger.error("输入的促销类型有误")

    # 选择方案价格选择
    def select_play_price(self, price):
        """
        :param price: 0：免费  其他值为方案价格
        :return:
        """
        price_seat = 0
        if price == 0:
            price_seat = 1
        elif price == 38:
            price_seat = 2
        elif price == 58:
            price_seat = 3
        elif price == 68:
            price_seat = 4
        elif price == 88:
            price_seat = 5
        elif price == 128:
            price_seat = 6
        elif price == 188:
            price_seat = 7
        elif price == 288:
            price_seat = 8
        else:
            logger.error("输入价格错误")
        xpath_plan_price = '//*[@resource-id ="com.inkr.sport:id/glPrice"]/android.view.ViewGroup[{}]'.format(
            price_seat)
        self.element_click(By.XPATH, xpath_plan_price)

    # 专家福利选择
    def select_expert_benefits(self, expert_benefits_type=None, is_no_limit_number=None, number=None):
        """
        :param expert_benefits_type: 专家福利类型；xianjin--现金   shiwu--实物
        :param is_no_limit_number: is--限制人数   no-不限制人数
        :param number: 限制几人
        :return:
        """
        if expert_benefits_type == None:  # 为none不需要选择专家福利，否者就走专家福利流程
            logger.info("不选择专家福利")
        else:
            if expert_benefits_type == "现金":  # 现金
                self.element_click_uiautomator(self.text_expert_benefits_cash)
            elif expert_benefits_type == "实物":  # 实物
                self.element_click_uiautomator(self.text_expert_benefits_prize)
            else:
                logger.error("输入专家福利类型有误")
            self.element_click(By.ID, self.id_select_reward_button)
            self.elements_click(By.ID, self.id_select_reward, number=1)  # 选择第几个奖励。默认选择第一个即可
            if is_no_limit_number == "yes":  # 限制人数
                self.element_click(By.ID, self.id_expert_benefits_limit_number)
                self.element_click(By.ID, self.id_join_number_button)
                self.element_send_keys(By.ID, self.id_join_number_input_box, input_text=number)
                self.element_click(By.ID, self.id_join_number_confirm_button)
            elif is_no_limit_number == "no":  # 不限制人数
                self.element_click(By.ID, self.id_expert_benefits_no_limit_number)
            else:
                logger.error("输入是否限制人数有误")

    # 发布方案
    def publish_plan(self,
                     match_count,
                     play_price,
                     plan_title,
                     recommend_reason,
                     expert_analyse_content,
                     first=None,
                     play_type=None,
                     play_way=None,
                     mian=None, secondary=None,
                     score_type=None,
                     score_value1=None,
                     score_value2=None,
                     goal1=None,
                     goal2=None,
                     promotion_type=None,
                     expert_benefits_type=None,
                     is_no_limit_number=None,
                     expert_benefits_number=None,
                     ):
        """
        综合发布方案需要的一些方案，让我们更简单发布多种不同的方案
        :param match_count: 第几场比赛
        :param play_price:  方案价格
        :param plan_title:  方案标题
        :param recommend_reason: 推荐理由
        :param expert_analyse_content: 方案内容
        :param play_type: 竞彩类型，北单、竞足、竞篮
        :param play_way:  北单、竞足、竞篮的结果方式，胜平负、大小分，胜负。。。
        :param mian: 主推
        :param secondary: 次推
        :param score_type: 比分玩法类型 比分玩法类型 1：主胜  2：平 3：客胜
        :param score_value1: 第一次选择第几个比分
        :param score_value2:第二次选择第几个比分
        :param goal1: 第一次选择第几个总进球数
        :param goal2: 第二次选择第几个总进球数 -可以组合选择，不需要就不用填写该参数
        :param expert_benefits_type: 专家福利类型： 现金 红包 --不选择专家福利，以下三个参数不用填写
        :param is_no_limit_number:  是否限制人数
        :param expert_benefits_number: 限制多少人
        :return:
        """
        if first == None:    # 默认从打开app开始，不为 none 直接可以点击发布方案
            self.element_click(By.ID, self.id_my_is_expert_button)  # 点击我是专家
            self.element_click(By.ID, self.id_publish_plan_button)  # 点击立即发布
            self.element_click(By.ID, self.id_plan_description_not_reminding_tick_box)  # 勾选发布说明不再提醒
            self.element_click(By.ID, self.id_plan_description_now_publish_button)  # 点击发布说明的立即发布
            self.element_click(By.ID, self.id_i_know_button)  # 点击提示信息的我知道啦
        else:
            self.element_click(By.ID, self.id_publish_button)  # 点击方案管理的立即发布
            logger.info("非首次发布，可以直接选择比赛")
        self.element_click(By.ID, self.id_select_match_button)  # 点击选择比赛按钮
        self.select_play_type(play_type, match_count=match_count, play_way=play_way)  # 选择比赛
        self.get_main_secondary_results(main=mian, secondary=secondary)  # 选择主推次推
        self.select_other_play(score_type, score_value1, score_value2, goal1, goal2)  # 选择其他玩法
        self.select_play_price(play_price)  # 输入方案价格
        self.swipe_up()  # 上滑
        self.select_promotion_Information(promotion_type)  # 促销信息选择
        self.select_expert_benefits(expert_benefits_type, is_no_limit_number, expert_benefits_number)  # 选择专家福利
        self.element_click(By.ID, self.id_plan_title)  # 点击方案标题输入框
        self.element_send_keys(By.ID, self.id_two_input_box, input_text=plan_title)  # 输入方案标题
        self.element_click(By.ID, self.id_input_affirm_box)  # 点击方案标题确认按钮
        self.element_click(By.ID, self.id_recommend_reason)  # 推荐理由
        self.element_send_keys(By.ID, self.id_two_input_box, input_text=recommend_reason)
        self.element_click(By.ID, self.id_input_affirm_box)
        self.element_click(By.ID, self.id_expert_analyse_content)  # 方案内容
        self.element_send_keys(By.ID, self.id_two_input_box, input_text=expert_analyse_content)
        self.element_click(By.ID, self.id_input_affirm_box)
        self.element_click(By.ID, self.id_publish_button)  # 立即发布按钮
        self.element_click(By.ID, self.id_publish_button)  # 立即发布二次确认
        logger.info("发布方案成功")

    # 点击发布成功后的完成按钮
    def click_complete_button(self):
        self.element_click(By.ID, self.id_publish_complete)

    # 获取发布成功的value, 等于发布成功，表示已跳转发布成功页面
    def get_publish_success_value(self):
        attribute_value = self.get_attribute_value("text", By.ID, self.id_publish_success)
        logger.info("用户信息的value为：" + attribute_value)
        return attribute_value

    # 返回我的页面
    def return_my_page(self):
        self.element_click(By.ID, self.id_return_button)
        self.element_click(By.ID, self.id_return_button)
        self.bottom_navigation_bar_change("我的")

    # 在我的页面退出登录
    def logout_my_page(self):
        self.element_click(By.ID, self.id_setting_button)
        self.element_click(By.ID, self.id_logout_button)
        self.element_click(By.ID, self.id_logout_confirm_button)


if __name__ == '__main__':
    from selenium.webdriver.support.ui import WebDriverWait

    from selenium.webdriver.support import expected_conditions as ec

    a = MyPage()
    a.driver = DesiredCap().desired_cap()
    # a.login_password("13000000012", "abc123456")
    a.login_verification_code("13000000012", "123456")
    a.publish_plan(play_type="竞篮",
                   play_way="胜平负",
                   match_count=2,
                   # score_type = 2,
                   # score_value1 = 1,
                   # goal1 = 5,
                   play_price=0,
                   # expert_benefits_type = "现金",
                   # is_no_limit_number = "no" ,
                   mian=1,
                   secondary=2,
                   promotion_type=1,
                   plan_title="发布一个篮球方案打个66666",
                   recommend_reason="推荐",
                   expert_analyse_content="555")
    # print(a.get_publish_success_value())
    # print(a.select_mactch_number(1))
    # a.driver.find_elements()[1].click()
    # a.driver.find_element().get_attribute()
    # b = a.select_play_price(288)
