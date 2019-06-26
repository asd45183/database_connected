#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:Me.D

import pytest

# 引入被测类
from src.com.db.connectd.MemcachDB import Memcaheconnected


class TestMem(object):

    @pytest.fixture()
    def mem_init(self):
        key_name = "test_key"
        key_value = "test_key_value"
        key_value_new = "test_key_value_new"

        # 生成类
        mem_conn = Memcaheconnected(host="", port=11211,
                                    username="", password="", key_name=key_name,
                                    key_value=key_value, key_value_new=key_value_new)
        # print ("test_start")
        yield mem_conn
        # 结束执行
        # print ("test stop")

    def test_set_data(self, mem_init):
        # 判断插入数据成功 应为True
        assert mem_init.set_data() is True, "判断插入数据成功，结果应为:True"

    def test_get_data(self, mem_init):
        # 判断是否取到数据,有数据则为True
        assert mem_init.get_data() is True, "判断是否取到数据,有数据应为:True"

    def test_update_data(self, mem_init):
        # 判断更新数据方法
        assert mem_init.update_data() is True, "判断更新数据方法,结果应为:True"

    def test_delete_data(self, mem_init):
        # 判断删除数据成功 应为True
        assert mem_init.delete_data() is True, "判断删除数据成功,结果应为True"

    def test_set_multi_data(self, mem_init):
        # 判断插入数据成功 应为True
        assert mem_init.set_multi_data() is True, "判断插入数据成功，结果应为:True"


# 调用 Pytest 开始测试
if __name__ == '__main__':
    pytest.main()
