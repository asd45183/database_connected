#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-28 15:06
# @Author  : Mr_d
# @Site    : 
# @File    : test_PostgresDB.py
import pytest

from src.com.conf.common_config import get_err_line
from src.com.conf.commonlog import Logger
from src.com.db.connectd import PostgresConnected

log = Logger("TestPostgres")


class TestPostgres(object):

    @classmethod
    def setup_class(cls):

        # 这里定义测试数据
        host = ""
        port = 3432
        username = "root_1"
        password = "password"
        database = "postgres"

        try:
            # 初始化对象
            cls.pg_con = PostgresConnected(host=host, port=port, password=password, username=username,
                                           database=database)
        except:
            log.error("TestMethod---------ERROR")
            log.error("初始化错误，程序结束")
            pytest.skip(msg="始化错误")

        else:
            log.info("TestMethod--------START")
            return cls.pg_con

    @classmethod
    def teardown_class(cls):
        log.info("TestMethod--------END")
        pytest.exit("测试完成")

    def test_create_table(self):
        result = self.pg_con.create_table()
        assert result is None, log.error("测试失败，结果应为: None，错误方法为：%s, 错误行数为: %r" % get_err_line())
        log.info("测试通过，方法名称为: %s, 当前的行数为：%r" % get_err_line())

    def test_insert_data_to_table(self):
        result = self.pg_con.insert_data_to_table()
        assert result == 15, log.error("测试失败，结果应为: None，错误方法为：%s, 错误行数为: %r" % get_err_line())
        log.info("测试通过，方法名称为: %s, 当前的行数为：%r" % get_err_line())

    def test_get_data(self):
        result = self.pg_con.get_data()
        assert result == 15, log.error("测试失败，结果应为:15，错误方法为：%s, 错误行数为 %r" % get_err_line())

    def test_update_data(self):
        result = self.pg_con.update_data()
        assert result == "data_new", \
            log.error("测试失败，结果应为: data_new，错误方法为：%s, 错误行数为: %r" % get_err_line())
        log.info("测试通过，方法名称为: %s, 当前的行数为：%r" % get_err_line())

    def test_delete_data(self):
        result = self.pg_con.delete_data()
        assert result is None, log.error("测试失败，结果应为: None，错误方法为：%s, 错误行数为: %r" % get_err_line())
        log.info("测试通过，方法名称为: %s, 当前的行数为：%r" % get_err_line())

    def test_close_conn(self):
        result = self.pg_con.close_conn()
        assert result is None, log.error("测试失败，结果应为: None，错误方法为：%s, 错误行数为: %r" % get_err_line())
        log.info("测试通过，方法名称为: %s, 当前的行数为：%r" % get_err_line())


if __name__ == '__main__':
    pytest.main()
