#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:Me.D
"""
requirement：pip install psycopg2-binary
注：尚未验证可行性,
适用于 ppas,postgres,gpdb
"""
import psycopg2


class PostgresConnected(object):

    def __init__(self, host="", port=5432, username="", password="", database="postgres"):

        """
        - *dbname*: the database name
        - *database*: the database name (only as keyword argument)
        - *user*: user name used to authenticate
        - *password*: password used to authenticate
        - *host*: database host address (defaults to UNIX socket if not provided)
        - *port*: connection port number (defaults to 5432 if not provided)
        """

        # 初始化参数
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database

        # 定义连接端
        self.client = psycopg2.connect(database=self.database, user=self.username, password=self.password,
                                       host=self.host, port=self.port)

    # 创建一个测试库：test_db
    def create_database(self):

        # 创建数据操作游标
        cursor = self.client.cursor()

        # 执行SQL
        cursor.execute("CREATE DATABASE test_db WITH ENCODING='utf8'")

        """
        举个例子:cursor是我们连接数据库的实例

        fetchone()的使用:
        
        cursor.execute(select username,password,nickname from user where id='%s'  %(input)
        
        result=cursor.fetchone();  此时我们可以通过result[0],result[1],result[2]得到username,password,nickname
        
        fetchall()的使用:
        
        cursor.execute(select * from user)
        
        result=cursor.fetchall();此时select得到的可能是多行记录,那么我们通过fetchall得到的就是多行记录,是一个二维元组
        
        ((username1,password1,nickname1),(username2,password2,nickname2),(username3,password3,nickname))
        
        """
        cursor.fetchone()

        cursor.close()

    # 创建测试表
    def create_table(self):

        # 创建数据操作游标
        cursor = self.client.cursor()

        # 执行SQL
        cursor.execute("USE test_db")

        cursor.execute(
            "CREATE TABLE test_table("
            "data_id SERIAL primary key,"
            "data_name VARCHAR(20) NOT NULL,"
            "data_info VARCHAR(20),"
            "data_time timestamp NOT NULL DEFAULT current_timestamp(0)/*默认写入当前时间*/)"
        )
        cursor.commit()

        cursor.fetchone()

        cursor.close()

    def insert_data_to_table(self):

        # 创建数据操作游标
        cursor = self.client.cursor()

        cursor.execute("USE test_db")

        # 定义插入数据列表
        sql_list = [
            "insert into test_table(data_id,data_name,data_info) values ('1001','date_001','it is a test data')",
            "insert into test_table(data_id,data_name,data_info) values ('1002','date_002','it is a test data')",
            "insert into test_table(data_id,data_name,data_info) values ('1003','date_003','it is a test data')",
            "insert into test_table(data_id,data_name,data_info) values ('1004','date_004','it is a test data')",
            "insert into test_table(data_id,data_name,data_info) values ('1005','date_005','it is a test data')",
            "insert into test_table(data_id,data_name,data_info) values ('1006','date_006','it is a test data')",
            "insert into test_table(data_id,data_name,data_info) values ('1007','date_007','it is a test data')",
            "insert into test_table(data_id,data_name,data_info) values ('1008','date_008','it is a test data')",
            "insert into test_table(data_id,data_name,data_info) values ('1009','date_009','it is a test data')",
            "insert into test_table(data_id,data_name,data_info) values ('1010','date_010','it is a test data')",
            "insert into test_table(data_id,data_name,data_info) values ('1011','date_011','it is a test data')",
            "insert into test_table(data_id,data_name,data_info) values ('1012','date_012','it is a test data')",
            "insert into test_table(data_id,data_name,data_info) values ('1013','date_013','it is a test data')",
            "insert into test_table(data_id,data_name,data_info) values ('1014','date_014','it is a test data')",
            "insert into test_table(data_id,data_name,data_info) values ('1015','date_015','it is a test data')",
            "insert into test_table(data_id,data_name,data_info) values ('1016','date_016','it is a test data')"
        ]

        # 循环获取并插入数据
        for sql in sql_list:
            cursor.execute(sql)
            cursor.commit()

        cursor.close()

    # 查询数据
    def get_data(self):

        """
        fetchone()的使用:

        cursor.execute(select username,password,nickname from user where id='%s'  %(input)

        result=cursor.fetchone();  此时我们可以通过result[0],result[1],result[2]得到username,password,nickname
        fetchall()的使用:

        cursor.execute(select * from user)

        result=cursor.fetchall();此时select得到的可能是多行记录,那么我们通过fetchall得到的就是多行记录,是一个二维元组

        ((username1,password1,nickname1),(username2,password2,nickname2),(username3,password3,nickname))
        """

        # 创建数据操作游标
        cursor = self.client.cursor()

        cursor.execute("USE test_db;")

        cursor.execute("select * from test_table;")

        result = cursor.fetchall()

        for row in result:
            return ("data_id=" + str(row[0]) + "data_name=" + str(row[1]) + "data_info=" + str(
                row[2]) + "data_time=" + str(row[3]))

    # 修改表
    def update_date(self):

        # 定义游标
        cursor = self.client.cursor()

        cursor.execute("USE test_db")

        cursor.execute("update test_table set data_name='date_new' where data_id=1016")

        cursor.execute("select * from test_table where data_id=1016")

        cursor.commit()

        result = cursor.fetchone()

        # 返回修改后的值，1 表示第二个值 即 data_name
        return result[1]

    # 删除表
    def delete_date(self):

        # 定义游标
        cursor = self.client.cursor()

        cursor.execute("USE test_db")

        cursor.execute("delete from  test_table  where data_id=1016")

        cursor.execute("select * from test_table where data_id=1016")

        cursor.commit()

        result = cursor.fetchone()

        # 数据应被删除，所以返回结果即可
        return result

    # 关闭连接
    def close_conn(self):

        result = self.client.close()

        return result


if __name__ == '__main__':
    # 调用类
    pg_con = PostgresConnected(host="", port=5432, username="", password="", database="postgres")
