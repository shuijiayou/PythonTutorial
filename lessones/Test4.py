#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce
print("6 - 函数式编程")
print("6 -1 高阶函数")

print("abs输出：", abs)
print("abs(-10)=", abs(-10))
print("abs(-10)是函数调用，而 abs 是函数本身。")
f = abs

print("f=abc[绝对值函数],则f(-3) = ", f(-3))
print("成功！说明变量 f 现在已经指向了 abs 函数本身。直接调用 abs()函数和调用变量 f()完全相同。")
print("函数名也是变量")

# abs=10
# try:
#     print("把 abs 指向 10 后:",abs(-6))
# except Exception as e:
#     print("异常",e)

print("把 abs 指向 10 后，就无法通过 abs(-10)调用该函数了！因为 abs 这个变量已经不指向求绝对值函数而是指向一个整数 10！")

# 当然实际代码绝对不能这么写，这里是为了说明函数名也是变量。要恢
# 复 abs 函数，请重启 Python 交互环境。
# 注：由于 abs 函数实际上是定义在__builtin__模块中的，所以要让修改
# abs 变量的指向在其它模块也生效，要用__builtin__.abs = 10。


print("高阶函数定义：一个函数可以接收另一个函数作为参数，这种函数就称之为高阶函数。")


# 一个最简单的高阶函数：

def add(x, y, f):
    return f(x) + f(y)


ad = add(-4, -5, abs)
print(ad)

print("6-2 map/reduce")


def f(x):
    return x * x;


res = map(f, [1, 3, 5])
print(list(res))

strput = map(str, [1, 2, 3, 4, 5])
print("数字list转换为str-list：", list(strput))

print("reduce需要进行导入操作")


print("reduce计算list求和")


def caladd(x, y):
    return x * y


red = reduce(caladd, [1, 2, 3, 5, 6])
print(red)

print("reduce将list按序组成数字，如[1,3,5,7,9]=>13579")


def orderNum(x, y=0):
    return x * 10 + y


on = [5, 4, 3, 2, 1]
num = reduce(orderNum, on)
print(num)
print("sum函数对数字list求和", sum(on))


# print("sum函数对数字list求和",sum(['1','2']))#会抛异常
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
            '7': 7, '8': 8, '9': 9, '.': '.'}[s]


str_int = reduce(orderNum, map(char2num, '13567'))
print("字符串转换为int类型：", str_int)

print("使用lambda表达式处理")


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print("使用lambda表达式：", str2int('123789'))

# 练习
print("map/reduce练习题")


def normalize(name):
    return name.capitalize()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))

print(L2)


def prod(L):
    return reduce(lambda x, y: x * y, L)


print("reduce求积练习：", prod([3, 5, 7, 9]))


# TODO 该函数注释部分解开之后返回结果异常，不懂。
def str2float_1(s):
    mapNum = [map(str2int, mapNum) for mapNum in s.split('.')]
    intNum = reduce(lambda x, y: x * 10 + y, mapNum[0])
    # pointNum = reduce(lambda x, y: x * 10 + y, mapNum[1])
    # listLen = list(mapNum[1])
    powNum = pow(10, -len(list(mapNum[1])))
    return intNum + powNum


def str2float(s):
    mapNum = [map(str2int, mapNum) for mapNum in s.split('.')]
    intNum = reduce(lambda x, y: x * 10 + y, mapNum[0])
    pointNum = reduce(lambda x, y: x * 10 + y, mapNum[1])

    powNum = pow(10, -len(str(pointNum)))
    return intNum + pointNum * powNum


print("str2float_1函数结果：", str2float_1('12.679'))
print("str2float函数结果：", str2float('12.679'))
print("int函数结果：", float('12.345'))

print("6-3 filter")

# 和 map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是 True 还
# 是 False 决定保留还是丢弃该元素。
def is_odd(s):
    return s % 2 == 1


isodd = filter(is_odd, [1, 2, 3, 4, 5, 6, 7])
print(list(isodd))
print("strip函数：只要边（开头或结尾）上的字符在删除序列内，就删除掉。")
print("删除空白符函数strip：", "原有字符长度 aa b-", len(' aa b'), 'strip之后：',
      len(' aa b'.strip()))  # 默认删除空白符（包括'\n', '\r',  '\t',  ' ')


#  返回true or false
def not_empty(s):
    return s and s.strip()


filt = filter(not_empty, ['A', '', 'B', None, 'C', ' '])
print("删除序列中的空字符串：", list(filt))
# emp = ''
print("非空判断：", str('abc ' and 'abc '.strip()))

print("使用filter求素数")


# 计算素数的一个方法是埃氏筛法，
# 1. 定义生成器(奇数数列)
def _odd_iter(n):
    x = 3
    while x < n:
        yield x
        x += 2
    return x

# 2. 定义筛选函数
def _not_divisible(n):
    bk = lambda x: x % n > 0
    return bk

def primes(n):
    yield 2
    it = _odd_iter(n)  # 初始序列
    # print(list(it))
    while True:
        m = next(it)
        yield m
        it = filter(_not_divisible(m), it)  # 构造新序列

print("primes:",list(primes(12)))
print("_odd_iter:",list(_odd_iter(12)))




print(
    reduce(
        lambda l, y:#递减的操作函数
        not 0 in map(lambda x: y % x, l) and l + [y] or l,#l是一个列表[], 结果l中后加入的数不能被前数整除，被整除则不添加后数
        [2,3,4,5,6,7],
        # range(2, 120),#范围[2,12)
        []))

# 过程是:
# 测试到6， 就把6依次整除之前的l=[2,3,5] ，除2余0，就放弃6。l仍是[2,3,5]
# 测试到7， 就把7依次整除之前的l=[2,3,5] ，除2都不余0，加入6。l变成[2,3,5,7]
# 最后得到一个纯素数的列表[];

# 练习
# 回数是指从左向右读和从右向左读都是一样的数，例如 12321， 909。请
# 利用 filter()滤掉非回数：
print("练习：回数计算")
def reverse(n):
    res = ''
    m = str(n)
    for i in m:
        res=i+res
    return res

def is_palindrome(n):
    if len(str(n))<2:
        return False
    return reverse(n)==str(n)

output = filter(is_palindrome, range(1, 1000))
print(list(output))

print("6-4 sorted")

#默认排序操作
print(sorted([3,-12,1,0,12,45]))

#自定义排序操作
#sorted()函数也是一个高阶函数，它还可以接收一个 key 函数来实现自定义的排序，例如按绝对值大小排序
print(sorted([3,-12,1,0,12,45],key=abs))

def sortData(n):
    print(n+10)
    return abs(n+10)

print(sorted([3,-12,1,0,12,45],key=sortData))

#对字母排序，按照大小写的ASCII码进行排序
print(sorted(['Credit','abs','Adam','baby']))
print("不区分大小写进行排序")
print(sorted(['Credit','abs','Adam','baby'],key=str.lower))