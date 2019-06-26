#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-26 13:43
# @Author  : Mr_d
# @Site    : 
# @File    : test_MysqlDB.py
# 未验证！！
import pytest

# 引入被测类
from src.com.db.connectd.MysqlDB import MySQLConnected


class TestMysql(object):

    @pytest.fixture()
    def mysql_init(self):
        # 初始化数据
        host = "127.0.0.1"
        port = 3306
        username = "root"
        password = "password"
        database = "mytest"
        charset = "utf8"

        # 初始化对象
        my_con = MySQLConnected(host=host, port=port, username=username, password=password, database=database,
                                charset=charset)

        yield my_con
        # 结束执行

    def test_set_data(self, mysql_init):
        # 判断插入数据成功 应为True
        assert mysql_init.set_data() is True, "判断插入数据成功，结果应为:True"

    def test_get_data(self, mysql_init):
        # 判断是否取到数据,有数据则为True
        assert mysql_init.get_data() is True, "判断是否取到数据,有数据应为:True"

    def test_update_data(self, mysql_init):
        # 判断更新数据方法
        assert mysql_init.update_data() is True, "判断更新数据方法,结果应为:True"

    def test_delete_data(self, mysql_init):
        # 判断删除数据成功 应为True
        assert mysql_init.delete_data() is True, "判断删除数据成功,结果应为True"


# 调用 Pytest 开始测试
if __name__ == '__main__':
    pytest.main()
