#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-26 16:00
# @Author  : Mr_d
# @Site    : 
# @File    : test_TSDB.py
import logging
import os

import pytest

from src.com.db.connectd.TSDB import TSDBConnected

# 定位到项目目录
base_url = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))))
log_url = base_url + "/testfiles/log/TestTSDB.log"


class TestTSDB(object):
    logging.basicConfig(level=logging.DEBUG, filename=log_url)

    @pytest.fixture()
    def ts_init(self):
        host = ''
        port = 8888
        ts_conn = TSDBConnected(host=host, port=port)

        yield ts_conn

    def test_get_version(self, ts_init):
        log = logging.getLogger("test_get_version")
        result = ts_init.get_version()
        assert result.status_code == 200
        log.debug('\n')
        # 输出内核
        log.debug(result.json()['version'])

    def test_put_single_data(self, ts_init):
        log = logging.getLogger("test_put_single_data")
        result = ts_init.put_single_data()
        assert result.status_code == 204
        log.debug(result)

    def test_query_metrics_data(self, ts_init):
        log = logging.getLogger("test_query_metrics_data")
        result = ts_init.query_metrics_data()
        assert result.status_code == 200
        log.debug(result.text)

    def test_put_multi_data(self, ts_init):
        log = logging.getLogger("test_put_multi_data")
        assert ts_init.put_multi_data().status_code == 204
        log.debug(ts_init.put_multi_data().text)

    def test_query_multi_data(self, ts_init):
        log = logging.getLogger("test_query_multi_data")
        result = ts_init.query_multi_data()
        assert result.status_code == 200
        log.debug(result.json())

    def test_delete_metric_data(self, ts_init):
        log = logging.getLogger("test_delete_metric_data")
        result = ts_init.delete_metric_data()
        assert result.status_code == 200
        log.debug(result.text)

    def test_delete_metric_meta(self, ts_init):
        log = logging.getLogger("test_delete_metric_meta")
        result = ts_init.delete_metric_meta()
        assert result.status_code == 200
        log.debug(result.text)


if __name__ == '__main__':
    pytest.main('-s')
