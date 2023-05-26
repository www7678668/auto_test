#-*- coding:utf-8 -*-
# @Time : 2023-02-07 9:37
# @Author : zhangwen
# @File : home_page.py

import configparser
import logging
import time
from Common.AllPath import *
import shutil
import os, sys

# 工具类实现
class Utils:
    # 读取配置文件的方法
    def get_config(self,filename, config_name, config_key):
        """
        :param filename:  配置文件名称
        :param config_name: 配置项名称
        :param config_key: 配置项key的值
        :return: 配置项key对应的value值
        """
        conf_path = os.path.join(config_path, filename+".ini")  # config文件路径，包含文件名
        sys.path.append(conf_path)
        conf = configparser.ConfigParser()
        conf.read(conf_path, encoding="utf-8")
        config = conf.get(config_name, config_key)  # 获取配置key对应的值
        return config

    # 打印日志
    @property
    def logs(self):
        logger = logging.getLogger("")
        logger.setLevel(logging.INFO)   # 设置输出日志的最低等级
        if not logger.handlers:          # 判断logger.handlers是否存在，不存在新建，存在直接返回，无此判断会有日志重复问题
            formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s", "%Y-%m-%d %H:%M:%S")  # 设置日志格式
            log_name = f'{time.strftime("%Y-%m-%d", time.localtime())}.log'  # 日志日志名称，日期加名字
            SH = logging.StreamHandler()  # 控制台输出
            FH = logging.FileHandler(os.path.join(Log_path, log_name), encoding="UTF-8")  # 文件输出
            logger.addHandler(SH)  # 控制台加载
            logger.addHandler(FH)  # 文件加载
            SH.setFormatter(formatter)  # 输出到控制台
            FH.setFormatter(formatter)  # 输出到文件
        return logger  # 返回logger对象

    # 辅助allure生成历史数据的趋势图，把每次结果复制到 history 目录下
    @staticmethod
    def copy_history():
        ALLURE_REPORT = os.path.join(report_path, "allure-report")
        ALLURE_RESULTS = os.path.join(report_path, "allure-result")
        start_path = os.path.join(ALLURE_REPORT, 'history')
        end_path = os.path.join(ALLURE_RESULTS, 'history')
        if os.path.exists(end_path):
            shutil.rmtree(end_path)
            print("复制上一运行结果成功！")
        try:
            shutil.copytree(start_path, end_path)
        except FileNotFoundError:
            print("allure没有历史数据可复制！")


if __name__ == '__main__':
    a = Utils()
    a.copy_history()

