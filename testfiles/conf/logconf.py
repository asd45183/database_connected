#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-26 18:16
# @Author  : Mr_d
# @Site    : 
# @File    : logconf.py
import logging


class LogConf(object):

    def __init__(self):
        # 配置输出日志格式
        self.LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(pathname)s %(message)s "
        # 配置输出时间的格式，注意月份和天数不要搞乱了
        self.DATE_FORMAT = '%Y-%m-%d  %H:%M:%S %a '
        self.log_conf = logging.basicConfig(level=logging.DEBUG,
                                            format=self.LOG_FORMAT,
                                            datefmt=self.DATE_FORMAT,
                                            # 有了filename参数就不会直接输出显示到控制台，而是直接写入文件
                                            filename=r"d:\test\test.log"
                                            )


if __name__ == '__main__':
    pass
