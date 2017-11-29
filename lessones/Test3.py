#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys
print("====20. 递归函数 ====")

print("阶乘计算----")
def fact(n=1):
    if n==1:
        return 1
    return n*fact(n-1)

print("100的阶乘：",fact(100))

# print(len("93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000"))



def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1,2)
f1(1,2,c=12)
f1(1,2,'a','b')
f1(1,2,'a','b',ad='hello')
f1(1,2,'a','b',ad='hello',bc='world')
f2(1,2,d='命名关键字参数传参',x='关键字参数传参')
tup =(1,2,3,4,5)
kw={'d':99,'x':"$%"}
f1(*tup,**kw)
tu=(1,2,3)#如果tuple内容为1，2，3，4，5，则不会被正常调用
f2(*tu,**kw)



#尾递归优化

def factUp(n):
    return fact_update(n,1)

def fact_update(n,result):
    if n==1:
        return result
    return fact_update(n-1,n*result)

# print(factUp(6))
print("\n\n\n")
print("21 切片")
#对这种经常取指定索引范围的操作，用循环十分繁琐，因此， Python提
# 供了切片（ Slice）操作符，能大大简化这种操作。
print("对这种经常取指定索引范围的操作，用循环十分繁琐，因此， Python提供了切片（ Slice）操作符，能大大简化这种操作。")

L = ["1","2","3","4"]
#取前三个元素
print("循环取前三个元素")
for i in range(3):
    print(L[i])

print("切片方式获取前三个元素 L[0:3]：",L[0:3])
#如果第一个索引为0，还可以省略
print("省略索引0的切片 L[:3]：",L[:3])
print("从1开始获取数据，切片 L[1:3]：",L[1:3])
print("获取倒数第一个数据 L[-1] = ",L[-1])
print("倒数切片数据获取 L[-3:] = ",L[-3:])
print("倒数切片数据获取 L[-2:-1] = ",L[-2:-1])

L = list(range(100))

print("0-99的数列：L= ",L)
print("前10个数：",L[:10])
print("前10个数，每隔两个取一个 L[:10:2] = ",L[:10:2])
print("所有数，每5个取一个 L[::5] = ",L[::5])
print("list直接复制 L[:] = ",L[:])

# tuple 也是一种 list，唯一区别是 tuple 不可变。因此， tuple 也可以用切
# 片操作，只是操作的结果仍是 tuple

print("tuple切片结果 ： ",(0,1,2,3,4,5)[:3])
print("字符串切片：",'hello,python'[:8])

# 有了切片操作，很多地方循环就不再需要了。 Python 的切片非常灵活，
# 一行代码就可以实现很多行循环才能完成的操作。

print("\n\n\n 5-2 迭代")
# 如果给定一个 list 或 tuple，我们可以通过 for 循环来遍历这个 list 或
# tuple，这种遍历我们称为迭代（ Iteration）。
# Python 的 for 循环抽象程度要高于 Java 的 for 循环，因为
# Python 的 for 循环不仅可以用在 list 或 tuple 上，还可以作用在其他可迭
# 代对象上。

print("dict对象的迭代")
d = {'a': 1, 'b': 2, 'c': 3,'c':6}
# for dic in range(10):
#    d[dic] = str(dic)+"a"

for key in d:
    print(key ,"-",d[key])


for value in d.values():
     print("dict value:",value)

for k,v in d.items():
    print(k,v)
# dict 的存储不是按照 list 的方式顺序排列，所以，迭代出的结果顺
# 序很可能不一样。

for str1 in 'hello,string':
    print(str1)

# 最后一个小问题，如果要对 list 实现类似 Java 那样的下标循环怎么办？
# Python 内置的 enumerate 函数可以把一个 list 变成索引-元素对，这样就
# 可以在 for 循环中同时迭代索引和元素本身：
li = ['a','b','c','d']
for i,value in enumerate(li):
    print(i,value)

print("两个值输出：")
tuple_list = [(1,1),(2,3),(3,5)]
for k,v in tuple_list:
    print(k,v)

print("23 - 列表生成式")
print("小结：运用列表生成式，可以快速生成 list，可以通过一个 list 推导出另一个 list， 而代码却十分简洁。")
print(list(range(1,10)))
print(list(range(1,10,2)))

