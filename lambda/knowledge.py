#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce
#lambda语句中，冒号前是参数，可以有多个，用逗号隔开，冒号右边的返回值。lambda语句构建的其实是一个函数对象。
def _not_divisible(n):
    bk = lambda x: x % n > 0
    return bk

print(_not_divisible(4))

lam = lambda x,y:x*y
print(lam(4,5))

print (lambda:'begin')   #<function <lambda> at 0x00B00A30>
# 2、无参数
# 如果没有参数，则lambda冒号前面就没有，如以上例子。

# 3、有参数
def add(x,y):return x+y
add2 = lambda x,y:x+y
print (add2(1,2))     #3
print (reduce(add2,(1,2,3,4)))     #10

def sum(x,y=10):return x+y
sum2 = lambda x,y=10:x+y
print (sum2(1))       #11
print (sum2(1,100))   #101