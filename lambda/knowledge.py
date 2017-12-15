#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def _not_divisible(n):
    bk = lambda x: x % n > 0
    return bk

print(_not_divisible(4))

lam = lambda x,y:x*y
print(lam(4,5))
# 2. 定义筛选函数
def _not_divisible(n):
    bk = lambda x: x % n > 0
    return bk
numlist = filter(_not_divisible(n), [2,3,4,5,6])
