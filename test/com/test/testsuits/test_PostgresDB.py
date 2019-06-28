#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-28 15:06
# @Author  : Mr_d
# @Site    : 
# @File    : test_PostgresDB.py
import pytest
import pytest

from src.com.conf.common_config import get_err_line
from src.com.conf.commonlog import Logger
from src.com.db.connectd import SqlServerConnected

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
            cls.mssql_con = SqlServerConnected(host=host, port=port, password=password, username=username,
                                               database=database)

        except:
            log.error("TestMethod---------ERROR")
            log.error("初始化错误，程序结束")
            pytest.skip(msg="始化错误")

        else:
            log.info("TestMethod--------START")
            return cls.mssql_con

    @classmethod
    def teardown_class(cls):
        log.info("TestMethod--------END")
        pytest.exit("测试完成")
