#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
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
d = {'a': 1, 'b': 2, 'c': 3}
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
























