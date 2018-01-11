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


print("primes:", list(primes(12)))
print("_odd_iter:", list(_odd_iter(12)))

print(
    reduce(
        lambda l, y:  # 递减的操作函数
        not 0 in map(lambda x: y % x, l) and l + [y] or l,  # l是一个列表[], 结果l中后加入的数不能被前数整除，被整除则不添加后数
        [2, 3, 4, 5, 6, 7],
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
        res = i + res
    return res


def is_palindrome(n):
    if len(str(n)) < 2:
        return False
    return reverse(n) == str(n)


output = filter(is_palindrome, range(1, 1000))
print(list(output))

print("6-4 sorted")

# 默认排序操作
print(sorted([3, -12, 1, 0, 12, 45]))

# 自定义排序操作
# sorted()函数也是一个高阶函数，它还可以接收一个 key 函数来实现自定义的排序，例如按绝对值大小排序
print(sorted([3, -12, 1, 0, 12, 45], key=abs))

# 对字母排序，按照大小写的ASCII码进行排序
print(sorted(['Credit', 'abs', 'Adam', 'baby']))
print("不区分大小写进行排序")
print(sorted(['Credit', 'abs', 'Adam', 'baby'], key=str.lower))
print("反向排序")
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

print("练习")
L = [('Bob', 75), ('adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(n):
    return tuple(n)[0].lower()


print("按照名字不区分大小写排序：", sorted(L, key=by_name))


def by_score(n):
    return tuple(n)[1]


print("按照分数排序：", sorted(L, key=by_score))

print("6-5 返回函数")


def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


su = lazy_sum(1, 3, 5, 7, 9)
print("返回函数信息：", su)
print("调用返回函数，计算求和结果：", su())
# 请再注意一点，当我们调用 lazy_sum()时，每次调用都会返回一个新的
# 函数，即使传入相同的参数
su_2 = lazy_sum(1, 3, 5, 7, 9)
print(su == su_2)
# 我们在函数 lazy_sum 中又定义了函数 sum，并且，内部
# 函数 sum 可以引用外部函数 lazy_sum 的参数和局部变量，当 lazy_sum 返
# 回函数 sum 时，相关参数和变量都保存在返回的函数中，这种称为“闭包
# （ Closure） ”的程序结构拥有极大的威力。


print("闭包")


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print("输出f1,f2,f3函数调用结果：", f1(), f2(), f3())


# 你可能认为调用 f1()， f2()和 f3()结果应该是 1， 4， 9，但实际结果是：9 9 9
# 全部都是 9！原因就在于返回的函数引用了变量 i，但它并非立刻执行。
# 等到 3 个函数都返回时，它们所引用的变量 i 已经变成了 3，因此最终
# 结果为 9。

# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量， 或者后
# 续会发生变化的变量。

# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的
# 参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到
# 函数参数的值不变：
def count_1():
    def rs(n):
        def g():
            return n * n

        return g

    fs = []
    for i in range(1, 4):
        fs.append(rs(i))

    return fs


g1, g2, g3 = count_1()
print("输出g1,g2,g3函数调用结果：", g1(), g2(), g3())


# 使用lambda进行压缩
def count_2():
    def rs(n):
        return lambda: n * n

    fs = []
    for i in range(1, 4):
        fs.append(rs(i))

    return fs


gg1, gg2, gg3 = count_1()
print("输出gg1,gg2,gg3函数调用结果：", gg1(), gg2(), gg3())

# 小结
# 1. 一个函数可以返回一个计算结果，也可以返回一个函数。
# 2. 返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。

print("6-6 匿名函数")

# 在 Python 中，对匿名函数提供了有限支持。还是以 map()函数为例，计
# 算 f(x)=x2 时，除了定义一个 f(x)的函数外，还可以直接传入匿名函数：
# list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# 关键字 lambda 表示匿名函数，冒号前面的 x 表示函数参数。

print(list(map(lambda x: x * x, [1, 2, 3, 4, 5])))
# 注意：匿名函数有个限制，就是只能有一个表达式，不用写 return，返回值就
# 是该表达式的结果。

anonymity = lambda x:x*x

print("匿名函数变量求值：",anonymity(12))
print(anonymity.__name__)
# 也可以把匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y
#小结：
# Python 对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数。

print("6-7 装饰器")
# 函数对象有一个__name__属性，可以拿到函数的名字：
print("获取 6-5 章节的函数count_2名称：",count_2.__name__)
# 在函数调用前后自动
# 打印日志，但又不希望修改 now()函数的定义，这种在代码运行期间动
# 态增加功能的方式，称之为“装饰器”（ Decorator）。

def log(func):
    def wrapper(*args,**kw):
        print('call %s():'%func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2018-1-7 10:58')

now()

def logString(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s 方法 %s() 被调用。%s'%(text,func.__name__,args))
            return func(*args,**kw)
        return wrapper
    return decorator
#这个三层嵌套的decorator用法如下：
@logString('定义日志输出的固定内容：')
def now():
    print('2018-1-7 17:04')

now()
@logString('函数之后进行日志输出：')
def define(input):
    print('2018-1-10 16:55,输入信息为：',input)

define('你好，python。我一直在加油')

