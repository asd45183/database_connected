#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/25 20:13
# @Author  : Mr_d
# @Site    : 
# @File    : OracleDB.py
#
"""
requirement: pip install cx_Oracle,
报错： no module name 可参考指导链接：https://www.jb51.net/article/106295.htm
https://www.cnblogs.com/leihenqianshang/articles/4522837.html
"""
import os

# add oci.dll  to your python's site-packages
import cx_Oracle

# 设置字符集编码
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


class OracleConnected(object):

    def __init__(self, host="", port=1521, username="", password="", database=""):
        # 初始化参数
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database

        # 初始化链接
        url = '%s/%s@%s:%s/%s' % (self.username, self.password, self.host, self.port, self.database)
        self.client = cx_Oracle.connect(url)

        """
        another method:
        # base_url = cx_Oracle.makedsn(self.host, self.port, self.database)
        # self.client =cx_Oracle.connect(self.username, self.password, base_url)
        """

    # 创建表
    def create_table(self):

        # 定义游标
        cursor = self.client.cursor()

        """
        try:


            #  插入Oracle 的SQL 语句切记不要带‘;’,否则会抛出异常
            # 解析sql语句
            cursor.parse("create table EMP ("
                           "EMPNO NUMBER(4) PRIMARY KEY,"
                           "ENAME VARCHAR2(10),"
                           "JOB VARCHAR2(9),"
                           "MGR NUMBER(4),"
                           "HIREDATE DATE,"
                           "SAL NUMBER(7,2),"
                           "COMM NUMBER(7,2),"
                           "DEPNO NUMBER(4))"
                           )
        except cx_Oracle.DatabaseError as e:
            print(e)
        """

        # 执行语句
        try:
            cursor.execute("create table EMP ("
                           "EMPNO NUMBER(4) PRIMARY KEY,"
                           "ENAME VARCHAR2(10),"
                           "JOB VARCHAR2(9),"
                           "MGR NUMBER(4),"
                           "HIREDATE DATE,"
                           "SAL NUMBER(7,2),"
                           "COMM NUMBER(7,2),"
                           "DEPNO NUMBER(4))"
                           )
        except cx_Oracle.DataError as e:
            print (e)

        finally:
            result = cursor.execute("commit")
            # 关闭游标
            cursor.close()
            return result

    # 插入测试数据
    def insert_test_data(self):
        # 定义游标
        cursor = self.client.cursor()
        # 初始化插入的数据
        sql_list = ["INSERT INTO EMP VALUES (7369,'SMITH','CLERK',7902,to_date('17-12-1980','dd-mm-yyyy'),800,null,20)",
                    "INSERT INTO EMP VALUES (7499, 'ALLEN', 'SALESMAN', 7698, to_date('20-2-1981','dd-mm-yyyy'), 1600, 300, 30)",
                    "INSERT INTO EMP VALUES (7521, 'WARD', 'SALESMAN', 7698, to_date('22-2-1981', 'dd-mm-yyyy'), 1250, 500, 30)",
                    "INSERT INTO EMP VALUES (7566, 'JONES', 'MANAGER', 7839, to_date('2-4-1981', 'dd-mm-yyyy'), 2975, NULL, 20)",
                    "INSERT INTO EMP VALUES (7654, 'MARTIN', 'SALESMAN', 7698, to_date('28-9-1981','dd-mm-yyyy'), 1250, 1400, 30)",
                    "INSERT INTO EMP VALUES (7698, 'BLAKE', 'MANAGER', 7839, to_date('1-5-1981', 'dd-mm-yyyy'), 2850, NULL, 30)",
                    "INSERT INTO EMP VALUES (7782, 'CLARK', 'MANAGER', 7839, to_date('9-6-1981', 'dd-mm-yyyy'), 2450, NULL, 10)",
                    "INSERT INTO EMP VALUES (7839, 'KING', 'PRESIDENT', NULL, to_date('17-11-1981','dd-mm-yyyy'), 5000, NULL, 10)",
                    "INSERT INTO EMP VALUES (7844, 'TURNER', 'SALESMAN', 7698, to_date('8-9-1981','dd-mm-yyyy'), 1500, 0, 30)",
                    "INSERT INTO EMP VALUES (7900, 'JAMES', 'CLERK', 7698, to_date('3-12-1981', 'dd-mm-yyyy'), 950, NULL, 30)",
                    "INSERT INTO EMP VALUES (7902, 'FORD', 'ANALYST', 7566, to_date('3-12-1981', 'dd-mm-yyyy'), 3000, NULL, 20)",
                    "INSERT INTO EMP VALUES (7934, 'MILLER', 'CLERK', 7782, to_date('23-1-1982','dd-mm-yyyy'), 1300,NULL, 10)"
                    ]
        # sql = "INSERT INTO EMP VALUES (7369,'SMITH','CLERK',7902,to_date('17-12-1980','dd-mm-yyyy'),800,null,20)"
        try:
            for sql in sql_list:
                # 插入数据
                # print(sql)
                cursor.execute(sql)
            cursor.execute("commit")

        except cx_Oracle.DatabaseError as e:
            print (e)

        finally:
            cursor.execute("select count(*) from EMP")
            result = cursor.fetchone()
            # 关闭游标
            cursor.close()
            return result[0]

    # 修改用户密码
    def update_user_password(self):

        # 重定向client
        # 需要sys(用户）, syspassword
        url = 'sys/123456@%s:%s/%s' % (self.host, self.port, self.database)
        # 定义游标
        client = cx_Oracle.connect(url, mode=cx_Oracle.SYSDBA)
        cursor = client.cursor()
        sql = "alter user %s identified by %s " % (self.username, self.password)
        try:
            # 修改用户密码
            cursor.execute(sql)
        except cx_Oracle.DatabaseError as e:
            print (e)
        else:
            result = cursor.execute("commit")
            return result

    # 删除测试数据
    def delete_test_data(self):
        # 定义游标
        cursor = self.client.cursor()
        try:
            sql = "DELETE FROM EMP WHERE EMPNO = 7369"
            cursor.execute(sql)
        except cx_Oracle.DatabaseError as e:
            print (e)
        finally:
            cursor.execute("commit")
            cursor.execute("select count(*) from EMP")
            result = cursor.fetchone()
            return result[0]

    # 删除表
    def delete_table(self):
        # 定义游标
        cursor = self.client.cursor()
        try:
            # 删除表
            cursor.execute(
                "DROP TABLE EMP"
            )
            cursor.execute("select * from EMP")
        except cx_Oracle.DatabaseError as e:
            print (e)
        finally:
            result = cursor.execute("commit")
            # 关闭游标
            cursor.close()
            print result

    # 关闭客户端
    def close_client(self):

        result = self.client.close()
        print result


if __name__ == '__main__':
    # 初始化测试数据
    host = '127.0.0.1'
    port = 1521
    username = 'gioi'
    password = '123456'
    database = 'orcl'

    # 初始化对象
    ora_con = OracleConnected(host=host, port=port, username=username, password=password, database=database)
    # ora_con.create_table()
    # ora_con.insert_test_data()
    # ora_con.delete_test_data()
    # ora_con.delete_table()
    # ora_con.update_user_password()
    ora_con.close_client()
