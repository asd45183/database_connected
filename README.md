name: 几种常见的数据库连接方法

CODE: Python 2.7.15 |Anaconda, Inc.| OR Other env

框架: pytest

依赖文件目录：require_packages

安装文件：setup.sh --部分需要自行安装

方法目录：src/com/db/connectd --可进入目录调用方法

测试目录: test/com/test/testsuits

外部测试脚本：startandreport.sh

exapmle1: sh startandreport.sh mytest.py mytest
example2: sh startandreport.sh mytest.py

requiremen_list:
python ==> 2.7
       ==> pip install pytest
       ==> pip install logging
       ==> pip install colorama
       ==> pip install pytest-html
       ==> pip install pytest-ordering


mongo ==> pymongo-3.8.0.tar.gz

memcached ==> python-binary-memcached-0.26.1.tar

need ==> pip install six-1.9.0-py2.py3-none-any.whl

redis ==> redis-py-master.tar.gz

postgres ==> pip install psycopg2-binary

Oracle ==> pip install cx_Oracle

TSDB ==> pip install requests

hbase ==> pip install thrift
      ==> pip install hbase-thrift
