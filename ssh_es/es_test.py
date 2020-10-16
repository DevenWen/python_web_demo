#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   es_test.py
@Time    :   2020/09/23 23:26:44
@Author  :   Liu YuanYuan :)
@Version :   1.0
@Desc    :   None
'''

# here put the import lib

from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool!',
    'timestamp': datetime.now()
}

