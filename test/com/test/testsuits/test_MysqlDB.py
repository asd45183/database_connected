#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-26 13:43
# @Author  : Mr_d
# @Site    : 
# @File    : test_MysqlDB.py
# 使用pytest执行
# 引入被测类
# 引入公共配置
import pytest

from src.com.conf.common_config import get_err_line
from src.com.conf.commonlog import Logger
from src.com.db.connectd import MySQLConnected

log = Logger("TestMysql")


class TestMysql(object):

    @classmethod
    def setup_class(cls):

        # 这里定义测试数据
        host = "127.0.0.1"
        port = 3306
        username = "root"
        password = "123456"
        database = ""
        charset = "utf8"

        try:
            cls.my_con = MySQLConnected(host=host, port=port, username=username, password=password, database=database,
                                        charset=charset)
        except:
            log.error("TestMethod---------ERROR")
            log.error("初始化错误，程序结束")
            pytest.skip(msg="始化错误")
        else:
            log.info("TestMethod--------START")
            return cls.my_con

    @classmethod
    def teardown_class(cls):
        log.info("TestMethod--------END")
        pytest.exit("测试完成")

    def test_create_database(self):
        result = self.my_con.create_database()
        assert result == 1, log.error("测试失败，结果应为:1，错误方法为：%r,错误行数为 %r" % get_err_line())
        log.debug(result)

    def test_create_table(self):
        result = self.my_con.create_table()
        assert result == 0, log.error("测试失败，结果应为:0，错误方法为：%r,错误行数为 %r" % get_err_line())
        log.debug(result)

    def test_insert_data(self):
        result = self.my_con.insert_data_to_table()
        assert result == 27, log.error("测试失败，结果应为:27，错误方法为：%r,错误行数为 %r" % get_err_line())
        log.debug(result)

    def test_get_data(self):
        result = self.my_con.get_data()
        assert result == 27, log.error("测试失败，结果应为:27，错误方法为：%r,错误行数为 %r" % get_err_line())
        log.debug(result)

    def test_update_data(self):
        result = self.my_con.update_data()
        assert result == "data_new", log.error("测试失败，结果应为:data_new，错误方法为：%r,错误行数为 %r" % get_err_line())
        log.debug(result)

    def test_delete_data(self):
        result = self.my_con.delete_table()
        log.debug(result)
        assert result == 26, log.error("测试失败，结果应为:26，错误方法为：%r,错误行数为 %r" % get_err_line())
        log.debug(result)

    def test_delete_all_data(self):
        result = self.my_con.delete_all_data()
        assert result == 1, log.error("测试失败，结果应为:1，错误方法为：%r,错误行数为 %r" % get_err_line())
        log.debug(result)


if __name__ == '__main__':
    pytest.main()
