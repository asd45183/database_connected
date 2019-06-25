#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:Me.D

import pymysql


class MySQLConnected:

    def __init__(self, host="", port=3306, username="", password="", database="", charset="utf8"):

        # 初始化参数
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.charset = charset

        # 定义连接端
        self.client = pymysql.connect(database=self.database, user=self.username, passwd=self.password,
                                      host=self.host, port=self.port, charset=self.charset)

    # 创建一个测试库：test_db
    def create_database(self):

        # 创建数据操作游标
        cursor = self.client.cursor()

        # 执行SQL
        cursor.execute("CREATE DATABASE test_db WITH ENCODING='utf8';")

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
        cursor.execute("USE test_db;")

        cursor.execute("DROP TABLE IF EXISTS table3;")

        cursor.execute(
            "create table table3("
            "p_id int primary key,"
            "p_name varchar(20) NOT NULL,"
            "p_sex varchar(10),"
            "CreateTime datetime NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间')"
            " ENGINE  =  INNODB    DEFAULT  CHARSET  =  utf8mb4 ;"
        )

        cursor.fetchone()
        cursor.close()

    def insert_data_to_table(self):

        # 创建数据操作游标
        cursor = self.client.cursor()

        cursor.execute("USE test_db;")

        cursor.execute(
            "Insert into table3 (p_id,p_name,p_sex) values (1001,'a1a','zz');"
            "Insert into table3 (p_id,p_name,p_sex) values (1002,'a2a','zz');"
            "Insert into table3 (p_id,p_name,p_sex) values (1003,'a3a','zz');"
            "Insert into table3 (p_id,p_name,p_sex) values (1004,'a4a','zz');"
            "Insert into table3 (p_id,p_name,p_sex) values (1005,'a5a','zz');"
            "Insert into table3 (p_id,p_name,p_sex) values (1006,'a6a','zz');"
            "Insert into table3 (p_id,p_name,p_sex) values (1007,'a7a','zz');"
            "Insert into table3 (p_id,p_name,p_sex) values (1008,'a8a','zz');"
            "Insert into table3 (p_id,p_name,p_sex) values (1009,'a9a','zz');"
            "Insert into table3 (p_id,p_name,p_sex) values (1010,'a10a','zz');"
            "Insert into table3 (p_id,p_name,p_sex) values (1011,'a11a','zz');"
            "Insert into table3 (p_id,p_name,p_sex) values (1012,'a12a','zz');"
            "Insert into table3 (p_id,p_name,p_sex) values (1013,'a13a','zz');"
            "Insert into table3 (p_id,p_name,p_sex) values (1014,'a14a','zz');"
            "Insert into table3 (p_id,p_name,p_sex) values (1015,'a15a','zz');"
            "Insert into table3 (p_id,p_name,p_sex) values (1016,'a16a','zz');"
            "Insert into table3 (p_id,p_name,p_sex) values (1017,'a17a','zz');"
            "Insert into table3 (p_id,p_name,p_sex) values (1018,'a18a','zz');"
            "Insert into table3 (p_id,p_name,p_sex) values (1019,'a19a','zz');"
            "Insert into table3 (p_id,p_name,p_sex) values (1020,'a20a','zz');"
            "Insert into table3 (p_id,p_name,p_sex) values (1021,'a21a','zz');"
            "Insert into table3 (p_id,p_name,p_sex) values (1022,'a22a','zz');"
            "Insert into table3 (p_id,p_name,p_sex) values (1023,'a23a','zz');"
            "Insert into table3 (p_id,p_name,p_sex) values (1024,'a24a','zz');"
            "Insert into table3 (p_id,p_name,p_sex) values (1026,'张张','zz');"
            "Insert into table3 (p_id,p_name,p_sex) values (1025,'张张','zz');"
            "Insert into table3 (p_id,p_name,p_sex) values (1027,'饕餮','zz');"
            )

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

        cursor.execute("select * from table3;")

        result = cursor.fetchall()

        for row in result:
            return ("p_id=" + str(row[0]) + "p_name=" + str(row[1]) + "p_sex=" + str(
                row[2]) + "CreateTime=" + str(row[3]))

    # 修改表
    def update_date(self):

        # 定义游标
        cursor = self.client.cursor()

        cursor.execute("USE test_db;")

        cursor.execute("update table3 set p_name='date_new' where p_id=1027;")

        cursor.execute("select * from table3 where p_id=1027;")

        result = cursor.fetchone()

        # 返回修改后的值，1 表示第二个值 即 p_name
        return (result[1])

    # 删除表
    def delete_date(self):

        # 定义游标
        cursor = self.client.cursor()

        cursor.execute("USE test_db;")

        cursor.execute("delete from  table3  where p_id=1027;")

        cursor.execute("select * from table3 where p_id=1027;")

        result = cursor.fetchone()

        # 数据应被删除，所以返回结果即可
        return (result)

    # 关闭连接
    def close_conn(self):

        result = self.client.close()

        return (result)


if __name__ == '__main__':
    pass
