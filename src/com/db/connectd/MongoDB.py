#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:Me.D
"""
requirements:pymongo-3.8.0.tar.gz
"""

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import json


class MonGoConnected:
    def __init__(self, host="", port=28001, username="root", password="", con_db="admin", database_name="",
                 collection=""):
        # 定义连接客户端
        self.client = None
        # 初始化参数
        self.db_name = database_name
        self.col = collection
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.con_db = con_db
        
        self.url = "mongodb://%s:%s@%s:%s/%s" % (self.username, self.password, self.host, self.port, self.con_db)
"""
        self.url = "mongodb://%s:%s@%s:%s/%s" % (username, password, host, port, con_db)
        try:
            # 定义 Client
            conn_url = self.url
            # 定义连接客户端
            self.client = MongoClient(conn_url)

        except ConnectionFailure as connect_error:
            print (connect_error.message)
            print ("")
            print ("Server not available")

    # 插入数据
    def insert_test_data(self):

        # 创建数据库
        test_db = self.client[self.db_name]
        # 插入数据:创建集合
        test_collection = test_db[self.col]
        # 插入数据：写入数据
        data = test_collection.insert_many(data_list)
        # 插入数据：保存数据
        # test_collection.save(data_list)
        self.client.close()

    # 查询数据
    def find_test_data(self):

        # 获取所有db列表
        db_list = self.client.list_database_names()
        # 检查是否存在测试db
        assert (
                self.db_name in db_list), "except database_name is  % self.db_name, but we can't find it in db_list" % self.db_name
        # 检查是否存在测试集合
        collection_list = self.client[self.db_name].list_collection_names()
        assert (
                self.col in collection_list), "except collection is % self.col ,but we can't find it in collection_list" % self.col
        # 查询数据
        test_collection = self.client[self.db_name][self.col]
        for data in test_collection.find():
            # dict类型
            print (type(data))
            # 调用json.dumps() 转换为json类型
            print (json.dumps(str(data), encoding='utf-8', ensure_ascii=False))

    # 更新数据
    def update_data(self):

        test_collection = self.client[self.db_name][self.col]
        # 更新数据
        test_collection.update_many({"data_name": "test_data_3"}, {'$set': {"data_name": "test_data_4"}})
        # 查询数据
        for data in test_collection.find():
            # dict类型
            print (type(data))
            # 调用json.dumps() 转换为json类型
            print (json.dumps(str(data), encoding='utf-8', ensure_ascii=False))

    # 删除数据
    def delete_data(self):

        del_collection = "runoob"
        db = self.client[self.db_name]
        col = self.client[self.db_name][self.col]
        # 删除数据
        print(col.delete_many({"data_name": "test_data_4"}))
        # 删除集合
        print(db.drop_collection(del_collection))

    # 创建用户
    def create_user(self):

        user_name = "test_user"
        db = self.client["admin"]
        # 新建用户
        print(db.command("createUser", user_name, pwd="password", roles=["root"]))

    # 更新用户信息
    def update_user(self):

        user_name = "test_user"
        db = self.client["admin"]
        # 更新用户（密码）
        print(db.command("updateUser", user_name, pwd="123456", roles=["root"]))


if __name__ == '__main__':
    # 初始化测试数据
    data_list = [{
        "title": 'MongoDB 教程',
        "description": 'MongoDB 是一个 Nosql 数据库',
        "by": '菜鸟教程',
        "url": 'http://www.runoob.com',
        "tags": ['mongodb', 'database', 'NoSQL'],
        "likes": 100
    }, {
        "data_name": "test_data_2",
        "data_value": "this is a test data",
    }, {
        "data_name": "test_data_3",
        "data_value": "this is a test data",
    }, {
        "data_name": "test_data_4",
        "data_value": "this is a test data",
    }]

    # 初始化新数据 update
    data_list_new = {
        "title": 'MongoDB 教程',
        "description":
            'MongoDB 是一个 Nosql 数据库',
        "by": '菜鸟教程',
        "url": 'http://www.runoob.com',
        "tags": ['mongodb', 'database', 'NoSQL'],
        "likes": 0
    }

    # 定义对象，传入测试数据
    mon_conn = MonGoConnected(host="", username="root", password="Admin123", con_db="admin", port=28001,
                            database_name="test_db", collection="testCollection")
    mon_conn.insert_test_data()
    mon_conn.find_test_data()
    mon_conn.update_data()
    mon_conn.create_user()
    mon_conn.update_user()
    mon_conn.create_user()
    mon_conn.update_user()
