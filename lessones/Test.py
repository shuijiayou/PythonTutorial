#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def outputLen(describe,input):
	 print(describe+str(len(input)));

def outputStr(describe,input):
	print(describe+"   "+str(input)) ;

a = -2
if a>=0:
	print(a)
else:
	print(-a)
#整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确 的(除法难道也是精确的?是的!)，而浮点数运算则可能会有四舍五 入的误差
print(1.23e5)
print(1.23e-5)
print(0.000012)

print(123);

# Python 允许用'''...'''的格式表示多行内容
print('''line1
... line2
... line3''')
print('''
line1
line2
line3''')
print(r'''hello world''' 
	  r'''next line''')
# 布尔值（请注意大小写）
print(True);
print(False);
print("4>5 is "+str((4>5)))

print("True or True -->"+str(True or True))
print("True and True -->"+str(True or True))
print("True and False -->"+str(True and False))
print("True or False -->"+str(True or False))
print("False or False -->"+str(False or False))
print("False and False -->"+str(False and False))
print("4>3 and 4>2 is "+str(4>3 and 4>2))
# not 运算是非运算，它是一个单目运算符，把 True 变成 False，False 变 成 True:
print("not 1<2 is "+str(not 1<2))

age = 17;
if age>=18:
	print('adult')
else:
	print("young")

# 空值是 Python 里一个特殊的值，用 None 表示。None 不能理解为 0，因 为 0 是有意义的，而 None 是一个特殊的空值。
print("None value is "+str(None))
print(None)
# 这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。

# 静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不 匹配，就会报错。
# 例如Java是静态语言，赋值语句如下(// 表示注释):
# int a = 123; // a 是整数类型变量
# a = "ABC"; // 错误:不能把字符串赋给整型变量
# 和静态语言相比，动态语言更灵活，就是这个原因。

variable = 10;
print(variable)
variable = 'string'
print("variable value is "+variable)


