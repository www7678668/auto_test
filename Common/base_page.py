#-*- coding:utf-8 -*-
# @Time : 2023-02-06 11:32
# @Author : zhangwen
# @File : home_page.py

#appium操作元素基础封装
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Common.desired_cap import desired_cap
from appium.webdriver.common.mobileby import MobileBy as By
from Common.utils import Utils
from appium.webdriver.common.appiumby import AppiumBy

logger = Utils().logs

class BasePage:
    def __int__(self, driver):
        self.driver = driver

    #定位元素
    def find_element(self, *locator):
        try:
            element = WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(*locator))
            #element =  self.driver.find_element(*locator)
            logger.info("查找元素'{}'完成".format(locator))
            return element
        except Exception as e:
            logger.error("获取元素'{}'失败，原因：{}".format(locator, e))

    #定位一组元素
    def find_elements(self, *locator):
        return  self.driver.find_elements(*locator)

    #一组元素点击
    def elements_click(self, *locator,number):
        """
        :param locator:
        :param number: 需要点击第几个元素，默认点击第一个
        :return:
        """
        if number != None:
            self.find_elements(*locator)[number].click()
            logger.info("点击元素'{}'完成".format(locator))
        else:
            return "number为空，不做任何操作"

    #元素点击
    def element_click(self, *locator):
        self.find_element(locator).click()
        logger.info("点击元素'{}'完成".format(locator))

    #输入内容
    def element_send_keys(self, *locator, input_text):
        self.find_element(locator).send_keys(input_text)

    # uiautomator定位元素
    def find_element_uiautomator(self, text):
        """
        :param text: text元素名称
        :return:
        """
        try:
            element = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("{}")'.format(text))
            logger.info("查找元素'{}'完成".format(text))
            return element
        except Exception as  e:
            logger.error("获取text元素'{}'失败，原因：{}".format(text, e))


    # uiautomator点击
    def element_click_uiautomator(self, text):
        self.find_element_uiautomator(text).click()
        logger.info("点击元素'{}'完成".format(text))

    # uiautomator输入
    def element_send_keys_uiautomator(self, text, input_text):
        self.find_element_uiautomator(text).send_keys(input_text)

    #获取手机屏幕宽，高
    def get_screen_size(self):
        screen_size = self.driver.get_window_size()
        return screen_size

    #获取元素的value值
    def get_attribute_value(self,attr,*locator):
        return self.find_element(locator).get_attribute(attr)

    #左滑
    def left_slide(self, count = 1, t = 100):
        """
        :param count: 滑动次数，默认1
        :param t: 滑动时间，默认100ms
        :return:
        """
        screen_size = self.get_screen_size()
        logger.info("开始左滑")
        x1 = screen_size['width'] * 0.95
        y1 = screen_size['height'] * 0.5
        x2 = screen_size['width'] * 0.15
        for i in range(count):
            time.sleep(1)
            self.driver.swipe(x1, y1, x2, y1, t)
            logger.info("左滑{}次".format(i+1))
        logger.info("左滑完成")

    # 右滑
    def swipe_right(self,count = 1, t = 100):
        """
        :param count: 滑动次数，默认1
        :param t: 滑动时间，默认100ms
        :return:
        """
        screen_size = self.get_screen_size()
        logger.info("开始右滑")
        x1 = screen_size['width'] * 0.25
        y1 = screen_size['height'] * 0.5
        x2 = screen_size['width'] * 0.75
        for i in range(count):
            time.sleep()
            self.driver.swipe(x1, y1, x2, y1, t)
        logger.info("右滑完成")

    # 上滑
    def swipe_up(self, count = 1, t = 100):
        """
        :param count: 滑动次数，默认1
        :param t: 滑动时间，默认100ms
        :return:
        """
        screen_size = self.get_screen_size()
        logger.info("开始上滑")
        x1 = screen_size['width'] * 0.5
        y1 = screen_size['height'] * 0.75
        y2 = screen_size['height'] * 0.25
        for i in range(count):
            self.driver.swipe(x1, y1, x1, y2, t)
        logger.info("上滑完成")

    # 下滑
    def swipe_down(self, count = 1, t = 100):
        """
        :param count: 滑动次数，默认1
        :param t: 滑动时间，默认100ms
        :return:
        """
        screen_size = self.get_screen_size()
        logger.info("开始下滑")
        x1 = screen_size['width'] * 0.5
        y1 = screen_size['height'] * 0.25
        y2 = screen_size['height'] * 0.75
        for i in range(count):
            self.driver.swipe(x1, y1, x1, y2, t)
        logger.info("下滑完成")



if __name__ == '__main__':
    a = BasePage()
    # a.driver = desired_cap().desired_cap()
    # a.element_click(By.ID,"com.inkr.sport:id/tvPopAgreementAgree")
    # a.left_slide(count=2)
    # a.element_click(By.ID, "com.inkr.sport:id/ivEnterApp")
    # a.element_click(By.ID, "com.inkr.sport:id/ivTbMine")
    # #a.find_element(By.ID,"com.inkr.sport:id/tvUserName").click()
    # b = a.get_text_value("text",By.ID, "com.inkr.sport:id/tvUserName",)
    # print(b)
    logger.info("555")

    #
    # a.element_click(By.ID, "com.inkr.sport:id/tvUserName")
    # a.element_click_uiautomator("账号密码登录")
    # a.element_send_keys_uiautomator("请输入手机号", "13000000000")
    # a.element_send_keys_uiautomator("请输入密码", "abc123456")
    # a.element_click(By.ID, "com.inkr.sport:id/ivPolicyCheckBox")
    # a.element_click(By.ID,"com.inkr.sport:id/btLogin")
