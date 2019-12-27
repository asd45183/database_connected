#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:Me.D
import sys,re,time
reload(sys)
sys.setdefaultencoding('utf8')
import pymysql


class MySQLConnected(object):

    def __init__(self, host="", port=3306, username="", password="",  charset="utf8", database="mytest"):
        # 初始化参数
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.charset = charset

        # 定义连接端
        self.client = pymysql.connect(user=self.username, passwd=self.password,host=self.host, port=self.port, charset=self.charset, autocommit=True,connect_timeout=10)
        self.__create_database(database)

        time.sleep(0.2)
        print("reset connect .............")
        # 定义连接端
        self.client = pymysql.connect(host=self.host, port=self.port, user=self.username, passwd=self.password,database=database,
                                       charset=self.charset, autocommit=True,connect_timeout=10)
    def __create_database(self, database):
        # 创建数据操作游标
        cursor =self.client.cursor()
        # 执行SQL
        print "配置数据库，5 S 后开始执行，若该库已存在则删除......"

        time.sleep(5)
        print("start .............")
        cursor.execute("drop database if exists" + database)
        cursor.execute("CREATE DATABASE " + database + " default charset utf8 COLLATE utf8_general_ci")

    # 创建测试表
    def create_table(self):
        # 创建数据操作游标
        cursor = self.client.cursor()
        # 执行SQL

        cursor.execute("DROP TABLE IF EXISTS table3")

        result = cursor.execute(
            "create table table3("
            "p_id int primary key,"
            "p_name varchar(20) NOT NULL,"
            "p_sex varchar(10),"
            "CreateTime datetime NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间')"
            " ENGINE  =  INNODB    DEFAULT  CHARSET  =  utf8mb4 "
        )
        #cursor.execute("commit")
        cursor.close()
        print result

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
            print ("Start insert .........")
            cursor.execute(sql)
            print ("Start endINsert .........")
        print ("Start check .........")
        cursor.execute("select count(*) from table3")
        result = cursor.fetchone()

        assert result[0] == 27, "Insert Fail......"

    def insert_multi_data(self, counts):
        cursor = self.client.cursor()
        # create new table
        cursor.execute(
            "create table table4("
            "p_id int AUTO_INCREMENT PRIMARY KEY,"
            "p_name varchar(20) NOT NULL,"
            "p_sex varchar(10),"
            "CreateTime datetime NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间')"
            " ENGINE  =  INNODB    DEFAULT  CHARSET  =  utf8mb4 ")

        for count in range(1, counts):
            sql_insert = "Insert into table4 (p_name,p_sex) values ('test_data_"+str(count)+"','zz')"
            print("prepare insert: " + sql_insert)
            cursor.execute(sql_insert)
            print ("prepare to check sql have been inserted....")
            cursor.execute("select count(p_id) from table4")
            query_result = cursor.fetchone()[0]
            assert query_result == count, "Insert error,please check.... "
            print ("Insert Success , data number is: " + str(query_result))
            time.sleep(0.1)


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

        cursor.execute("select count(*) from table3")

        result = cursor.fetchone()

        # 数据应被删除，所以返回结果即可
        print result[0]

        # result_list = cursor.fetchall()

    """
        for row in result:
            print ("p_id=" + str(row[0]) + "p_name=" + str(row[1]) + "p_sex=" + str(
                row[2]) + "CreateTime=" + str(row[3]))
"""

    #  for row in result_list:
    #      result = ("p_id=%d, p_name=%s, p_sex=%s, CreateTime=%s" % (row[0], row[1], row[2], row[3]))
    #
    #     print result

    # 修改表
    def update_data(self):
        # 定义游标
        cursor = self.client.cursor()

        cursor.execute("update table3 set p_name='data_new' where p_id=1027")

        #cursor.execute("commit")

        cursor.execute("select p_name from table3 where p_id=1027")

        result = cursor.fetchone()

        # 返回修改后的值，1 表示第二个值 即 p_name
        print result[0]

    # 删除表中内容
    def delete_table(self):
        # 定义游标
        cursor = self.client.cursor()

        cursor.execute("delete from  table3  where p_id=1027")

        #cursor.execute("commit")

        cursor.execute("select count(* ) from table3 ")

        result = cursor.fetchone()

        # 数据应被删除，所以返回结果即可
        print result[0]

    # 删除表及测试数据库
    def delete_all_data(self):
        # 定义游标
        cursor = self.client.cursor()
        result = cursor.execute("Drop database" + database)
        print result

    # 关闭连接
    def close_conn(self):
        result = self.client.close()

        print result

    def check_tde(self):
        cursor = self.client.cursor()
        # open tde
        cursor.execute("alter table table3 engine=innodb, block_format=encrypted")
        cursor.execute("show create table table3")
        result = str(cursor.fetchall())
        print result
        assert re.search(r'ENCRYPTED', result), 'TDE没有开启'
# 创建一个测试库：test_db


if __name__ == '__main__':
    # 初始化数据,请使用高权限账号
    host = "127.0.0.1"
    port = 3306
    username = "root"
    password = "123456"
    database = ""
    charset = "utf8"

    # 初始化对象
    my_con = MySQLConnected(host=host, port=port, username=username, password=password, database=database,
                            charset=charset)
    my_con.create_table()
    my_con.get_data()
    my_con.update_data()
    my_con.get_data()
    my_con.delete_all_data()
