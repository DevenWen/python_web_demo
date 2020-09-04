#!/usr/bin/python3
# -*- coding:UTF-8 -*-
'''
 @AUTHOR: kangqiang.w :)
 @FILE: ~/learn/python_web_demo/redis_test/write_100w_redis.py
 @DATE: 2020/09/04 周五
 @TIME: 12:04:46

# DESCRIPTION:

向 Redis 写入 100w 个数据

'''

import redis
import datetime

client = redis.StrictRedis(host="redis.qpm.com", port=16379, db=0)


def writekvdemo():
    client.set("key:demo", "value:demo")
    result = client.get("key:demo")
    print(result)


def write5wkv():
    print("begin write 100w")
    before = getRedisUsedMemory()
    for k in range(0, 50000):
        client.set(k, 'v' + str(k))
    after = getRedisUsedMemory()
    print("end write 100w, using: " + str(after - before))


def write5wkv_with_pipline():
    print("begin write 100w")
    pip = client.pipeline(transaction=False)

    before = getRedisUsedMemory()
    for k in range(0, 1000000):
        pip.set(k, 'v' + str(k))
    pip.execute()
    after = getRedisUsedMemory()
    print("end write 100w, using: " + str(after - before))


def getRedisUsedMemory():
    info = client.info('memory')
    print("used_memory_human:" + info.get('used_memory_human'))
    return info.get('used_memory')


if __name__ == "__main__":
    # writekvdemo()
    # write5wkv()
    write5wkv_with_pipline()
    # getRedisUsedMemory()