L =[];
for x in range(1,11):
    L.append(x*x)

print("L=",L)
#列表生成式
La = [m*m for m in range(1,11)]
print("La =",La)
#取偶数平方
Lb = [m*m for m in range(1,11) if m%2==0]
print("Lb = ",Lb)

#for嵌套
Lc = [m + n for m in 'ABC' for n in 'XYZ']
print("Lc = ",Lc)


print("导入os系统包")

Ld = [d for d in os.listdir(".")]
print("Ld =",Ld)

d = {'x': 'A', 'y': 'B', 'z': 'C' }
Le = ['k='+k+',v='+v for k,v in d.items()]
print("dict类型key和value获取：Le=",Le)

L = ['Hello', 'World', 'IBM', 'Apple']

print([alpha.lower() for alpha in L])

# 不可使用关键字定义变量，也不能用变量类型定义变量
#练习

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [result for result in L1 if isinstance(result,str)]
print("输出字符串类型  L2 = ",L2)

#练习延伸
B = 'a', 'v'
C = 'a string'

re = isinstance(B, tuple)
print("tuple类型判断：",re)
# print(isinstance(C, basestring))
#小结
# 运用列表生成式，可以快速生成 list，可以通过一个 list 推导出另一个 list，
# 而代码却十分简洁。

#TODO
LArray = [d for d in range(3) if d>0]
print("5-4  生成器")
Lgenerator = (d*d for d in range(10))
print("Lcreate = ",Lgenerator)
print("next(Lgenerator)输出方式：",next(Lgenerator),next(Lgenerator),next(Lgenerator))

for Lgen in Lgenerator:
    print(Lgen)


def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n+=1

for fi in fib(6):
    print("生成器输出斐波那契级数：",fi)

# fi_1 = fib(5)
# print("while循环输出斐波那契：")
# while True:
#     try:
#         print (next(fi_1), end="-")
#     except :
#         sys.exit()#执行此部分，则下面的内容都会停止执行。

# 这里，最难理解的就是 generator 和函数的执行流程不一样。函数是顺
# 序执行，遇到 return 语句或者最后一行函数语句就返回。而变成
# generator 的函数，在每次调用 next()的时候执行，遇到 yield 语句返回，
# 再次执行时从上次返回的 yield 语句处继续执行。

fi1 = fib(7)


while True:
    try:
        print(next(fi1))
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


#练习
#0 [1]
#1 [1,1]
#(1-1[0],1-1[0])

#2 [1,2,1]
#(2-1[0] ,2-1[0] + 2-1[1], 2-1[1])

#3 [1,3,3,1]
#(3-1[0],3-1[0] + 3-1[1], 3-1[1] + 3-1[2] , 3-1[2])

#4 [1,4,6,4,1]
#5 [1,5,10,10,5,1]
#6 [1,6,15,20,15,6,1]

print("杨辉三角")

def triangles(ma):
    ltri = [1]
    n=0
    while n<ma:
        yield ltri
        ltri.append(0)
        ltri = [ltri[i-1]+ltri[i] for i in range(len(ltri))]
        n+=1



for fo in triangles(5):
    print(fo)


def tri(n):
    Lt=[1]
    init=0
    while init<n:
        yield Lt
        # print(Lt)
        Lt.append(0)
        Lt = [Lt[i-1]+Lt[i] for i in range(len(Lt))]
        init+=1
print("自定义杨辉")
for tr in tri(1):
    print(tr)


print("5-5 迭代器")

print("这些可以直接作用于 for 循环的对象统称为可迭代对象： Iterable。(!= Iterator)")

from collections import Iterable
print("list是否可迭代：",isinstance([],Iterable))
print("dict是否可迭代：",isinstance({},Iterable))
print("str是否可迭代：",isinstance('abc',Iterable))
print("tuple是否可迭代：",isinstance((),Iterable))
print("列表生成式是否可迭代：",isinstance((x for x in range(3)),Iterable))
print("数字是否可迭代：",isinstance(100,Iterable))

print("可以被 next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。(!=Iterable)")

