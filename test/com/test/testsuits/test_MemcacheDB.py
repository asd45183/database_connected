#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:Me.D

# 引入被测类
from . import Memcaheconnected

# 引入公共配置
import pytest
from . import Logger
from . import get_err_line
log = Logger("TestMem")


class TestMem(object):

    @pytest.fixture()
    def mem_init(self):

        # 这里定义测试数据
        key_name = "test_key"
        key_value = "test_key_value"
        key_value_new = "test_key_value_new"

        # 生成类
        mem_conn = Memcaheconnected(host="", port=11211,
                                    username="", password="", key_name=key_name,
                                    key_value=key_value, key_value_new=key_value_new)
        log.info("TestMethod--------START")
        yield mem_conn
        log.info("TestMethod--------END")

    def test_set_data(self, mem_init):
        # 判断插入数据成功 应为True
        assert mem_init.set_data() is True, log.error("测试失败，结果应为:True，错误方法为：%r,错误行数为 %r" % get_err_line())

    def test_get_data(self, mem_init):
        # 判断是否取到数据,有数据则为True
        assert mem_init.get_data() is True, log.error("测试失败，结果应为:True，错误方法为：%r,错误行数为 %r" % get_err_line())

    def test_update_data(self, mem_init):
        # 判断更新数据方法
        assert mem_init.update_data() is True, log.error("测试失败，结果应为:True，错误方法为：%r,错误行数为 %r" % get_err_line())

    def test_delete_data(self, mem_init):
        # 判断删除数据成功 应为True
        assert mem_init.delete_data() is True, log.error("测试失败，结果应为:True，错误方法为：%r,错误行数为 %r" % get_err_line())

    def test_set_multi_data(self, mem_init):
        # 判断插入数据成功 应为True
        assert mem_init.set_multi_data() is True, log.error("测试失败，结果应为:True，错误方法为：%r,错误行数为 %r" % get_err_line())


# 调用 Pytest 开始测试
if __name__ == '__main__':
    pytest.main()
