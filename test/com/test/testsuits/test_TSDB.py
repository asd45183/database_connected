#!/anaconda3/envs/python2.7/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-26 16:00
# @Author  : Mr_d
# @Site    : 
# @File    : test_TSDB.py
# 使用pytest执行
# 引入被测类
import os

# 引入公共配置
import pytest

from src.com.conf.common_config import get_err_line
from src.com.conf.commonlog import Logger
from src.com.db.connectd import TSDBConnected

log = Logger("TestTSDB")


class TestTSDB(object):

    @classmethod
    def setup_class(cls):

        # 这里定义测试数据
        host = ''
        port = 3242
        try:
            cls.ts_con = TSDBConnected(host=host, port=port)
        except:
            log.error("TestMethod---------ERROR")
            log.error("初始化错误，程序结束")
            pytest.skip(msg="始化错误")
        else:
            log.info("TestMethod--------START")
        return cls.ts_con

    @classmethod
    def teardown_class(cls):
        log.info("TestMethod--------END")
        pytest.exit("测试完成")

    def test_get_version(self):
        result = self.ts_con.get_version()
        assert result.status_code == 200, log.error("测试失败，错误方法为：%r,错误行数为 %r" % get_err_line())
        # 输出内核
        log.debug("version:" + result.json()['version'])

    def test_put_single_data(self):
        result = self.ts_con.put_single_data()
        assert result.status_code == 204, log.error("测试失败，错误方法为：%r,错误行数为 %r" % get_err_line())
        log.debug(result)

    def test_query_metrics_data(self):
        result = self.ts_con.query_metrics_data()
        assert result.status_code == 200, log.error("测试失败，错误方法为：%r,错误行数为 %r" % get_err_line())
        log.debug(result.text)

    def test_put_multi_data(self):
        assert self.ts_con.put_multi_data().status_code == 204, log.error("测试失败，错误方法为：%r,错误行数为 %r" % get_err_line())
        log.debug(self.ts_con.put_multi_data().text)

    def test_query_multi_data(self):
        result = self.ts_con.query_multi_data()
        assert result.status_code == 200, log.error("测试失败，错误方法为：%r,错误行数为 %r" % get_err_line())
        log.debug(result.json())

    def test_delete_metric_data(self):
        result = self.ts_con.delete_metric_data()
        assert result.status_code == 200, log.error("测试失败，错误方法为：%r,错误行数为 %r" % get_err_line())
        log.debug(result.text)

    def test_delete_metric_meta(self):
        result = self.ts_con.delete_metric_meta()
        assert result.status_code == 200, log.error("测试失败，错误方法为：%r,错误行数为 %r" % get_err_line())
        log.debug(result.text)


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    cmd = 'python -m  pytest %s --html=%s' % (
    __file__, '/Users/dingyq/python_study/db_connected/test/com/test/test.html')
    os.system(cmd)
