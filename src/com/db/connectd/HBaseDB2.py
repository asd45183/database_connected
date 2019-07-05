#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-03 14:04
# @Author  : Mr_d
# @Site    : 
# @File    : HBaseDB2.py

# import need
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from hbase import Hbase
from hbase.ttypes import *


class HBaseDB2(object):

    def __init__(self, host='', port=9090):

        transport = TSocket.TSocket(host=host, port=port)
        self.transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        self.client = Hbase.Client(protocol)
        self.transport.open()

    def create_table(self):
        # init Column family
        contents = ColumnDescriptor(name='cf:a',maxVersions=1)
        # create table test_table
        result = self.client.createTable('test_table',[contents])
        # None
        print (result)

    def insert_row_data(self):
        row = 'row-key1'
        mutations = [Mutation(column='cf:a', value='1')]
        result = self.client.mutateRow('test_table', row=row, mutations=mutations)
        # None
        print (result)

    def query_row_data(self):
        result = self.client.getRow(tableName='test_table', row='row-key1')
        # example:[TRowResult(columns={'cf:a': TCell(timestamp=1562135256850, value='1')}, row='row-key1')]
        for item in result:
            print("the row is", item.row)
            # dict 类型 {'cf:a': TCell(timestamp=1562135256850, value='1')}
            # <class 'hbase.ttypes.TCell'>
            print ("the values is ", item.columns.get('cf:a').value)

    def insert_multi_row_data(self):

        mutation = Mutation(column='cf:a',value='test_data2')
        batchMutation = BatchMutation('row1',mutations=[mutation])
        result = self.client.mutateRows(tableName='test_table', rowBatches=batchMutation)

    def replace_row_data(self):
        mutations = [Mutation(column='cf:a', value='2')]
        result = self.client.mutateRow(tableName='test_table', row='row-key1',mutations=mutations)
        print (result)


if __name__ == '__main__':

    hb_con = HBaseDB2(host='', port=9099)
    hb_con.create_table()

