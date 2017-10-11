#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


def outputLen(describe, input):
    print(describe + str(len(input)));


def outputStr(describe, input):
    print(describe + "   " + str(input));


print("17 - 定义函数")

print("十六进制10的输出结果：%x" % (10))
print("-------------")

# 空函数
def kong():
    pass


# pass 语句什么都不做，那有什么用？实际上 pass 可以用来作为占位符，
# 比如现在还没想好怎么写函数的代码，就可以先放一个 pass，让代码能
# 运行起来。
# pass 还可以用在其他语句里，比如：
# if age >= 18:
# pass
# 缺少了 pass，代码运行就会有语法错误。

def num(input):
    if not isinstance(input, (int, float)):
        raise TypeError('错误的类型')
    if input > 0:
        return input
    else:
        return -input


value = num(2)
print(value)
# value = num('abs')
# print(value)

print("多个值的返回函数")


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
# 但其实这只是一种假象， Python 函数返回的仍然是单一值：
print('但其实这只是一种假象， Python 函数返回的仍然是单一值：')
r = move(100, 100, 60, math.pi / 6)
outputStr("实际返回值：", r)
# 原来返回值是一个 tuple！但是，在语法上，返回一个 tuple 可以省略括
# 号，而多个变量可以同时接收一个 tuple，按位置赋给对应的值，所以，
# Python 的函数返回多值其实就是返回一个 tuple，但写起来更方便。

print(math.sqrt(2))


# 练习，求解一元二次方程的解

def quadratic(a, b, c):
    nx = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    ny = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return nx, ny


print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))

print("18 - 函数的参数")


def power(x, n=2):#只传一个参数时，默认计算平方值，传两个参数，则代表计算指定次方
    s = 1
    while n>0:
        n-=1
        s*=x
    return s
print(power(3))
# #一是必选参数在前，默认参数在后，否则 Python 的解释器会报错（思
# 考一下为什么默认参数不能放在必选参数前面）；
# ######二是如何设置默认参数。####
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。
# 变化小的参数就可以作为默认参数。
# 使用默认参数有什么好处？最大的好处是能降低调用函数的难度。



def add_end(L=[]):
    L.append('END')
    return L

print("for 循环打印自定义函数 add_end 默认值结果,结果值一次比一次多")
for i in range(3):
    print(add_end())

# 原因解释如下：
# Python 函数在定义的时候，默认参数 L 的值就被计算出来了，即[]，因
# 为默认参数 L 也是一个变量，它指向对象[]，每次调用该函数，如果改
# 变了 L 的内容，则下次调用时，默认参数的内容就变了，不再是函数定
# 义时的[]了。

# 要修改上面的例子，我们可以用 None 这个不变对象来实现：
def add_end_handle(L=None):
    if L is None:
        L = []
        L.append('END')
    return L
print("循环五次结果如下：已经正确")
for i in range(5):
    print(add_end_handle())

print("range(1,2,1) 循环输出，查看结果：")
for i in range(1,2,1):#类似于Java版for(int i=1;i<2;i++)
    print(i)

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('jiayou',3)

print("可变参数设置方式")

#计算a2 + b2 +c2+...

def calc(numbers):
    sum = 0
    for i in numbers:
        sum=sum+i*i
    outputStr("入参各个参数的平方之和为：",sum)


calc((1,2,3))

print("修改入参格式为：*numbers")

def calc2(*numbers):
    sum = 0
    for i in numbers:
        sum+=i*i
    outputStr("入参格式修改后计算结果不变：",sum)

calc2(1,2,3)
calc2()
print("如果已定义了list或者tuple参数，传参时需要添加星号，便可作为可变参数传参")
tu = (1,3,5,7)
calc2(*tu)

# 定义可变参数和定义一个 list 或 tuple 参数相比，仅仅在参数前面加了一
# 个*号。在函数内部，参数 numbers 接收到的是一个 tuple，因此，函数
# 代码完全不变。但是，调用该函数时，可以传入任意个参数，包括 0 个
# 参数
def person(name,age,**value):
    print('name:',name,'age:',age)

kw = {'name':'John','age':18}
print("====关键字函数定义============")
person(**kw)
person('Pola',20)

print("====命名关键字参数====")
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。
# 至于到底传入了哪些，就需要在函数内部通过 kw 检查。
def person(name,age,**kw):
    if 'city' in kw:
        pass
    elif 'job' in kw:
        pass
    else:
        print('name:',name,'age:',age,'other:',kw)
# 但是调用者仍可以传入不受限制的关键字参数：

person('Jack',24,city='BeiJing',job='IT工作者')
person('Jack',24,addr='朝阳区')
# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接
# 收 city 和 job 作为关键字参数。这种方式定义的函数如下
print('====限制关键字参数的名字=====')
def person_param_define(name, age, *, city, job):
    print(name, age, city, job)

print("method person_param_define------")
person_param_define('Jack', 24, city='Beijing', job='Engineer')
# person_param_define('Jack', 24, city='Beijing')

# 命名关键字参数可以有缺省值，从而简化调用：
print("method person_param_default------")
def person_param_default(name, age, *, city='Hangzhou', job):
    print(name, age, city, job)

person_param_default('Kaer', 20, job='IT ')




