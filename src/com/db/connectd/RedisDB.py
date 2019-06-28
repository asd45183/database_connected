#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:Me.D
"""
requirement:redis-py-master.tar.gz
"""
from redis import Redis, ConnectionError


class RedisConnected(object):

    # 初始化连接
    def __init__(self, host="", port=6379, password="", key_name="", key_value="", hash_name="", hash_data={}):

        """
        # ssl认证时使用
        pool = ConnectionPool(
            host=host,
            port=port,
            password=password,

            ssl=True,
            ssl_cert_reqs=True,
            ssl_ca_certs="xxx.ca"
        )
        self.client = Redis(pool)
"""
        self.key_name = key_name
        self.key_value = key_value
        self.hash_name = hash_name
        self.hash_data = hash_data

        try:

            self.client = Redis(
                host=host,
                port=port,
                password=password
            )

        except ConnectionError as connection_err:
            print (connection_err.message)

    # 普通插入数据
    def set_data(self):

        """
        Set the value at key ``name`` to ``value``

        ``ex`` sets an expire flag on key ``name`` for ``ex`` seconds.

        ``px`` sets an expire flag on key ``name`` for ``px`` milliseconds.

        ``nx`` if set to True, set the value at key ``name`` to ``value`` only
            if it does not exist.

        ``xx`` if set to True, set the value at key ``name`` to ``value`` only
            if it already exists.
        """

        result = self.client.set(name=self.key_name, value=self.key_value)
        #True
        return result

    # 普通查询数据
    def get_data(self):

        result = self.client.get(name=self.key_name)

        assert self.key_value == result, "the value of %s is not expect ,the really value is %s" % (

            self.key_name, result)
        # test_key_value
        return result

    # 插入hash 类型的数据
    def set_hash_data(self):

        result = self.client.hmset(name=self.hash_name, mapping=self.hash_data)
        #True
        return result

    # 查询hash 类型的数据
    def get_hash_data(self):

        result = self.client.hgetall(name=self.hash_name)
        #1
        return result

    # 插入 list 类型的数据
    def set_list_data(self):

        # 每次执行都会新增
        result = self.client.lpush("list_data", 1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
        # 10
        return result

    # 获取 list 数据
    def get_list_data(self):

        # 获取数据
        result = self.client.lindex("list_data", 0)
        # 1
        return result


if __name__ == '__main__':
    # 初始化测试数据
    key_name = "test_key"
    key_value = "test_key_value"
    hash_name = "test_hash_data"
    hash_data = {
        "data_author": "root",
        "data_value": "test_data_value",
        "data_name": "test_data",
        "data_id": "1001"
    }

    re_con = RedisConnected(host="", port=6379, password="", key_name=key_name, key_value=key_value,
                            hash_name=hash_name, hash_data=hash_data)
    re_con.set_list_data()