from collections import Iterator
print("list是否为迭代器：",isinstance([],Iterator))
print("dict是否为迭代器：",isinstance({},Iterator))
print("str是否为迭代器：",isinstance('abc',Iterator))
print("tuple是否为迭代器：",isinstance((),Iterator))
print("列表生成式是否为迭代器：",isinstance((x for x in range(3)),Iterator))
print("数字是否为迭代器：",isinstance(100,Iterator))

print("生成器都是 Iterator 对象，但 list、 dict、 str 虽然是 Iterable，却不是Iterator。")
print("把 list、 dict、 str 等 Iterable 变成 Iterator 可以使用 iter()函数")

print("list使用iter()函数转化后，是否为迭代器：",isinstance(iter([]),Iterator))
print("dict使用iter()函数转化后，是否为迭代器：",isinstance(iter({}),Iterator))
print("str使用iter()函数转化后，是否为迭代器：",isinstance(iter('abc'),Iterator))
print("tuple使用iter()函数转化后，是否为迭代器：",isinstance(iter(()),Iterator))
# 你可能会问，为什么 list、 dict、 str 等数据类型不是 Iterator？
# 这是因为 Python 的 Iterator 对象表示的是一个数据流， Iterator 对象可
# 以被 next()函数调用并不断返回下一个数据，直到没有数据时抛出
# StopIteration 错误。可以把这个数据流看做是一个有序序列，但我们却
# 不能提前知道序列的长度，只能不断通过 next()函数实现按需计算下一
# 个数据，所以 Iterator 的计算是惰性的，只有在需要返回下一个数据时
# 它才会计算。
# Iterator 甚至可以表示一个无限大的数据流，例如全体自然数。而使用
# list 是永远不可能存储全体自然数的。

print("6 - 函数式编程")
print("6 -1 高阶函数")

print("abs输出：",abs)
print("abs(-10)=",abs(-10))
print("abs(-10)是函数调用，而 abs 是函数本身。")
f = abs

print("f=abc[绝对值函数],则f(-3) = ",f(-3))
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

def add(x,y,f):
    return f(x)+f(y)
ad = add(-4,-5,abs)
print(ad)

print("6-2 map/reduce")

def f(x):
    return x*x;

res = map(f,[1,3,5])
print(list(res))

strput = map(str,[1,2,3,4,5])
print("数字list转换为str-list：",list(strput))


print("reduce需要进行导入操作")
from functools import reduce
print("reduce计算list求和")
def caladd(x,y):
    return x*y
red = reduce(caladd,[1,2,3,5,6])
print(red)

print("reduce将list按序组成数字，如[1,3,5,7,9]=>13579")

def orderNum(x,y=0):
    return x*10+y
on =[5,4,3,2,1]
num = reduce(orderNum,on)
print(num)
print("sum函数对数字list求和",sum(on))
# print("sum函数对数字list求和",sum(['1','2']))#会抛异常
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
'7': 7, '8': 8, '9': 9,'.':'.'}[s]

str_int = reduce(orderNum,map(char2num,'13567'))
print("字符串转换为int类型：",str_int)

print("使用lambda表达式处理")

def str2int(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))

print("使用lambda表达式：",str2int('123789'))

#练习
print("map/reduce练习题")
def normalize(name):

    return name.capitalize()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize,L1))

print(L2)


def prod(L):
   return reduce(lambda x,y:x*y,L)

print("reduce求积练习：",prod([3,5,7,9]))


def str2float_1(s):
    mapNum=[map(str2int,mapNum) for mapNum in s.split('.')]
    intNum = reduce(lambda x, y: x * 10 + y, mapNum[0])
    # pointNum = reduce(lambda x, y: x * 10 + y, mapNum[1])
    # listLen = list(mapNum[1])
    powNum = pow(10,-len(list(mapNum[1])))
    return intNum+powNum


def str2float(s):
    mapNum=[map(str2int,mapNum) for mapNum in s.split('.')]
    intNum = reduce(lambda x, y: x * 10 + y, mapNum[0])
    pointNum = reduce(lambda x,y:x*10+y,mapNum[1])

    powNum = pow(10,-len(str(pointNum)))
    return intNum+pointNum*powNum

print("str2float_1函数结果：",str2float_1('12.679'))
print("str2float函数结果：",str2float('12.679'))
print("int函数结果：",float('12.345'))

