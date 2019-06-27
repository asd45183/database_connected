# -*- coding: UTF-8 -*-
# author:Me.D
#!/usr/bin/env bash
#!/bin/bash
<<!
exapmle1: sh startandreport.sh mytest.py mytest
example2: sh startandreport.sh mytest.py
!
echo '$0: '$0
echo "pwd: "`pwd`
echo "=================================================>start"

test_case=$1

# 获取并传递当前文件所在路径
CURDIR=$(cd $(dirname $0); pwd)

report_url=$CURDIR/testfiles/report

testsuilt_url=$CURDIR/test/com/test/testsuits

# 激活测试环境
source activate python2.7

start(){
        echo "需要执行的测试脚本是:"$test_case

        echo "开始执行测试,测试报告存放于："$report_url/$report_name.html
        # 执行测试并输出
        python -m  pytest $testsuilt_url/$test_case --html=$report_url/$report_name.html --self-contained-html
}

# 仅传入测试脚本名称
if [ $# -eq 1 ];
then
    if [ {$test_case#*.py} ]; then

        # 截取.py 前的文件名作为报告名称
        report_name=$(echo ${test_case%%.py*})

        # 调用方法
        start

    else
        echo "传入的参数错误，传入的参数不是.py文件"
    fi
# 传入测试脚本名称和报告名称
elif [ $# -eq 2 ]; then
    report_name=$2
    start

else
    echo "传入的参数错误,不符合要求"
fi


