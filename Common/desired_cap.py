#-*- coding:utf-8 -*-
# @Time : 2023-02-06 14:20
# @Author : zhangwen
# @File : home_page.py

#手机启动配置
from appium.webdriver import Remote  #引入打开软件的包
import configparser  #导入配置读取的包
from Common import utils
import warnings

utils = utils.Utils()  #实例化工具类
logger = utils.logs   #实例化log对象
platformName = utils.get_config("desired_cap", "desired_cap", "platformName"); #获取platformName的值
platformVersion = utils.get_config("desired_cap", "desired_cap", "platformVersion"); #获取platformVersion的值
deviceName = utils.get_config("desired_cap", "desired_cap", "deviceName"); #获取deviceName的值
automationName = utils.get_config("desired_cap", "desired_cap", "automationName"); #获取utomationName的值
appPackage = utils.get_config("desired_cap", "desired_cap", "appPackage"); #获取appPackage的值
appActivity = utils.get_config("desired_cap", "desired_cap", "appActivity"); #获取appActivity的值
driver_url = utils.get_config("desired_cap", "desired_cap", "driver_url"); #获取driver_url的值


class desired_cap:
    #app启动参数
    def desired_cap(self):
        desired_cap = {}
        desired_cap["platformName"] =platformName    # 手机系统
        desired_cap["platformName"] = platformName    # 手机系统版本
        desired_cap["deviceName"] = deviceName        # 手机的名字，不会进行校验，但是没有会报错
        desired_cap["automationName"] = automationName # 自动化测试框架 （1.4以上的appium不用写）
        desired_cap["appPackage"] = appPackage         # app包名
        desired_cap["appActivity"] = appActivity      # app的启动页面
        logger.info("*********开始启动APP*********")
        logger.info("手机参数：{}".format(desired_cap))
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        driver = Remote(command_executor=driver_url, desired_capabilities=desired_cap)
        logger.info("*********启动成功*********")
        return driver


if __name__ == '__main__':
    a = desired_cap().desired_cap()


