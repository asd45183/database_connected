#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/28 21:54
# @Author  : Mr_d
# @Site    : 
# @File    : test_OracleDB.py
import pytest

from src.com.conf.common_config import get_err_line
from src.com.conf.commonlog import Logger
from src.com.db.connectd import OracleConnected

log = Logger("TestOracleDB")


class TestOracleDB(object):

    @classmethod
    def setup_class(cls):

        # 初始化参数
        host = "127.0.0.1"
        port = 1521
        username = "gioi"
        password = "123456"
        database = "orcl"
        # 初始化链接
        try:
            cls.ora_con = OracleConnected(host=host, port=port, username=username,
                                          password=password, database=database)
        except:
            log.error("TestMethod---------ERROR")
            log.error("初始化错误，程序结束")
            pytest.skip(msg="始化错误")

        else:
            log.info("TestMethod--------START")
            return cls.ora_con

    @classmethod
    def teardown_class(cls):
        log.info("TestMethod--------END")
        pytest.exit("测试完成")

    def test_create_table(self):
        result = self.ora_con.create_table()
        assert result is None, log.error("测试失败，结果应为:None，错误方法为：%s, 错误行数为:%r" % get_err_line())
        log.info("测试通过，方法名称为:%s, 当前的行数为：%r" % get_err_line())

    def test_insert_test_data(self):
        result = self.ora_con.insert_test_data()
        assert result == 12, log.error("测试失败，结果应为:12，错误方法为：%s, 错误行数为:%r" % get_err_line())
        log.info("测试通过，方法名称为:%s, 当前的行数为：%r" % get_err_line())

    def test_delete_test_data(self):
        result = self.ora_con.delete_test_data()
        assert result == 11, log.error("测试失败，结果应为:11，错误方法为：%s, 错误行数为:%r" % get_err_line())
        log.info("测试通过，方法名称为:%s, 当前的行数为：%r" % get_err_line())

    def test_update_user_password(self):
        result = self.ora_con.update_user_password()
        assert result is None, log.error("测试失败，结果应为:None，错误方法为：%s, 错误行数为:%r" % get_err_line())
        log.info("测试通过，方法名称为:%s, 当前的行数为：%r" % get_err_line())

    def test_delete_table(self):
        result = self.ora_con.delete_table()
        assert result is None, log.error("测试失败，结果应为:None，错误方法为：%s, 错误行数为:%r" % get_err_line())
        log.info("测试通过，方法名称为:%s, 当前的行数为：%r" % get_err_line())

    def test_close_client(self):
        result = self.ora_con.close_client()
        assert result is None, log.error("测试失败，结果应为:None，错误方法为：%s, 错误行数为:%r" % get_err_line())
        log.info("测试通过，方法名称为:%s, 当前的行数为：%r" % get_err_line())


if __name__ == '__main__':
    pytest.main()
