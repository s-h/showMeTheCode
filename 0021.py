#!/usr/bin/env python
#coding: utf-8
'''
第 0021 题： 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密
'''
import hmac,hashlib
import random

def createSalt():
    strings = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-'
    salt = []
    for i in range(10):
        salt.append(random.choice(strings))
    salt = ''.join(salt)

    return salt
        

def createHash(salt,password):
    h = hmac.HMAC(salt.encode('utf-8'), password.encode('utf-8'),hashlib.sha256)
    return h.hexdigest()


salt = createSalt()   
password = 'wobugaosuni'
print createHash(salt,password)
