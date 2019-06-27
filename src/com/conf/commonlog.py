#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
import os.path
import time
import sys
# 改写自:https://blog.csdn.net/xugexuge/article/details/87916020
"""
import logging

from colorama import Fore, Style

from common_config import CommonConf


class Logger(object):

    def __init__(self, class_name=""):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
        将日志存入到指定的文件中
        :param logger:  定义对应的程序模块名name，默认为root
        """
        # 创建一个logger
        self.logger = logging.getLogger()

        # self.logger.setLevel(logging.DEBUG)  # 指定最低的日志级别 critical > error > warning > info > debug

        # 实例化对象，传递日志路径
        com = CommonConf(class_name)
        self.log_url = com.set_log_conf()

        # 配置输出时间的格式，注意月份和天数不要搞乱了
        DATE_FORMAT = '%Y-%m-%d %H:%M:%S %a '

        # 配置log基础设置
        """
        filename: 指定日志文件名
        filemode: 和file函数意义相同，指定日志文件的打开模式，'w'或'a'
        format: 指定输出的格式和内容，format可以输出很多有用信息，如上例所示:
         %(levelno)s: 打印日志级别的数值
         %(levelname)s: 打印日志级别名称
         %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
         %(filename)s: 打印当前执行程序名
         %(funcName)s: 打印日志的当前函数
         %(lineno)d: 打印日志的当前行号
         %(asctime)s: 打印日志的时间
         %(thread)d: 打印线程ID
         %(threadName)s: 打印线程名称
         %(process)d: 打印进程ID
         %(message)s: 打印日志信息
        datefmt: 指定时间格式，同time.strftime()
        level: 设置日志级别，默认为logging.WARNING
        """
        logging.basicConfig(level=logging.DEBUG,
                            format=" -- %(filename)s -- [%(asctime)s] -- [%(message)s]",
                            datefmt=DATE_FORMAT,
                            # 有了filename参数就不会直接输出显示到控制台，而是直接写入文件
                            filename=self.log_url
                            )
        """
        # 创建一个handler，用于写入日志文件
        rq = time.strftime("<%Y-%m-%d_%H-%M-%S>", time.localtime(time.time()))
        log_path = os.getcwd() + "/logs/"
        log_name = log_path + rq + ".log"
        #  这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志，解决重复打印的问题
        if not self.logger.handlers:
            # 创建一个handler，用于输出到控制台
            ch = logging.StreamHandler(sys.stdout)
            ch.setLevel(logging.DEBUG)

            # 定义handler的输出格式
            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s")
            ch.setFormatter(formatter)

            # 给logger添加handler
            # self.logger.addHandler(fh)
            self.logger.addHandler(ch)
            """

    def debug(self, msg):
        """
        定义输出的颜色debug--white，info--green，warning/error/critical--red
        :param msg: 输出的log文字
        :return:
        """
        self.logger.debug(Fore.CYAN + "DEBUG - " + str(msg) + Style.RESET_ALL)

    def info(self, msg):
        self.logger.info(Fore.GREEN + "INFO - " + str(msg) + Style.RESET_ALL)

    def warning(self, msg):
        self.logger.warning(Fore.YELLOW + "WARNING - " + str(msg) + Style.RESET_ALL)

    def error(self, msg):
        self.logger.error(Fore.RED + "ERROR - " + str(msg) + Style.RESET_ALL)

    def critical(self, msg):
        self.logger.critical(Fore.RED + "CRITICAL - " + str(msg) + Style.RESET_ALL)


if __name__ == '__main__':
    log = Logger("TestTSDB")
    log.debug("debug")
    log.info("info")
    log.error("error")
    log.warning("warning")
    log.critical("critical")
