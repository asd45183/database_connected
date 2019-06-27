#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-26 13:43
# @Author  : Mr_d
# @Site    : 
# @File    : test_MysqlDB.py
# 未验证！！

# 引入被测类
from . import SqlServerConnected

# 引入公共配置
import pytest
from . import Logger
from . import get_err_line
log = Logger("TestSqlServer")


class TestSqlServer(object):

    @pytest.fixture()
    def mssql_init(self):

        # 这里定义测试数据
        host = "127.0.0.1"
        port = 3306
        username = "root"
        password = "password"
        database = "mytest"
        charset = "utf8"
        # 初始化对象
        mssql_con = SqlServerConnected(host=host, port=port, password=password, username=username, database=database)

        log.info("TestMethod--------START")
        yield mssql_con
        # 结束执行
        log.info("TestMethod--------END")

    def test_create_database(self, mssql_init):
        result = mssql_init.create_database()
        assert result == 1, log.error("测试失败，结果应为:1，错误方法为：%r,错误行数为 %r" % get_err_line())
        log.debug(result)

    def test_create_table(self, mssql_init):
        result = mssql_init.create_table()
        assert result == 0, log.error("测试失败，结果应为:0，错误方法为：%r,错误行数为 %r" % get_err_line())
        log.debug(result)

    def test_insert_data(self, mssql_init):
        # 判断插入数据成功 应为True
        result = mssql_init.insert_data_to_table()
        assert result == 27, log.error("测试失败，结果应为:27，错误方法为：%r,错误行数为 %r" % get_err_line())
        log.debug(result)

    def test_get_data(self, mssql_init):
        # 判断是否取到数据,有数据则为True
        result = mssql_init.get_data()
        assert result == 27, log.error("测试失败，结果应为:27，错误方法为：%r,错误行数为 %r" % get_err_line())
        log.debug(result)

    def test_update_data(self, mssql_init):
        # 判断更新数据方法
        result = mssql_init.update_data()
        assert result == "data_new", log.error("测试失败，结果应为:data_new，错误方法为：%r,错误行数为 %r" % get_err_line())
        log.debug(result)

    def test_delete_data(self, mssql_init):
        # 判断删除数据成功 应为True
        result = mssql_init.delete_table()
        assert result == 26, log.error("测试失败，结果应为:26，错误方法为：%r,错误行数为 %r" % get_err_line())
        log.debug(result)

    def test_delete_all_data(self, mssql_init):
        result = mssql_init.delete_all_data()
        assert result == 1, log.error("测试失败，结果应为:1，错误方法为：%r,错误行数为 %r" % get_err_line())
        log.debug(result)


# 调用 Pytest 开始测试
if __name__ == '__main__':
    pytest.main('--html=report.html --self-contained-html')
