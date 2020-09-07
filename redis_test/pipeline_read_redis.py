#!/usr/bin/python3
# -*- coding:UTF-8 -*-
'''
 @AUTHOR: kangqiang.w :)
 @FILE: ~/learn/python_web_demo/redis_test/pipeline_read_redis.py
 @DATE: 2020/09/07 周一
 @TIME: 11:43:16

# DESCRIPTION:

实验结构：
createDate: 5.93s
countList_V1 1.48s
countList_V2_with_pipeline: 69.48ms
'''

import redis
from stopwatch import Stopwatch

client = redis.StrictRedis(host="redis.qpm.com", port=16379, db=0)


def createData():
    '''
    创建 500 个 Sorted List，每个 Sorted List 创建 100个数据
    '''
    stopwatch = Stopwatch()
    stopwatch.start()
    pipe = client.pipeline()
    for x in range(0, 500):
        for v in range(0, 100):
            pipe.zadd(getProjectName(x), {
                v: 1
            })
    pipe.execute()
    stopwatch.stop()
    print("createDate:", str(stopwatch))  # 5.27s


def countList_V1():
    '''
    统计 500 个 Sorted List
    '''
    watch = Stopwatch()
    watch.start()
    result = {}
    for x in range(0, 500):
        name = getProjectName(x)
        c = client.zcount(name, 0, 100)
        result[name] = c
    watch.stop()
    print("countList_V1", str(watch))   # 1.42s


def countList_V2_with_pipeline():
    '''
    统计 500 个 Sorted List，观察速度
    '''
    stopwatch = Stopwatch()
    stopwatch.start()
    result = {}
    pipe = client.pipeline()
    for x in range(0, 500):
        name = getProjectName(x)
        c = pipe.zcount(name, 0, 100)

    # 执行，并批量获取查询结构
    rr = pipe.execute()
    for x, v in zip(range(0, 500), rr):
        result[getProjectName(x)] = v

    stopwatch.stop()
    print("countList_V2_with_pipeline:", str(stopwatch))  # 75ms


def getProjectName(x):
    return "project_" + str(x)


if __name__ == "__main__":
    createData()
    countList_V1()
    countList_V2_with_pipeline()
    client.flushdb()
