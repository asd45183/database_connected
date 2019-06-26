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
base_url = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
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
        assert ts_init.get_version().status_code == 200
        log.debug('\n')
        # 输出内核
        log.debug(ts_init.get_version().json()['version'])

    def test_put_single_data(self, ts_init):
        log = logging.getLogger("test_put_single_data")
        assert ts_init.put_single_data().status_code == 204

    def test_query_metrics_data(self, ts_init):
        log = logging.getLogger("test_query_metrics_data")
        assert ts_init.query_metrics_data().status_code == 200
        log.debug(ts_init.query_metrics_data().text)

    def test_put_multi_data(self, ts_init):
        log = logging.getLogger("test_put_multi_data")
        assert ts_init.put_multi_data().status_code == 204
        log.debug(ts_init.put_multi_data().text)

    def test_query_multi_data(self, ts_init):
        log = logging.getLogger("test_query_multi_data")
        assert ts_init.query_multi_data().status_code == 200
        log.debug(ts_init.delete_metric_data().json())

    def test_delete_metric_data(self, ts_init):
        log = logging.getLogger("test_delete_metric_data")
        assert ts_init.delete_metric_data().status_code == 200
        log.debug(ts_init.delete_metric_data().text)

    def test_delete_metric_meta(self, ts_init):
        log = logging.getLogger("test_delete_metric_meta")
        assert ts_init.delete_metric_meta().status_code == 200
        log.debug(ts_init.delete_metric_meta().text)


if __name__ == '__main__':
    pytest.main('-s')