x = 'hello'
x = x+str(3);
#x = x+3 会报错
print(x)
# 在 Python 中，有两种除 法，一种除法是/:
# 计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数
print("正常除法 单斜线'/':"+str(14/3))
# 还有一种除法是//，称为地板除，两个整数的除法仍然是整数
print("地板除法 双斜线'//':"+str(14//3))
#取余数
print("取余数："+str(14%3))
# 无论整数做//除法还是取余数，结果永远是整数，所以，整数运算结果 永远是精确的。
#练习题
print(r'Hello,"python"')
print(r'''hello,
Lisa!''')
# 注意:Python 的整数没有大小限制，而某些语言的整数根据其存储长度 是有大小限制的，例如 Java 对 32 位整数的范围限制在 -2147483648-2147483647。
# Python 允许用'''...'''的格式表示多行内容
#问题1，在pccharm中，为何不需要 ...即可正常换行？而命令中会自动添加？程序中无需添加。还可使用r
# 问题2，多行字符串r如何应用？
# Python 的浮点数也没有大小限制，但是超出一定范围就直接表示为 inf (无限大)。
one = 11111111111111111111111111111111;
two = 22222222222222222222222222222222;
print(one+two)


# 10.对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('A'));
print(chr(65));
print('\u4e2d\u6587');
# Python 对 bytes 类型的数据用带 b 前缀的单引号或双引号表示
x = b'ABC'
print('ABC'.encode('ascii'))#b'ABC'
print(x.decode('ascii'))#ABC

# len()函数计算的是 str 的字符数，如果换成 bytes，len()函数就计算字 节数:
print(len('aaa'))
print(" 长度："+str(len("aaa".encode("UTF8"))))
print(" 长度："+str(len("中文".encode("UTF8"))))

print('utf8编码：'+str('中文'.encode('utf8')))#b'\xe4\xb8\xad\xe6\x96\x87'
print("gb2312编码："+str('中文'.encode('gb2312')))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf8'));
# 申明了 UTF-8 编码并不意味着你的.py 文件就是 UTF-8 编码的，必须并
# 且要确保文本编辑器正在使用 UTF-8 without BOM 编码

# 在 Python 中，采用的格式化方式和 C 语言是一致的，用%实现
# %d 整数
# %f 浮点数
# %s 字符串
# %x 十六进制整数
print('hello,%s'%('John'))
print('1+2 = %d'%(3))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
print('rate is %d %%'%98)

#练习
result = (85-72);
print('%.1f%%'%result)

# 11. 使用 list 和 tuple
# Python 内置的一种数据类型是列表:list。list 是一种有序的集合，可以 随时添加和删除其中的元素。
classmates = ['张三','李四','王五']
print('list 输出结果：'+str(classmates))
print('list 长度'+str(len(classmates)))
print('list 下标输出0：'+str(classmates[0]))
print('list 下标输出1：'+str(classmates[1]))
print('list 下标输出2：'+str(classmates[2]))
# 如果要取最后一个元素，除了计算索引位置外，还可以用-1 做索引，直 接获取最后一个元素
# 以此类推，可以获取倒数第 2 个、倒数第 3 个
print('list 下标输出 -1：'+str(classmates[-2]))
classmates.append('Adam data')
outputLen("list添加数据后的长度：",classmates)
outputStr("list添加数据后的数据展示：",classmates)
# 要删除指定位置的元素，用 pop(i)方法，其中 i 是索引位置:pop()默认删除末尾数据
print("删除末尾数据---"+str(classmates.pop()))
print("删除之后的结果数据---"+str(classmates))
# list 里面的元素的数据类型也可以不同
dataList = ['String',123,True]
# list 元素也可以是另一个 list
s = ['python', 'java', ['asp', 'php'], 'scheme']
# 另一种有序列表叫元组： tuple。tuple 和 list 非常类似，但是 tuple 一旦初始化就不能修改，比如同样是列出同学的名字

#tuple
students = ('Mike','Jack','John')
# 它也没有 append()， insert()这样
# 的方法。其他获取元素的方法和 list 是一样的，你可以正常地使用
# classmates[0]， classmates[-1]，但不能赋值成另外的元素。
outputLen("tuple 长度",students)
print(students[2])
# 不可变的 tuple 有什么意义？因为 tuple 不可变，所以代码更安全。如果
# 可能，能用 tuple 代替 list 就尽量用 tuple。

# tuple 的陷阱：当你定义一个 tuple 时，在定义的时候， tuple 的元素就必
# 须被确定下来，但是，要定义一个只有 1 个元素的 tuple，如果你这么定义
t = (1)
# 定义的不是 tuple，是 1 这个数！这是因为括号()既可以表示 tuple，又
# 可以表示数学公式中的小括号，这就产生了歧义，因此， Python 规定，
# 这种情况下，按小括号进行计算，计算结果自然是 1。所以，只有 1 个元素的 tuple 定义时必须加一个逗号,，来消除歧义：
t = (1,)
print(t)
# tuple所谓的“不变”是说， tuple 的每个元素，指向永远不变
tup = ('a','b',['A','B'])
outputStr("原始tuple数据:",tup)
tup[2][0] = 'X'
tup[2][1] ='Y'
outputStr("改变tuple中list之后的数据:",tup)
#练习
L = [
['Apple', 'Google', 'Microsoft'],
['Java', 'Python', 'Ruby', 'PHP'],
['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])
#小结：list 和 tuple 是 Python 内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们。

#12 条件判断
print('12. 条件判断')
age =12
if age>=18:
	print('your age is ',age)
	print('adult')
else:
	print('your age is ',age)
	print('teenager')

print('elif判断模式:')

if age>18:
	print("adult")
elif age>10:
	print('teenager')
else:
	print('kid')

# 只要 x 是非零数值、非空字符串、非空 list 等，就判断为 True，否则为False。
x=2
if x:
	print("True")
else:
	print('False')

# birth = input('birth: ')
# birth = input()
# 这是因为 input()返回的数据类型是 str， str 不能直接和整数比较，必
# 须先把 str 转换成整数。
birth = 3;#int(input('birth:'))
if birth < 2000:
	print('00 前')
else:
	print('00 后')

print("12 - 练习")
height = 1.75
wight = 80.5
bmi = wight/pow(height,2)
print("bmi:"+str(bmi))
if(bmi<18.5):
	print("过轻")
elif bmi>=18.5 and bmi<25 :
	print("正常")
elif bmi>=25 and bmi<28:
	print("过重")
elif bmi>=28 and bmi<32:
	print("肥胖")
elif bmi>=32:
	print("过于肥胖")

print("【13 - 循环】")

names = ['Michael', 'Bob', 'Tracy']
for name in names:
	print(name)

sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
	sum+=x
print(sum)
s = 0
for x in list(range(6)):
	s+=x
print(s)

for i in range(3):
	outputStr("输出结果：",i)
print("range(1,4,2) 循环输出，查看结果：")
#range(1,5,2) #代表从1到5，间隔2(不包含5)
for i in range(1,4,2):#1—初始值，4-终止点，不包含4，2-步长
    print(i)
print("13 - 练习")
L = ['Bart', 'Lisa', 'Adam']
for out in L:
	print("Hello,"+out)

print("14 - 使用 dict 和 set")

# Python 内置了字典： dict 的支持， dict 全称 dictionary，在其他语言中也
# 称为 map，使用键-值（ key-value）存储，具有极快的查找速度。python中的map表示高阶函数

d = {'Michael':98,'jack':88,'John':76}
outputStr("Michael成绩：",d['Michael'])
d['Pola'] = 84

d.pop('jack')#删除key
print(d)
print(d.get('Ali','指定默认值'))
# 和 list 比较， dict 有以下几个特点：
# 1. 查找和插入的速度极快，不会随着 key 的增加而增加；
# 2. 需要占用大量的内存，内存浪费多。
# 而 list 相反：
# 1. 查找和插入的时间随着元素的增加而增加；
# 2. 占用空间小，浪费内存很少。

# 因为 dict 根据 key 来计算 value 的存储位置，如果每次计算相同的
# key 得出的结果不同，那 dict 内部就完全混乱了。这个通过 key 计算位
# 置的算法称为哈希算法（ Hash）。
print("set部分")
s = set([1,2,3])
print(s)
# 重复元素在 set 中自动被过滤：
outputStr("输入[1,1,2,2,5],输出",set([1,1,2,2,5]))
s.remove(3)
outputStr("移除3之后的结果",s)
# set 可以看成数学意义上的无序和无重复元素的集合，因此，两个 set 可
# 以做数学意义上的交集、并集等操作
s1 = set([1,2,3])
s2 = set([2,3,4])
outputStr("s1和s2-交集：",s1&s2)
outputStr("s1和s2-并集：",s1|s2)

str1 = 'abc'
str1 = str1.replace('a','A')
print(str1)

print("15 16 - 函数 调用函数")

print(abs(-64))
print(max('b','a'))
print(max(1,2,5,8))




