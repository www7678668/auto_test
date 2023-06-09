# -*- coding:utf-8 -*-
# @Time : 2023-02-06 14:20
# @Author : zhangwen
# @File : home_page.py

import  os, sys

# 手机启动配置
from appium.webdriver import Remote  # 引入打开软件的包
from Common import utils


utils = utils.Utils()  # 实例化工具类
logger = utils.logs  # 实例化log对象


# app启动参数
class DesiredCap:
    @staticmethod
    def desired_cap(phone_model = "mumu"):
        platformName = utils.get_config("desired_cap", phone_model, "platformName")  # 获取platformName的值
        platformVersion = utils.get_config("desired_cap", phone_model, "platformVersion")  # 获取platformVersion的值
        deviceName = utils.get_config("desired_cap", phone_model, "deviceName")  # 获取deviceName的值
        automationName = utils.get_config("desired_cap", phone_model, "automationName") # 获取automationName的值
        appPackage = utils.get_config("desired_cap", phone_model, "appPackage")  # 获取appPackage的值
        appActivity = utils.get_config("desired_cap", phone_model, "appActivity") # 获取appActivity的值
        driver_url = utils.get_config("desired_cap", phone_model, "driver_url")  # 获取driver_url的值
        desired_cap = {"platformName": platformName,
                       "platformVersion": platformVersion,
                       "deviceName": deviceName,
                       "automationName": automationName,
                       "appPackage": appPackage,
                       "appActivity": appActivity
                       }
        logger.info("*********开始启动APP*********")
        logger.info("手机参数：{}".format(desired_cap))
        #warnings.filterwarnings("ignore", category=DeprecationWarning)
        driver = Remote(command_executor=driver_url, desired_capabilities=desired_cap)
        logger.info("*********启动成功*********")
        return driver


if __name__ == '__main__':
    a = DesiredCap().desired_cap()
