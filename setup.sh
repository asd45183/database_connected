#!/usr/bin/env bash
#!/usr/bin/env python2.7
#!/bin/bash
echo '$0: '$0
echo "pwd: "`pwd`
echo "=================================================>start"

# 获取并传递当前文件所在路径
CURDIR=$(cd $(dirname ${BASH_SOURCE[0]}); pwd )
base_dir=$CURDIR/require_packages

echo $base_dir

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
psql_cli="psycopg2_binary-2.7.3.2-cp27-cp27mu-manylinux1_x86_64.whl"
pymssql_tar="pymssql-2.1.4.tar.gz"
pymssql_cli="pymssql-2.1.4"
cx_Oracle_cli="cx_Oracle-7.1.3-cp27-cp27mu-manylinux1_x86_64.whl"
pymysql_tar="PyMySQL-0.9.3.tar.gz"
pymysql_cli="PyMySQL-0.9.3"
unixODBC_tar='unixODBC-2.3.7.tar.gz'
unixODBC_cli='unixODBC-2.3.7'
tsql_tar='freetds-current.tar.gz'
tsql_cli='freetds-dev.1.00.514'
Cython_tar='Cython-0.29.13.tar.gz'
Cython_cli='Cython-0.29.13'
setuptools_git='setuptools_git-1.2-py2.py3-none-any.whl'
instantclient_zip='instantclient-basiclite-linux.x64-11.2.0.4.0.zip'
instantclient='instantclient-basiclite-linux.x64-11.2'
# 安装依赖 pytest
# source activate python2.7 && pip install pytest

# 解压文件
cd $base_dir && \

tar -zxvf $pymongo_need &&\
tar -zxvf $redis_tar && \
tar -xvf $memcache_need && \
tar -zxvf $hbase_tar && \
tar -zxvf $hbase_tar_1 && \
tar -zxvf $pymssql_tar && \
tar -zxvf $pymysql_tar && \
tar -zxvf $unixODBC_tar && \
tar -zxvf $tsql_tar && \
tar -zxvf $Cython_tar &&


# pip 安装
pip install $redis_need && \
cd $base_dir && pip install $setuptools_git && \
# pip install requests
### 安装pymsql
yum install python-dev*
# 安装依赖 mongo, redis,  memcache, hbase,
cd $base_dir/$pymongo_client/ && python setup.py install && \

cd $base_dir/$redis_py_tar/ && python setup.py install && \

cd $base_dir/$memcache_tar && python setup.py install && \

cd $base_dir && pip install $psql_cli && \

cd $base_dir/$pymysql_cli && python setup.py install && \

echo "配置 oracle --start"

cd $base_dir && pip install $cx_Oracle_cli && \

cd $base_dir && pip install $setuptools_git && \

cd $base_dir && unzip $instantclient_zip && \

mkdir -p mkdir /opt/oracle && cp -r $instantclient /opt/oracle && \

sudo sh -c "echo /opt/oracle/instantclient_11_2 > /etc/ld.so.conf.d/oracle-instantclient.conf" && \

sudo ldconfig && echo "配置 oracle --end"  && \


# cd $base_dir/$hbase_tar_1_c && python setup.py install && \

# cd $base_dir/$hbase_tar_c && python setup.py install && \

# 安装Cython
cd $base_dir/$Cython_cli && python setup.py install && \

cd $base_dir/$unixODBC_cli && \

./configure --prefix=/usr/local/unixODBC --enable-gui=no --enable-drivers=no --with-qt-dir=/usr/lib/qt-3.3 &&\

make && make install && \

echo "...."

cd $base_dir/$tsql_cli/ && \

./configure && \

make && make install

echo "......"
echo "......"
echo "检测安装"

tsql -C

# echo $? 获取上一条命令执行后的状态，执行成功后应为0
out=$(echo $?)

if [ "$out"x == "0"x  ]; then
	echo "tsql 安装完成......"
else
	echo "ERROR , tsql 安装失败，请检查"
fi

cd $base_dir/$pymssql_cli &&  python setup.py install && \

ehcho "exit..."
