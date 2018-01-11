#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def printStr(str):
    print("====",str.__name__,"函数输出：====")


#装饰器学习
a_string = "This is a global variable"
def foo():
    print(locals())
print(globals())
printStr(foo)
foo()#2
# 2. 作用域
# 内建函数 globals 返回一个包含所有 Python 能识别变量的字典。（为了更清楚的描述，输
# 出时省略了 Python 自动创建的变量。）在注释 #2 处，调用了 foo 函数，在函数中打印局
# 部变量的内容。从中可以看到，函数 foo 有自己单独的、此时为空的命名空间。


# 3. 变量解析规则
# Python 的作用域规则是， 变量的创建总是会创建一个新的局部变量但是变量的访问（包括修改）
# 在局部作用域查找然后是整个外层作用域来寻找匹配。所以如果修改 foo 函数来打印全部变量，
# 结果将是我们希望的那样：

def foo3():
    print(a_string)#1
printStr(foo3)
foo3()
# 在 #1 处，Python 在函数 foo 中搜索局部变量 a_string，但是没有找到，然后继续搜索同名的全局变量。
# 另一方面，如果尝试在函数里给全局变量赋值，结果并不是我们想要的那样：

def foo3_1():
    a_string = "test"  #1
    print(locals())
printStr(foo3_1)
foo3_1()
print(a_string)#2

# 从上面代码可见，全部变量可以被访问（如果是可变类型，甚至可以被修改）但是（默认）
# 不能被赋值。在函数 #1 处，实际上是创建了一个和全局变量相同名字的局部变量，并且
# “覆盖”了全局变量。通过在函数 foo 中打印局部命名空间可以印证这一点，并且发现局部
# 命名空间有了一项数据。在 #2 处的输出可以看到，全局命名空间里变量 a_string 的值
# 并没有改变。

# 4. 变量生命周期
# 值得注意的是，变量不仅是在命名空间中有效，它们也有生命周期。思考下面的代码：

def foo4():
    x=1
printStr(foo4)
foo4()
print("该部分需要解开下一行方法的注释")
# print(x)#1
# 这个问题不仅仅是因为 #1 处的作用域规则（虽然那是导致 NameError 的原因），也与Python
# 和很多其他语言中函数调用的实现有关。没有任何语法可以在该处取得变量 x 的值——它确确实实
# 不存在！函数 foo 的命名空间在每次函数被调用时重新创建，在函数结束时销毁。

# 5. 函数的实参和形参
# Python 允许向函数传递参数。形参名在函数里为局部变量。
def foo5(x):
    print(locals())
printStr(foo5)
foo5(1)
# Python 有一些不同的方法来定义和传递函数参数。想要深入的了解，请参考 Python 文档关于函数的定义。
# 【http://docs.python.org/tutorial/controlflow.html#more-on-defining-functions】
# 来说一个简单版本：函数参数可以是强制的位置参数或者可选的有默认值的关键字参数。

def foo5_1(x, y=0):
    return x-y
printStr(foo5_1)
print(foo5_1(y=1,x=3))
# Python 支持在函数调用时使用关键字实参。
# 上述函数是用一个关键字形参和一个位置形参定义的，但此处使用了两个关键字实参来调用该函数。因为参数都有名称，所以传递参数的顺序没有影响。

# 哇哦！说了这么多看起来可以简单概括为一点：函数的参数可以有名称或位置。也就是说这其中
# 稍许的不同取决于是函数定义还是函数调用。可以对用位置形参定义的函数传递关键字实参，
# 反过来也可行！如果还想进一步了解请查看 Python 文档
# 【http://docs.python.org/tutorial/controlflow.html#more-on-defining-functions】。

# 6. 内嵌函数



