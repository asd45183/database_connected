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

# 定义软件安装目录
SD_1="/root/rds_softs"
# 输出日志
exec 2>&1>> $base_dir/setup.log
# 定义依赖名称
pymongo_need=pymongo-3.8.0.tar.gz
pymongo_client=pymongo-3.8.0
redis_need="six-1.9.0-py2.py3-none-any.whl"
redis_tar="redis-py-master.tar.gz"
redis_py_tar="redis-py-master"
memcache_need="python-binary-memcached-0.26.1.tar"
memcache_tar="python-binary-memcached-0.26.1"
hbase_cli_tar="alihbase-1.1.4-bin.tar.gz"
# 安装依赖 pytest
source activate python2.7 && pip install pytest
# 解压文件
cd $base_dir && \

tar -zxvf $pymongo_need &&\
tar -zxvf $redis_tar && \
pip install $redis_need && \
pip install psycopg2-binary
tar -xvf $memcache_need && \



# 安装依赖 mongo
cd $base_dir/$pymongo_client/ && python setup.py install && \

cd $base_dir/$redis_py_tar/ && python setup.py install && \

cd $base_dir/$memcache_tar && python setup.py install

