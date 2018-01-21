#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print("1. f()函数中第一个a为什么会报错？")
# 告诉你原因,第二个函数,内部有变量a的定义,在print a时,
# 是要找local的变量名,发现local变量名里有a,但是还没有
# 提前定义,就报错了
#*知识点*：python变量范围会先从函数中进行查找，如果函数中有定义，则
# 使用函数内部的参数变量进行输出，否则才会查找全局变量
#*解决方案*:
# 在f()函数中，添加global a，然后输出print(a)即可
# print(a)
a = 1
def g():
    print(a)

def f():
    # global a
    # print(a)
    a = 2
    print(a)

g()
f()
