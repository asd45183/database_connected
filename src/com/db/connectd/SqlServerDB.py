#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:Me.D
"""
requirement: pip install pymssql
Python 操作SQLServer 需要使用 pymssql 模块，使用pip install pymssql安装。然后import该包即可。安装成功后，使用如下语句和 MSSql 数据库交互。

（ pymssql 需要安装 Cython：https://pypi.org/project/Cython   和   freetds：linux下利用freetds 访问sqlserver数据库  ）

下载 FreeTDS，地址：www.freetds.org
下载后解压: tar -zxvf XXX.tar.gz
然后执行
        ./configure --prefix=/usr/local/freetds --with-tdsver=7.1 --enable-msdblib
        make
        make install

"""
# 需要创建一个数据库

import sys

reload(sys)
sys.setdefaultencoding('utf8')
import pymssql


class SqlServerConnected(object):

    def __init__(self, host="", port=5432, username="", password="", database="mytest"):
        self.client = pymssql.connect(server=host, port=port, user=username, password=password, database=database)

    # 创建测试表
    def create_table(self):
        # 创建数据操作游标
        cursor = self.client.cursor()
        # 执行SQL
        result = cursor.execute("create table table3("
                                "p_id int primary key,"
                                "p_name varchar(20) NOT NULL,"
                                "p_sex varchar(10),"
                                "CreateTime datetime NULL DEFAULT CURRENT_TIMESTAMP)"
                                )

        cursor.execute("commit")
        # None
        print result

    # 插入数据
    def insert_data_to_table(self):
        # 创建数据操作游标
        cursor = self.client.cursor()

        # 定义插入数据列表
        sql_list = [
            "Insert into table3 (p_id,p_name,p_sex) values (1001,'a1a','zz')",
            "Insert into table3 (p_id,p_name,p_sex) values (1002,'a2a','zz')",
            "Insert into table3 (p_id,p_name,p_sex) values (1003,'a3a','zz')",
            "Insert into table3 (p_id,p_name,p_sex) values (1004,'a4a','zz')",
            "Insert into table3 (p_id,p_name,p_sex) values (1005,'a5a','zz')",
            "Insert into table3 (p_id,p_name,p_sex) values (1006,'a6a','zz')",
            "Insert into table3 (p_id,p_name,p_sex) values (1007,'a7a','zz')",
            "Insert into table3 (p_id,p_name,p_sex) values (1008,'a8a','zz')",
            "Insert into table3 (p_id,p_name,p_sex) values (1009,'a9a','zz')",
            "Insert into table3 (p_id,p_name,p_sex) values (1010,'a10a','zz')",
            "Insert into table3 (p_id,p_name,p_sex) values (1011,'a11a','zz')",
            "Insert into table3 (p_id,p_name,p_sex) values (1012,'a12a','zz')",
            "Insert into table3 (p_id,p_name,p_sex) values (1013,'a13a','zz')",
            "Insert into table3 (p_id,p_name,p_sex) values (1014,'a14a','zz')",
            "Insert into table3 (p_id,p_name,p_sex) values (1015,'a15a','zz')",
            "Insert into table3 (p_id,p_name,p_sex) values (1016,'a16a','zz')",
            "Insert into table3 (p_id,p_name,p_sex) values (1017,'a17a','zz')",
            "Insert into table3 (p_id,p_name,p_sex) values (1018,'a18a','zz')",
            "Insert into table3 (p_id,p_name,p_sex) values (1019,'a19a','zz')",
            "Insert into table3 (p_id,p_name,p_sex) values (1020,'a20a','zz')",
            "Insert into table3 (p_id,p_name,p_sex) values (1021,'a21a','zz')",
            "Insert into table3 (p_id,p_name,p_sex) values (1022,'a22a','zz')",
            "Insert into table3 (p_id,p_name,p_sex) values (1023,'a23a','zz')",
            "Insert into table3 (p_id,p_name,p_sex) values (1024,'a24a','zz')",
            "Insert into table3 (p_id,p_name,p_sex) values (1026,'张张','zz')",
            "Insert into table3 (p_id,p_name,p_sex) values (1025,'张张','zz')",
            "Insert into table3 (p_id,p_name,p_sex) values (1027,'饕餮','zz')"
        ]

        for sql in sql_list:
            cursor.execute(sql)
        #cursor.execute("commit")

        cursor.execute("select count(*) from table3")

        result = cursor.fetchone()
        #27
        print result[0]

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

        # cursor.execute("select * table3")

        # result_list = cursor.fetchall()

        # for row in result_list:
        #    result = ("p_id=%d, p_name=%s, p_sex=%s, CreateTime=%s" % (row[0], row[1], row[2], row[3]))

        #    return result
        cursor.execute("select count(*) from table3")
        result = cursor.fetchone()
        #27
        print result[0]

    # 修改表
    def update_data(self):
        # 定义游标
        cursor = self.client.cursor()

        cursor.execute("update table3 set p_name='data_new' where p_id=1027")

        cursor.execute("select p_name from table3 where p_id=1027")

        result = cursor.fetchone()
        #data_new
        print result[0]

    # 删除表
    def delete_table(self):
        # 定义游标
        cursor = self.client.cursor()

        cursor.execute("delete from  table3  where p_id=1027")

        cursor.execute("select count(*) from table3")

        result = cursor.fetchone()
        #26
        print result[0]

    # 删除表及测试数据库
    def delete_all_data(self):
        # 定义游标
        cursor = self.client.cursor()

        result = cursor.execute("drop table table3")
        #None
        print result

    # 关闭连接
    def close_conn(self):
        result = self.client.close()
        #None
        print result


if __name__ == '__main__':
    # 参数初始化
    host = ""
    port = 5432
    username = ""
    password = ""
    database = "mytest"

    mssql_con = SqlServerConnected(host=host, port=port, password=password, username=username, database=database)

    mssql_con.create_table()
    mssql_con.insert_data_to_table()
    mssql_con.get_data()
    mssql_con.update_data()
    mssql_con.delete_table()
    mssql_con.delete_all_data()
    mssql_con.close_conn()
