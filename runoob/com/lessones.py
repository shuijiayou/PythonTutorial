#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# http://www.runoob.com/python3/python3-tutorial.html

import sys


# http://www.runoob.com/python3/python3-iterator-generator.html
# Python3 迭代器与生成器

list=[1,2,3,4]
it = iter(list)# 创建迭代器对象
print(next(it),"====")

def forprint(it):
    print("for循环输出：")
    for i in it:
        print(i, end='+')
    print()

def whileprint(it):
    print("while 循环输出：")
    while True:
        try:
            print(next(it))
        except StopIteration:
            sys.exit()

forprint(it)
# whileprint(iter(list))
#
# def fibonacci(n):# 生成器函数 - 斐波那契
#     a,b,i = 0,1,0
#     while True:
#         if i>n:
#             return
#         yield a
#         a,b = b,a+b
#         i+=1
# result = fibonacci(13)# result 是一个迭代器，由生成器返回生成
# print(result)
# while True:
#     try:
#         print(next(result),end=' ')
#     except StopIteration:
#         sys.exit()

def fibonacci_2(n,w=0): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        # print('%d,%d' % (a,b))
        counter += 1
f = fibonacci_2(10,0) # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print (next(f), end="-")
    except :
        sys.exit()

