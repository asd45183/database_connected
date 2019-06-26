#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:Me.D
"""
discrible:

"""
import struct

from hbase import Hbase
from thrift.protocol import TBinaryProtocol
from thrift.transport import TSocket
from thrift.transport import TTransport


# Method for encoding ints with Thrift's string encoding
def encode(n):
    return struct.pack("i", n)


# Method for decoding ints with Thrift's string encoding
def decode(s):
    return int(s) if s.isdigit() else struct.unpack('i', s)[0]


class HBaseApi(object):

    def __init__(self, table='fr_test_hbase:test_api', host='10.2.46.240', port=9090):
        self.table = table.encode('utf-8')
        self.host = host
        self.port = port
        # Connect to HBase Thrift server
        self.transport = TTransport.TBufferedTransport(TSocket.TSocket(host, port))
        self.protocol = TBinaryProtocol.TBinaryProtocolAccelerated(self.transport)

        # Create and open the client connection
        self.client = Hbase.Client(self.protocol)
        self.transport.open()
        # set type and field of column families
        self.set_column_families([bytes], ['info'])
        self._build_column_families()

    def set_column_families(self, type_list, col_list=['info']):
        self.columnFamiliesType = type_list

        self.columnFamilies = col_list

    def _build_column_families(self):
        """
        give all column families name list,create a table
        :return:
        """
        tables = self.client.getTableNames()
        if self.table not in tables:
            self.__create_table(self.table)

    def __create_table(self, table):
        """
        create table in hbase with column families
        :param table: fr_test_hbase:fr_test
        :return:
        """

        columnFamilies = []
        for columnFamily in self.columnFamilies:
            name = Hbase.ColumnDescriptor(name=columnFamily)
            columnFamilies.append(name)
        table = table.encode('utf-8')
        print(type(table), type(columnFamilies))

        self.client.createTable(table, columnFamilies)

    def __del__(self):
        self.transport.close()

    def __del_table(self, table):
        """
        delete a table,first need to disable it
        """
        self.client.disableTable(table)
        self.client.deleteTable(table)

    def getColumnDescriptors(self):
        return self.client.getColumnDescriptors(self.table)

    def put(self, rowKey, qualifier, value):
        """
        put one row
        column is column name,value is column value
        :param rowKey: rowKey
        :param column: column name
        :param value: column value
        :description: HbaseApi(table).put('rowKey','column','value')
        """

        rowKey = rowKey.encode('utf-8')
        mutations = []
        # for j, column in enumerate(column):
        if isinstance(value, str):
            value = value.encode('utf-8')
            m_name = Hbase.Mutation(column=(self.columnFamilies[0] + ':' + qualifier).encode('utf-8'), value=value)
        elif isinstance(value, int):
            m_name = Hbase.Mutation(column=(self.columnFamilies[0] + ':' + qualifier).encode('utf-8'),
                                    value=encode(value))
        mutations.append(m_name)
        self.client.mutateRow(self.table, rowKey, mutations, {})

    def puts(self, rowKeys, qualifier, values):
        """ put sevel rows, `qualifier` is autoincrement

        :param rowKeys: a single rowKey
        :param values: values is a 2-dimension list, one piece element is [name, sex, age]
        :param qualifier: column family qualifier

        Usage::

        >>> HBaseTest('table').puts(rowKeys=[1,2,3],qualifier="name",values=[1,2,3])

        """

        mutationsBatch = []
        if not isinstance(rowKeys, list):
            rowKeys = [rowKeys] * len(values)

        for i, value in enumerate(values):
            mutations = []
            # for j, column in enumerate(value):
            if isinstance(value, str):
                value = value.encode('utf-8')
                m_name = Hbase.Mutation(column=(self.columnFamilies[0] + ':' + qualifier).encode('utf-8'), value=value)
            elif isinstance(value, int):
                m_name = Hbase.Mutation(column=(self.columnFamilies[0] + ':' + qualifier).encode('utf-8'),
                                        value=encode(value))
            mutations.append(m_name)
            mutationsBatch.append(Hbase.BatchMutation(row=rowKeys[i].encode('utf-8'), mutations=mutations))
        self.client.mutateRows(self.table, mutationsBatch, {})

    def getRow(self, row, qualifier='name'):
        """
        get one row from hbase table
        :param row:
        :param qualifier:
        :return:
        """
        # res = []
        row = self.client.getRow(self.table, row.encode('utf-8'), {})
        for r in row:
            rd = {}
            row = r.row.decode('utf-8')
            value = (r.columns[b'info:name'].value).decode('utf-8')
            rd[row] = value
            # res.append(rd)
            # print ('the row is ',r.row.decode('utf-8'))
            # print ('the value is ',(r.columns[b'info:name'].value).decode('utf-8'))
            return rd

    def getRows(self, rows, qualifier='name'):
        """
        get rows from hbase,all the row sqecify the same 'qualifier'
        :param rows: a list of row key
        :param qualifier: column
        :return: None
        """
        # grow = True if len(rows) == 1 else False
        res = []
        for r in rows:
            res.append(self.getRow(r, qualifier))
        return res

    def scanner(self, numRows=100, startRow=None, stopRow=None):
        """

        :param numRows:
        :param startRow:
        :param stopRow:
        :return:
        """
        scan = Hbase.TScan(startRow, stopRow)
        scannerId = self.client.scannerOpenWithScan(self.table, scan, {})

        ret = []
        rowList = self.client.scannerGetList(scannerId, numRows)

        for r in rowList:
            rd = {}
            row = r.row.decode('utf-8')
            value = (r.columns[b'info:name'].value).decode('utf-8')
            rd[row] = value
            # print ('the row is ',r.row.decode('utf-8'))
            # print ('the value is ',(r.columns[b'info:name'].value).decode('utf-8'))
            ret.append(rd)

        return ret


def demo():
    ha = HBaseApi('fr_test_hbase:test_log1')
    # ha.put('0002','age','23')
    rowKeys = [str(key) for key in range(10001, 10010)]
    values = ['fr' + str(val) for val in range(10001, 10010)]
    ha.puts(rowKeys, 'name', values)
    print(ha.scanner())
    # print(ha.getRow('0001'))
    # print(ha.getRows(rowKeys))


if __name__ == "__main__":
    demo()
