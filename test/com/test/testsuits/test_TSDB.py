#!/anaconda3/envs/python2.7/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-26 16:00
# @Author  : Mr_d
# @Site    : 
# @File    : test_TSDB.py

# 引入被测类
from . import TSDBConnected

# 引入公共配置
import pytest
import os
from . import Logger
from . import get_err_line

log = Logger("TestTSDB")


class TestTSDB(object):
    
    @pytest.fixture()
    def ts_init(self):

        # 这里定义测试数据
        host = ''
        port = 3242
        ts_conn = TSDBConnected(host=host, port=port)
        log.info("TestMethod--------START")
        yield ts_conn
        log.info("TestMethod--------END")

    @pytest.mark.run(order=1)
    def test_get_version(self, ts_init):
        result = ts_init.get_version()
        assert result.status_code == 200, log.error("测试失败，错误方法为：%r,错误行数为 %r" % get_err_line())
        # 输出内核
        log.debug("version:" + result.json()['version'])

    def test_put_single_data(self, ts_init):
        result = ts_init.put_single_data()
        assert result.status_code == 204, log.error("测试失败，错误方法为：%r,错误行数为 %r" % get_err_line())
        log.debug(result)

    def test_query_metrics_data(self, ts_init):
        result = ts_init.query_metrics_data()
        assert result.status_code == 200, log.error("测试失败，错误方法为：%r,错误行数为 %r" % get_err_line())
        log.debug(result.text)

    def test_put_multi_data(self, ts_init):
        assert ts_init.put_multi_data().status_code == 204, log.error("测试失败，错误方法为：%r,错误行数为 %r" % get_err_line())
        log.debug(ts_init.put_multi_data().text)

    def test_query_multi_data(self, ts_init):
        result = ts_init.query_multi_data()
        assert result.status_code == 200, log.error("测试失败，错误方法为：%r,错误行数为 %r" % get_err_line())
        log.debug(result.json())

    def test_delete_metric_data(self, ts_init):
        result = ts_init.delete_metric_data()
        assert result.status_code == 200, log.error("测试失败，错误方法为：%r,错误行数为 %r" % get_err_line())
        log.debug(result.text)

    def test_delete_metric_meta(self, ts_init):
        result = ts_init.delete_metric_meta()
        assert result.status_code == 200, log.error("测试失败，错误方法为：%r,错误行数为 %r" % get_err_line())
        log.debug(result.text)



if __name__ == '__main__':

    os.chdir(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    cmd = 'python -m  pytest %s --html=%s' % (__file__, '/Users/dingyq/python_study/db_connected/test/com/test/test.html')
    os.system(cmd)


