#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-26 13:43
# @Author  : Mr_d
# @Site    : 
# @File    : test_MysqlDB.py
# 未验证！！
import pytest

# 引入被测类
from src.com.db.connectd.SqlServerDB import SqlServerConnected


class TestSqlServer(object):

    @pytest.fixture()
    def mssql_init(self):
        # 初始化数据
        host = "127.0.0.1"
        port = 3306
        username = "root"
        password = "password"
        database = "mytest"
        charset = "utf8"

        # 初始化对象
        mssql_con = SqlServerConnected(host=host, port=port, password=password, username=username, database=database)

        yield mssql_con
        # 结束执行

    def test_set_data(self, mssql_init):
        # 判断插入数据成功 应为True
        assert mssql_init.set_data() is True, "判断插入数据成功，结果应为:True"

    def test_get_data(self, mssql_init):
        # 判断是否取到数据,有数据则为True
        assert mssql_init.get_data() is True, "判断是否取到数据,有数据应为:True"

    def test_update_data(self, mssql_init):
        # 判断更新数据方法
        assert mssql_init.update_data() is True, "判断更新数据方法,结果应为:True"

    def test_delete_data(self, mssql_init):
        # 判断删除数据成功 应为True
        assert mssql_init.delete_data() is True, "判断删除数据成功,结果应为True"


# 调用 Pytest 开始测试
if __name__ == '__main__':
    pytest.main()
