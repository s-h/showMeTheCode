#!/usr/bin/env python
#coding:utf-8
import random,MySQLdb

# mysql setting
conn = MySQLdb.connect(
        host = '127.0.0.1',
        port = 3306,
        user = 'user',
        passwd = 'passwd',
        db = 'python',
        charset = 'utf8'
        )

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
    cur = conn.cursor()
    for act in activations:
        cur.execute('insert into activations values(NULL,"%s")' % (act))
    cur.close()
    conn.commit()
    conn.close()

writeAct(makActivation(100))



