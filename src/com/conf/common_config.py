#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-26 18:00
# @Author  : Mr_d
# @Site    : 
# @File    : common_config.py

import ConfigParser
import os
import sys

"""
-read(filename)               直接读取文件内容
-sections()                      得到所有的section，并以列表的形式返回
-options(section)            得到该section的所有option
-items(section)                得到该section的所有键值对
-get(section,option)        得到section中option的值，返回为string类型
-getint(section,option)    得到section中option的值，返回为int类型，还有相应的getboolean()和getfloat() 函数。
"""


class CommonConf(object):

    def __init__(self, class_name=""):
        # 定义基准URL
        self.base_url = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

        # 实例化对象
        self.cf = ConfigParser.ConfigParser()

        # 读取配置文件

        self.cf.read(self.__real_url("testfiles/conf/common.conf"))

        # 接受测试方法类

        self.class_name = class_name

        # 获取配置信息 class_nmae 为传入的测试类名
        self.conf_url = self.cf.get("common", "log_url")

    # 返回真是路径
    def __real_url(self, url_path=""):
        return '/'.join([self.base_url, url_path])

    def set_log_conf(self):
        log_url = self.__real_url(self.conf_url) + self.class_name + ".log"
        return log_url


# 定位到出错的位置
def get_err_line():
    """Return the frame object for the caller's stack frame."""
    try:
        raise Exception

    except:
        f = sys.exc_info()[2].tb_frame.f_back

    # 方法名：f.f_code.co_name 行数：f.f_lineno
    return f.f_code.co_name, f.f_lineno


if __name__ == '__main__':
    cf = CommonConf(class_name="TestMysql")
    cf.set_log_conf()
