#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-26 13:43
# @Author  : Mr_d
# @Site    : 
# @File    : test_MysqlDB.py
# 未验证！！
import logging
import os

import pytest

# 引入被测类
from src.com.db.connectd.MysqlDB import MySQLConnected

# 定位到项目目录
base_url = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))))
log_url = base_url + "/testfiles/log/TestMysql.log"


class TestMysql():
    logging.basicConfig(level=logging.DEBUG, filename=log_url)

    @pytest.fixture()
    def mysql_init(self):
        # 初始化数据
        host = "127.0.0.1"
        port = 3306
        username = "root"
        password = "123456"
        database = ""
        charset = "utf8"

        # 初始化对象
        my_con = MySQLConnected(host=host, port=port, username=username, password=password, database=database,
                                charset=charset)
        yield my_con
        my_con.close_conn()

    def test_create_database(self, mysql_init):
        result = mysql_init.create_database()
        log = logging.getLogger("test_create_table")
        assert result == 1
        log.debug(result)

    def test_create_table(self, mysql_init):
        log = logging.getLogger("test_create_table")
        result = mysql_init.create_table()
        assert result == 0
        log.debug(result)

    def test_insert_data(self, mysql_init):
        # 判断插入数据成功 应为True
        result = mysql_init.insert_data_to_table()
        log = logging.getLogger("test_insert_data")
        assert result == 27, "判断插入数据成功，结果应为:True"
        log.debug(result)

    def test_get_data(self, mysql_init):
        # 判断是否取到数据,有数据则为True
        result = mysql_init.get_data()
        log = logging.getLogger("test_get_data")
        assert result == 27, "判断是否取到数据,有数据应为:True"
        log.debug(result)

    def test_update_data(self, mysql_init):
        # 判断更新数据方法
        result = mysql_init.update_data()
        log = logging.getLogger("test_update_data")
        assert result == "data_new", "判断更新数据方法,结果应为:True"
        log.debug(result)

    def test_delete_data(self, mysql_init):
        log = logging.getLogger("test_delete_data")
        # 判断删除数据成功 应为True
        result = mysql_init.delete_table()
        log.debug(result)
        assert result == 26, "判断删除数据成功,结果应为26 条"

    def test_delete_all_data(self, mysql_init):
        log = logging.getLogger("test_delete_all_data")
        result = mysql_init.delete_all_data()
        assert result == 1




# 调用 Pytest 开始测试
if __name__ == '__main__':
    pytest.main('-s')
