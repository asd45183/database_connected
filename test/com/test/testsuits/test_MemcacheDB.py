#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:Me.D
# 使用pytest执行
# 引入被测类
# 引入公共配置
import pytest

from src.com.conf.common_config import get_err_line
from src.com.conf.commonlog import Logger
from src.com.db.connectd import Memcaheconnected

log = Logger("TestMem")


class TestMem(object):

    @classmethod
    def setup_class(cls):

        # 这里定义测试数据
        key_name = "test_key"
        key_value = "test_key_value"
        key_value_new = "test_key_value_new"
        try:
            # 生成类
            cls.mem_con = Memcaheconnected(host="", port=11211,
                                           username="", password="", key_name=key_name,
                                           key_value=key_value, key_value_new=key_value_new)
        except:
            log.error("TestMethod---------ERROR")
            log.error("初始化错误，程序结束")
            pytest.skip(msg="始化错误")
        else:
            log.info("TestMethod--------START")
            return cls.mem_con

    @classmethod
    def teardown_class(cls):
        log.info("TestMethod--------END")
        pytest.exit("测试完成")

    def test_set_data(self):
        # 判断插入数据成功 应为True
        assert self.mem_con.set_data() is True, log.error("测试失败，结果应为:True，错误方法为：%r,错误行数为 %r" % get_err_line())

    def test_get_data(self):
        # 判断是否取到数据,有数据则为True
        assert self.mem_con.get_data() is True, log.error("测试失败，结果应为:True，错误方法为：%r,错误行数为 %r" % get_err_line())

    def test_update_data(self):
        # 判断更新数据方法
        assert self.mem_con.update_data() is True, log.error("测试失败，结果应为:True，错误方法为：%r,错误行数为 %r" % get_err_line())

    def test_delete_data(self):
        # 判断删除数据成功 应为True
        assert self.mem_con.delete_data() is True, log.error("测试失败，结果应为:True，错误方法为：%r,错误行数为 %r" % get_err_line())

    def test_set_multi_data(self):
        # 判断插入数据成功 应为True
        assert self.mem_con.set_multi_data() is True, log.error("测试失败，结果应为:True，错误方法为：%r,错误行数为 %r" % get_err_line())
