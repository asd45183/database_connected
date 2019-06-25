#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:Me.D

# 引入被测类
from src.com.db.connectd.MemcachDB import Memcaheconnected
import pytest


class TestMem:

    key_name = "test_key"
    key_value = "test_key_value"
    key_value_new = "test_key_value_new"
    mem_conn = Memcaheconnected(host="", port=11211,
                                username="", password="", key_name=key_name,
                                key_value=key_value, key_value_new=key_value_new)

    def test_set_data(self):

        # 判断插入数据成功 应为True
        # assert self.mem_conn.set_data() is True
        assert self.mem_conn.set_data() is True

    def test_delete_data(self):

        # 判断插入数据成功 应为True
        assert self.mem_conn.delete_data() is True

    def test_replace_data(self):

        # 判断更新数据方法
        assert self.mem_conn.update_data() is True


# 调用Pytest 开始测试
if __name__ == '__main__':

    pytest.main()
