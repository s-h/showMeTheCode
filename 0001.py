#!/usr/bin/env python
#coding:utf-8
import random
Activations = []

def makeRandomLower():
    randomLower = chr(random.randint(97,122))
    return randomLower

def makeRandomCapital():
    randomCapital = chr(random.randint(65,90))
    return randomCapital

def makeRandomNumber():
    randomNumber = random.randint(0,9)
    return randomNumber

def getRandomCode():
    pass

def strChoose():
    choose = random.randint(1,3)
    if choose == 1:
        return makeRandomLower()
    elif choose == 2:
        return makeRandomCapital()
    else:
        return makeRandomNumber()

def makeActivation(actLen):
    activation = ""
    for i in range(0,actLen):
        activation = str(strChoose()) + activation

#    activation = "1111111111"
    if activation not in Activations:
        return activation
    else:
        makeActivation(actLen)
def makeActivationList(actNumber,actLen):
    n = 0
    while n < actNumber:
        Activations.append(makeActivation(actLen))
        n += 1

makeActivationList(100,10)
print Activations
'''
有时候思路更加重要，看了其他人的写法，根本没有必要每个字符随机生成。
将0~9,a~z,A~Z保存到list中，用random.sample从list中取固定位数 
def gen_code(length=8):
    code_list = []
    for i in range(10):
        code_list.append(str(i))
    for i in range(65,91):
        code_list.append(chr(i))
    for i in range(97,123):
        code_list.append(chr(i))

    myslice = random.sample(code_list, lenght)
    veri_code = ''.join(myslice)
    return veri_code
'''
