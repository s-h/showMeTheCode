#!/usr/bin/env python
#coding: utf-8
'''
第 0003 题： 将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
'''
import random
import redis

def makActivation(actNumber):
    radomStrNumber = [ str(x) for x in range(10) ]
    radomStrLower = [ chr(x) for x in range(65,91) ]
    radomStrCapital = [ chr(x) for x in range(97,123) ]
    radomStr =  radomStrNumber + radomStrLower + radomStrCapital
    activations = []
    n = 0
    while n < 100:
        activation = random.sample(radomStr, 8)
        activation = ''.join(activation)            #单个激活码
        if activation not in activations:           #防止重复
            activations.append(activation)
        else:
            continue
        n += 1

    return activations

def writeAct(activations):
    r = redis.Redis(host='127.0.0.1',port=6379,db=0)
    n = 1
    for act in activations:
        r.set(n,act)
        n += 1


writeAct(makActivation(100))

