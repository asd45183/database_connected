#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:Me.D
"""
requirement：python-binary-memcached-0.26.1.tar，six-1.9.0-py2.py3-none-any.whl
"""
import bmemcached


class Memcaheconnected:

    def __init__(self, host="", port=11211, username="", password="", key_name="", key_value="", key_value_new=""):

        self.key_name = key_name
        self.key_value = key_value
        self.key_value_new = key_value_new
        # 初始化客户端
        self.client = bmemcached.Client([host, str(port)], username, password)

    # 插入数据
    def set_data(self):

        """
        Set a value for a key on server.

        :param key: Key's name
        :type key: str
        :param value: A value to be stored on server.
        :type value: object
        :param time: Time in seconds that your key will expire.
        :type time: int
        :param compress_level: How much to compress.
            0 = no compression, 1 = fastest, 9 = slowest but best,
            -1 = default compression level.
        :type compress_level: int
        :return: True in case of success and False in case of failure
        :rtype: bool

        """
        result = self.client.set(key=self.key_name, value=self.key_value)
        return (result)

    # 查询数据
    def get_data(self):

        result = self.client.get(key=self.key_name)
        return (result)

    # 删除数据
    def delete_data(self):

        result = self.client.delete(key=self.key_name)
        return (result)

    # 更新数据
    def update_data(self):

        result = self.client.replace(key=self.key_name, value=self.key_value_new)
        return (result)

    # 未完待续


if __name__ == '__main__':

    # 初始化测试数据
    key_name = "test_key"
    key_value = "test_key_value"
    key_value_new = "test_key_value_new"

    # 生成类的对象
    mem_con = Memcaheconnected(host="", port=11211, username="", password="")
    mem_con.set_data()
