#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/28 21:18
# @Author  : Mr_d
# @Site    : 
# @File    : test_RedisDB.py
import pytest

from src.com.conf.common_config import get_err_line
from src.com.conf.commonlog import Logger
from src.com.db.connectd import RedisConnected

log = Logger("")


class TestRedisDB(object):

    @classmethod
    def setup_class(cls):

        # 这里定义测试数据
        key_name = "test_key"
        key_value = "test_key_value"

        try:
            # 生成类
            cls.re_con = RedisConnected(host="", port=6379, password="", key_name=key_name, key_value=key_value,
                                        hash_name="", hash_data={})
        except:
            log.error("TestMethod---------ERROR")
            log.error("初始化错误，程序结束")
            pytest.skip(msg="始化错误")
        else:
            log.info("TestMethod--------START")
            return cls.re_con

    @classmethod
    def teardown_class(cls):
        log.info("TestMethod--------END")
        pytest.exit("测试完成")

    def test_set_data(self):
        result = self.re_con.set_data()
        assert result is True, log.error("测试失败，结果应为:True，错误方法为：%s, 错误行数为: %r" % get_err_line())
        log.info("测试通过，方法名称为: %s, 当前的行数为：%r" % get_err_line())

    def test_get_data(self):
        result = self.re_con.get_data()
        assert result == "test_key_value", \
            log.error("测试失败，结果应为:test_key_value，错误方法为：%s, 错误行数为: %r" % get_err_line())
        log.info("测试通过，方法名称为: %s, 当前的行数为：%r" % get_err_line())

    def test_set_hash_data(self):
        result = self.re_con.set_hash_data()
        assert result is True, log.error("测试失败，结果应为: True，错误方法为：%s, 错误行数为: %r" % get_err_line())
        log.info("测试通过，方法名称为: %s, 当前的行数为：%r" % get_err_line())

    def test_get_hash_data(self):
        result = self.re_con.get_hash_data()
        assert result == 1, log.error("测试失败，结果应为:1，错误方法为：%s, 错误行数为: %r" % get_err_line())
        log.info("测试通过，方法名称为: %s, 当前的行数为：%r" % get_err_line())

    def test_set_list_data(self):
        result = self.re_con.set_list_data()
        assert result == 10, log.error("测试失败，结果应为:10，错误方法为：%s, 错误行数为: %r" % get_err_line())
        log.info("测试通过，方法名称为: %s, 当前的行数为：%r" % get_err_line())

    def test_get_list_data(self):
        result = self.re_con.get_list_data()
        assert result == 1, log.error("测试失败，结果应为:1，错误方法为：%s, 错误行数为: %r" % get_err_line())
        log.info("测试通过，方法名称为: %s, 当前的行数为：%r" % get_err_line())


if __name__ == '__main__':
    pytest.main()
