# -- coding: utf-8 --
# @Time : 2023-02-07 10:31
# @Author : zhangwen
# @File : my_page.py
import time

from appium.webdriver.common.mobileby import MobileBy as By
from Common.utils import Utils
from PageObject.home_page import HomePage
from Common.desired_cap import desired_cap
from appium.webdriver.common.appiumby import AppiumBy
utils = Utils()  # 实例化工具类
logger = Utils().logs

#我的页面所有操作
class MyPage(HomePage):
    id_go_logon_button = utils.get_config("my_page", "login", "id_go_logon_button")  # 去登录按钮
    id_verification_Code_login = utils.get_config("my_page", "login", "id_verification_Code_login")  # 验证码登录按钮
    id_phone_input_box = utils.get_config("my_page", "login", "id_phone_input_box")  # 手机号输入框
    id_verification_Code = utils.get_config("my_page", "login", "id_verification_Code")  # 验证码输入框
    id_account_password_login = utils.get_config("my_page", "login", "id_account_password_login")  # 切换账号密码登录按钮
    id_password_input_box = utils.get_config("my_page", "login", "id_password_input_box")  # 密码输入框按钮
    id_agree_Privacy_user_agreement_tick_box = utils.get_config("my_page", "login", "id_agree_Privacy_user_agreement_tick_box")  # 同意隐私协议按钮
    id_login_button = utils.get_config("my_page", "login", "id_login_button")  # 登录按钮
    id_my_is_expert_button = utils.get_config("my_page", "plan", "id_my_is_expert_button")  # 我是专家按钮
    id_publish_plan_button = utils.get_config("my_page", "plan", "id_publish_plan_button")  # 立即发布按钮
    id_plan_description_not_reminding_tick_box = utils.get_config("my_page", "plan", "id_plan_description_not_reminding_tick_box")  # 发布说明不再提醒选择选择框
    id_plan_description_now_publish_button = utils.get_config("my_page", "plan", "id_plan_description_now_publish_button")  # 发布说明的立即发布按钮
    id_i_know_button = utils.get_config("my_page", "plan", "id_i_know_button")  # 首次发布方案提示的我知道啦按钮
    id_select_match_button = utils.get_config("my_page", "plan", "id_select_match_button")  # 选择比赛按钮
    id_select_jingzu = utils.get_config("my_page", "plan", "id_select_jingzu")  # 选择竞足
    id_select_jinglan = utils.get_config("my_page", "plan", "id_select_jinglan")  # 选择竞篮
    xpath_first_match = utils.get_config("my_page", "plan", "xpath_first_match")  # 选择第一场比赛
    id_win_draw_fali_button = utils.get_config("my_page", "plan", "id_win_draw_fali_button")  # 切换北单胜负平
    # id_first_result = utils.get_config("my_page", "plan", "id_first_result")  # 选择第一个推荐结果
    # id_second_result = utils.get_config("my_page", "plan", "id_second_result")  # 选择第二个推荐结果
    # id_third_result = utils.get_config("my_page", "plan", "id_third_result")  # 选择第三个推荐结果
    id_odds = utils.get_config("my_page", "plan", "id_odds")  # 赔率
    id_other_play = utils.get_config("my_page", "plan", "id_other_play")  #其他玩法
    id_other_play_goal = utils.get_config("my_page", "plan", "id_other_play_goal")  # 其他玩法总比分
    id_other_play_confirm = utils.get_config("my_page", "plan", "id_other_play_confirm")  # 其他玩法弹窗确认按钮
    id_other_play_close = utils.get_config("my_page", "plan", "id_other_play_close")  # 其他玩法关闭按钮
    text_expert_benefits_cash = utils.get_config("my_page", "plan", "text_expert_benefits_cash")  # 专家福利现金
    text_expert_benefits_prize = utils.get_config("my_page", "plan", "text_expert_benefits_prize")  # 专家福利实物
    id_select_reward_button = utils.get_config("my_page", "plan", "id_select_reward_button")  # 专家福利选择福利按钮
    id_select_reward = utils.get_config("my_page", "plan", "id_select_reward")  # 专家福利的奖励
    id_expert_benefits_limit_number = utils.get_config("my_page", "plan", "id_expert_benefits_limit_number")  # 专家福利限制人数
    id_expert_benefits_no_limit_number = utils.get_config("my_page", "plan", "id_expert_benefits_no_limit_number")  # 专家福利不限制人数
    id_join_number_button = utils.get_config("my_page", "plan", "id_join_number_button")  # 专家福利添加参与人数按钮
    id_join_number_input_box = utils.get_config("my_page", "plan","id_join_number_input_box")  # 专家福利参与人数
    id_join_number_confirm_button = utils.get_config("my_page", "plan", "id_join_number_confirm_button")  # 专家福利选择人数后的确认按钮
    id_plan_title = utils.get_config("my_page", "plan", "id_plan_title")  # 方案标题框
    id_two_input_box = utils.get_config("my_page", "plan", "id_two_input_box")  # 二次弹出输入窗
    id_input_affirm_box = utils.get_config("my_page", "plan", "id_input_affirm_box")  # 二次弹出输入窗的确认按钮
    id_recommend_reason = utils.get_config("my_page", "plan", "id_recommend_reason")  # 推荐理由
    id_expert_analyse_content = utils.get_config("my_page", "plan", "id_expert_analyse_content")  # 专家分析内容框
    id_publish_button = utils.get_config("my_page", "plan", "id_publish_button")  # 立即发布按钮
    id_publish_success = utils.get_config("my_page", "plan", "id_publish_success")  # 立即发布按钮


    def __int__(self, driver):
        self.driver = driver

    #密码登录
    def login_password(self, account, password):
        self.element_click(By.ID, HomePage.personal_information_agree) #点击同意隐私协议
        self.left_slide(2) #左滑两次
        self.element_click(By.ID, HomePage.experience_now)
        self.element_click(By.ID, self.my)
        self.element_click(By.ID, self.id_go_logon_button)
        self.element_click(By.ID, self.id_account_password_login)
        #self.element_send_keys(By.ID, self.id_phone_input_box,input_text=account)
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.inkr.sport:id/etMobile")').send_keys(account)
        self.element_send_keys(By.ID, self.id_password_input_box,input_text=password)
        self.element_click(By.ID, self.id_agree_Privacy_user_agreement_tick_box)
        self.element_click(By.ID, self.id_login_button)
        logger.info("登录成功账号:{} 密码：{}".format(account, password))


    #获取用户信息的value, 未登录显示登录/注册，登录成功显示用户id
    def get_user_value(self):
        attribute_value = self.get_attribute_value("text", By.ID, self.id_go_logon_button)
        logger.info("用户信息的value为：" + attribute_value)
        return attribute_value


    #选择第几场比赛发布方案
    def select_mactch_number(self,number = 1):
        """
        第一场比赛从2开始，所以number需要默认加1
        默认选择第一场比赛
        """
        number = number+1
        xpath_match_number_element = '//*[@resource-id="com.inkr.sport:id/recyclerView"]/android.view.ViewGroup[{}]'.format(number)
        self.element_click(By.XPATH, xpath_match_number_element)
        logger.info("选择了第{}比赛".format(number))


    #选择北单，竞足，竞篮玩法
    def select_play_type(self,play_type = "beidan"):
        """
        :param play_type:默认北单，可以根据需求填写需要的参数（竞足、竞篮）
        :return:
        """
        if play_type == "jingzu":
            id_select_play_type = self.id_select_jingzu
        elif play_type == "jinglan":
            id_select_play_type = self.id_select_jinglan
        else:
            logger.error("输入玩法类型错误：{}".format(play_type))
            return "输入玩法类型错误"
        self.element_click(By.ID, id_select_play_type)
        logger.info("选择了{}玩法".format(play_type))


    #选择玩法推荐结果，包含主推次推
    def get_main_secondary_results(self, main = None, secondary = None, number=1):
        """
        获取第一个结果（first_odds），第二个结果（second_odds），第三个结果（third_odds）的赔率
        :param main: 主推的位置（1（主胜）, 2（平），3（客胜））
        :param secondary: 次推的位置（1（主胜）, 2（平），3（客胜））
        :param number:只有一个的时候选择，默认选择第一个结果，可设置第几个
        :return: 不能选择主推次推则则单选
        """
        time.sleep(2)
        if main == None and secondary == None:
            self.elements_click(By.ID, self.id_odds, number = number)  # 不能选择主推次推的情况，默认选择第一个
            return "选择结果成功"
        first_odds = float(self.find_elements(By.ID, self.id_odds)[1].get_attribute("text"))
        second_odds = float(self.find_elements(By.ID,  self.id_odds)[2].get_attribute("text"))
        third_odds = float(self.find_elements(By.ID,  self.id_odds)[3].get_attribute("text"))
        print(type(first_odds),second_odds, third_odds )

        if third_odds == None:
            logger.info("不能选择主推次推1")
            self.elements_click(By.ID, self.id_odds, number)     #不能选择主推次推的情况，默认选择第一个
        elif main == secondary:
            logger.info("主推次推不能选择同一个")
            self.elements_click(By.ID, self.id_odds, number)
        elif (first_odds>=2.1)+(second_odds>=2.1)+(third_odds>=2.1) >=2:  #如果三个赔率其中两个大于2.1，则可以选择主推次推
            n = 0
            odds_seat = []
            for i in(first_odds,second_odds, third_odds): #判断三个中，哪两个的值大于2.1
                n = n+1
                if i>2.1:
                    print(i)
                    odds_seat.append(n)  #把大于2.1的值的位置放在一个列表中
            print(odds_seat)
            if  main in odds_seat and  secondary in odds_seat:   #如果主推次推的位置
                #self.find_elements(By.ID,self.id_odds)[(main)].click()
                self.elements_click(By.ID,self.id_odds, number=main)
                #self.find_elements(By.ID,self.id_odds)[(secondary)].click()
                self.elements_click(By.ID, self.id_odds, number=secondary)
            else:
                logger.info("不能选择主推次推")
                self.elements_click(By.ID, self.id_odds, number = number)
        else:
            logger.info("不能选择主推次推")
            self.elements_click(By.ID, self.id_odds, number = number)

    #获取其他玩法xpth定位
    def get_other_play(self, score_type, score_value):
        if score_value != None:
            xpth_score_element = '//*[@resource-id="com.inkr.sport:id/llOdds"]' \
            '/android.view.ViewGroup[{}]/androidx.recyclerview.widget.RecyclerView[1]/android.view.ViewGroup[{}]'.format(score_type, score_value)
            return xpth_score_element
        else:
            return "score_value为空，不做任何操作"

    #选择其他玩法
    def select_other_play(self, other_play_type, other_play_number, score_type, score_value1, score_value2, goal1, goal2):
        """
        :param other_play_type: 其他玩法类型，0：总比分，1:总进球 2：总比分加总进球
        :param other_play_number:选择几个结果 1：选择一个 2：选择两个
        :param score_type: 比分的类型：0：主胜比分  1：平比分  2：客胜比分
        :param score_value1: 第一个比分，0 1 2 3 。。。依次类推（不是具体比分，是比分对应的位置）
        :param score_value2: 第二个比分，0 1 2 2 。。。依次类推（score_value1与score_value2不能相同）
        :param goal1: 第一个进球数：0 1 2 3 4 5 6 7（最多7个，7表示进球数7+）
        :param goal2: 第二个进球数：0 1 2 3 4 5 6 7（goal1与goal2不能相同）
        :return:
        """
        if other_play_type == 0 :
            self.elements_click(By.ID, self.id_other_play, number=0)  #点击比分玩法
            if other_play_number == 1:
                xpth_score_element = self.get_other_play(score_type, score_value1)
                self.element_click(By.ID, xpth_score_element)
                self.element_click(By.ID, self.id_other_play_confirm)
            elif other_play_number == 2:
                xpth_score_element1 = self.get_other_play(score_type, score_value1)
                self.element_click(By.ID, xpth_score_element1)
                xpth_score_element2 =self.get_other_play(score_type, score_value2)
                self.element_click(By.ID, xpth_score_element2)
                self.element_click(By.ID, self.id_other_play_confirm)
            else:
                logger.error("总比分次数选择错误-other_play_number")
        elif other_play_type == 1:
            self.elements_click(By.ID, self.id_other_play, number=1)
            if other_play_number == 1:
                self.elements_click(By.ID, self.id_other_play_goal, number=goal1)
                self.element_click(By.ID, self.id_other_play_confirm)
            if other_play_number == 2:
                self.elements_click(By.ID, self.id_other_play_goal, number=goal1)
                self.elements_click(By.ID, self.id_other_play_goal, number=goal2)
                self.element_click(By.ID, self.id_other_play_confirm)
            else:
                logger.error("总进球次数选择错误-other_play_number")
        elif other_play_type == 2:
            self.elements_click(By.ID, self.id_other_play, number=0)
            xpth_score_element1 = self.get_other_play(score_type, score_value1)
            self.element_click(By.ID, xpth_score_element1)
            xpth_score_element2 = self.get_other_play(score_type, score_value2)
            self.element_click(By.ID, xpth_score_element2)
            self.element_click(By.ID, self.id_other_play_confirm)
            self.elements_click (By.ID, self.id_other_play_goal, number=goal1)
            self.elements_click(By.ID, self.id_other_play_goal, number=goal2)
            self.element_click(By.ID, self.id_other_play_confirm)
        else:
            logger.error("其他玩法类型错误-other_play_type")


    #选择方案价格选择
    def select_play_price(self, price):
        """
        :param price: 0：免费  其他值为方案价格
        :return:
        """
        price_seat = 0
        if price == 38:
            price_seat = 1
        elif price == 58:
            price_seat = 2
        elif price == 68:
            price_seat = 3
        elif price == 88:
            price_seat = 4
        elif price == 128:
            price_seat = 5
        elif price == 188:
            price_seat = 6
        elif price == 288:
            price_seat = 7
        else:
            logger.error("输入价格错误")
        xpath_plan_price =  '// *[ @ resource - id = "com.inkr.sport:id/glPrice"] / android.view.ViewGroup[{}]'.format(price_seat)
        self.element_click(xpath_plan_price)


    #专家福利选择
    def select_expert_benefits(self, expert_benefits_type, is_no_limit_number, number = None ):
        if expert_benefits_type == "xianjin":
            self.element_click_uiautomator(self.text_expert_benefits_cash)
        elif expert_benefits_type == "shiwu":
            self.element_click_uiautomator(self.text_expert_benefits_prize)
        else:
            logger.error("输入专家福利类型有误")
        self.element_click(self.id_select_reward_button)
        self.elements_click(self.id_select_reward, number = 1)
        if is_no_limit_number =="is":
            self.element_click(By.ID,self.id_expert_benefits_limit_number)
            self.element_click(By.ID,self.id_join_number_button)
            self.element_send_keys(By.ID,self.id_join_number_input_box, input_text = number)
            self.element_click(By.ID, self.id_join_number_confirm_button)
        elif is_no_limit_number == "no":
            self.element_click(By.ID, self.id_expert_benefits_no_limit_number)
        else:
            logger.error("输入是否限制人数有误")



    #发布方案
    def publish_plan(self,account, password):
        self.login_password(account,password )
        self.element_click(By.ID, self.id_my_is_expert_button)
        self.element_click(By.ID, self.id_publish_plan_button)
        self.element_click(By.ID, self.id_plan_description_not_reminding_tick_box)
        self.element_click(By.ID, self.id_plan_description_now_publish_button)
        self.element_click(By.ID, self.id_i_know_button)
        self.element_click(By.ID, self.id_select_match_button)
        self.select_play_type("jingzu")
        self.select_mactch_number(3)
        self.get_main_secondary_results(2,3)
        self.select_other_play(2,2,1,1,1,1,1 )
        self.select_play_price(68)
        self.swipe_up()
        self.select_expert_benefits("xinjin","no")
        self.element_click(By.ID, self.id_plan_title)
        self.element_send_keys(By.ID,self.id_two_input_box, input_text="北单主胜测试方案发布01")
        self.element_click(By.ID, self.id_input_affirm_box)
        self.element_click(By.ID, self.id_recommend_reason)
        self.element_send_keys(By.ID, self.id_two_input_box, input_text="推荐好好爱护哦")
        self.element_click(By.ID, self.id_input_affirm_box)
        self.element_click(By.ID, self.id_expert_analyse_content)
        self.element_send_keys(By.ID, self.id_two_input_box, input_text="分析一下")
        self.element_click(By.ID, self.id_input_affirm_box)
        self.element_click(By.ID, self.id_publish_button)
        self.element_click(By.ID, self.id_publish_button) #立即发布二次确认
        logger.info("发布方案成功")

    # 获取发布成功的value, 等于发布成功，表示已跳转发布成功页面
    def get_publish_success_value(self):
        attribute_value = self.get_attribute_value("text", By.ID, self.id_go_logon_button)
        logger.info("用户信息的value为：" + attribute_value)
        return attribute_value

if __name__ == '__main__':
    a = MyPage()
    a.driver = desired_cap().desired_cap()
    a.publish_plan("13000000011", "abc123456")
    #print(a.select_mactch_number(1))
    #a.driver.find_elements()[1].click()
    #b = a.select_play_price(288)
    #print(b)
