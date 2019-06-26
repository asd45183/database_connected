# -*- coding: UTF-8 -*-
# author:Me.D
#!/usr/bin/env bash
#!/usr/bin/env python2.7
#!/bin/bash
echo '$0: '$0
echo "pwd: "`pwd`
echo "=================================================>start"

# 获取并传递当前文件所在路径
CURDIR=$(cd $(dirname ${BASH_SOURCE[0]}); pwd )
base_dir=$CURDIR/require_packages

# 输出日志
exec 2>&1>> $CURDIR/setup.log

# 定义依赖名称
pymongo_need=pymongo-3.8.0.tar.gz
pymongo_client=pymongo-3.8.0
redis_need="six-1.9.0-py2.py3-none-any.whl"
redis_tar="redis-py-master.tar.gz"
redis_py_tar="redis-py-master"
memcache_need="python-binary-memcached-0.26.1.tar"
memcache_tar="python-binary-memcached-0.26.1"
hbase_tar="hbase-thrift-0.20.4.tar.gz"
hbase_tar_1="thrift-0.11.0.tar.gz"
hbase_tar_c="hbase-thrift-0.20.4"
hbase_tar_1_c="thrift-0.11.0"

# 安装依赖 pytest
source activate python2.7 && pip install pytest

# 解压文件

cd $base_dir && \

tar -zxvf $pymongo_need &&\
tar -zxvf $redis_tar && \
tar -xvf $memcache_need && \
tar -zxvf $hbase_tar && \
tar -zxvf $hbase_tar_1


# pip 安装
pip install $redis_need && \
pip install psycopg2-binary && \
pip install cx_Oracle && \
pip install requests

# 安装依赖 mongo, redis,  memcache, hbase,
cd $base_dir/$pymongo_client/ && python setup.py install && \

cd $base_dir/$redis_py_tar/ && python setup.py install && \

cd $base_dir/$memcache_tar && python setup.py install && \

cd $base_dir/$hbase_tar_c && python setup.py install && \

cd $base_dir/$hbase_tar_1_c && python setup.py install

