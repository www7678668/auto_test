# -- coding: utf-8 --
# @Time : 2023-02-07 9:37
# @Author : zhangwen
# @File : home_page.py
from Common.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy as By
from Common.utils import Utils
from PageObject.load_config import HomeLoadConfig
utils = Utils()  # 实例化工具类
logger = Utils().logs  # 实例化logger


# 主页面(有料)操作封装
class HomePage(BasePage):
    def __int__(self, driver):
        self.driver = driver

    # 切换底部标签
    def bottom_navigation_bar_change(self, bar_name):
        if bar_name == "头条":
            self.element_click(By.ID, HomeLoadConfig.id_headline)
        elif bar_name == "视频":
            self.element_click(By.ID, HomeLoadConfig.id_video)
        elif bar_name == "有料":
            self.element_click(By.ID, HomeLoadConfig.id_home)
        elif bar_name == "比赛":
            self.element_click(By.ID, HomeLoadConfig.id_match)
        elif bar_name == "我的":
            self.element_click(By.ID, HomeLoadConfig.id_my)
        else:
            logger.error("输入底部标签名称有误")

    # 有料标签切换
    def have_news_tab(self, tab_name):
        if tab_name == "热卖":
            self.element_click(By.ID, HomeLoadConfig.id_hot_sale)
        elif tab_name == "命中":
            self.element_click(By.ID, HomeLoadConfig.id_hit_plan)
        elif tab_name == "免费":
            self.element_click(By.ID, HomeLoadConfig.id_free_plan)
        else:
            logger.error("输入有料标签类型有误")

    # 购买方案
    def buy_plan(self, buy_number, is_expert_benefits=None):
        self.element_click(By.ID, HomeLoadConfig.id_home)  # 切换的有料页
        self.have_news_tab("命中")  # 切换到命中列表
        xpath_plan = "// *[@resource-id='com.inkr.sport:id/recyclerView']" \
                     "/android.view.ViewGroup[{}]/android.view.View[2]".format(buy_number)
        self.element_click(By.XPATH, xpath_plan)  # 点击第几个方案
        self.element_click(By.ID, HomeLoadConfig.id_i_know_button)  # 点击我知道啦按钮
        if is_expert_benefits == "yes":  # 判断有没有专家福利
            self.element_click(By.ID, HomeLoadConfig.id_publish_complete)
        else:
            logger.info("购买的方案无专家福利")
        self.element_click(By.ID, HomeLoadConfig.id_pay_now_button)  # 点击支付按钮
        self.element_click(By.ID, HomeLoadConfig.id_pay_now_gold_button)
        if is_expert_benefits == "yes":
            self.element_click(By.ID, HomeLoadConfig.id_publish_complete)
        else:
            logger.info("无需要点击我知啦按钮")
        self.element_click(By.ID, HomeLoadConfig.id_return_button)



if __name__ == '__main__':
    pass
