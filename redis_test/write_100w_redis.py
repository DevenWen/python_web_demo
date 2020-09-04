#!/usr/bin/python3
# -*- coding:UTF-8 -*-
'''
 @AUTHOR: kangqiang.w :)
 @FILE: ~/learn/python_web_demo/redis_test/write_100w_redis.py
 @DATE: 2020/09/04 周五
 @TIME: 12:04:46

# DESCRIPTION:

向 Redis 写入 100w 个数据。分两个实验：
1. 普通写入100w个 KV 值
2. 利用 hash 对 100w 个值进行分级处理
3. 调整参数，让 hash 数据结构始终处于 ziplist

'''

import redis
import datetime

client = redis.StrictRedis(host="redis.qpm.com", port=6379, db=0)


def write100wkv_with_pipline():
    '''
    begin write 100w
    used_memory_human:844.65K
    used_memory_human:69.85M
    end write 100w, using: 72380608
    '''
    print("begin write 100w")
    pip = client.pipeline(transaction=False)

    before = getRedisUsedMemory()
    for k in range(0, 1000000):
        pip.set(k, 'v' + str(k))
    pip.execute()
    after = getRedisUsedMemory()
    print("end write 100w, using: " + str(after - before))

def write100wkv_with_pipline_hash():
    '''
    begin write 100w in hashway
    used_memory_human:865.74K
    used_memory_human:53.82M
    end write 100w, using: 55544192
    '''
    print("begin write 100w in hashway")
    pip = client.pipeline(transaction=False)

    before = getRedisUsedMemory()
    for k in range(0, 1000000):
        pip.hset(int(k/1000), k % 1000, 'v' + str(k))
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
    write100wkv_with_pipline_hash()
    # getRedisUsedMemory()
