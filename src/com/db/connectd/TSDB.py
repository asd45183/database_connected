#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-26 10:43
# @Author  : Mr_d
# @Site    : 
# @File    : TSDB.py
"""
requirement :pip install requests
构造http 请求来测试
"""
import random
import time

import requests


class TSDBConnected(object):

    def __init__(self, host="", port=1111):
        self.base_url = "http://%s:%s" % (host, port)

        self.headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache"
        }

    # 构造请求URL
    def make_request_url(self, endpoint=""):
        rel_url = "/".join([self.base_url, endpoint])

        return rel_url

    # 查看实例内核
    def get_version(self):
        # 构造url
        url = self.make_request_url("api/version")

        result = requests.request("GET", url, headers=self.headers)

        return result

    # 插入单条数据
    def put_single_data(self):
        # 构造url
        url = self.make_request_url("api/put")

        # 构造测试数据
        data = """{
        "metric": "checkputandquery",
        "timestamp": %s,
        "value": 1,
        "tags": {
        "isok": "ok"
        }
    }"""
        body = data % (int(time.time()))

        result = requests.request("POST", url, data=body, headers=self.headers)
        return result

    # 调用last api 查询最新接口数据
    def query_single_data(self):
        # 构造url
        url = self.make_request_url("api/query/last")

        # 构造查询数据
        data = """{"queries" : [{"metric":"checkputandquery"}]}"""

        result = requests.request("POST", url, data=data, headers=self.headers)

        return result

    # 插入多条测试数据
    def put_multi_data(self):
        # 构造url
        url = self.make_request_url("api/put")

        # 构造测试数据
        data = """{
        "metric": "checkputandquery",
        "value": %s,,
        "timestamp": %s,
        "tags": {
        "building": "tower1",
        "floor": "%s"
        }
        }"""

        base_time = time.time()

        for i in range(1, 3):
            for j in range(1, 20):
                body = data % (str(random.randint(10, 30)), str(base_time - j * 60), str(i))

                result = requests.request("POST", url, data=body, headers=self.headers)
                return result

    # 查询数据 查询一段时间内 "metric"="test_data" 的值
    def query_multi_data(self):
        # 构造url
        url = self.make_request_url("api/query")

        # 构造查询数据
        end_time = int(time.time())

        # 查询过去30分钟内的数据
        start_time = end_time - 1800

        data = """
        {
        "start":%s,
        "end":%s,
        "queries":[{
            "aggregator":"avg",
            "metric":"test_data"
            }
            ]
            }"""
        query_data = data % (start_time, end_time)

        result = requests.request("POST", url, data=query_data, headers=self.headers)

        return result

    # 查询数据 指定metrics
    def query_metrics_data(self):
        """
        查询 4 条以 “my” 为前缀的指标名称。请求：POST/api/suggest请求体：
        {"type": "metrics",
        "q": "my_",
        "max": 4}
        :return:
        """
        # 构造url
        url = self.make_request_url("api/suggest")

        # 构造测试数据
        query_data = """{
        "type": "metrics",
        "q": "test_data",
        "max":100
        }"""

        result = requests.request("POST", url, data=query_data, headers=self.headers)

        return result

    # 删除数据
    def delete_metric_data(self):
        # 构造url
        url = self.make_request_url("api/delete_data")
        # 构造查询数据
        end_time = int(time.time())

        # 清楚过去30分钟内的数据
        start_time = end_time - 1800
        # 构造测试数据
        data = """{
        "metric": "checkputandquery",
        "start":%s,
        "end":%s
        }"""
        query_data = data % (start_time, end_time)

        result = requests.request("POST", url, data=query_data, headers=self.headers)

        return result

    # 删除时间线
    def delete_metric_meta(self):
        # 构造url
        url = self.make_request_url("api/delete_meta")

        data = """{
        "metric": "test_data"
        }"""
        result = requests.request("POST", url, data=data, headers=self.headers)

        return result


if __name__ == '__main__':
    host = ''
    port = 8888
    ts_con = TSDBConnected(host=host, port=port)
