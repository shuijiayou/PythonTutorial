#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('2018-2-25 13:10')
print('==== 9 面向对象高级编程 ====')

# 数据封装、继承和多态只是面向对象程序设计中最基础的 3 个概念。在
# Python 中，面向对象还有很多高级特性，允许我们写出非常强大的功能。
# 我们会讨论多重继承、定制类、元类等概念


# 通常情况下，上面的 set_score 方法可以直接定义在 class 中，但动态绑
# 定允许我们在程序运行的过程中动态给 class 加上功能，这在静态语言
# 中很难实现

class Student(object):
    pass



s = Student()
s.name = 'Michael'

print('输出实例动态绑定的属性值：',s.name)


def set_age(self,age):
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age,s)# 给实例绑定一个方法

s.set_age(31)
print('给实例绑定一个方法，输出结果值：',s.age)
# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：
# s2 = Student()
# s2.set_age(21)
#
# print('s2实例age属性值获取：',s2.age)

# 为了给所有实例都绑定方法，可以给 class 绑定方法：

def set_score(self,score):
    self.score = score

Student.set_score = MethodType(set_score,Student)

# 给 class 绑定方法后，所有实例均可调用

s.set_score(101)
print('给Student类绑定set_score方法，调用结果：',s.score)

# 常情况下，上面的 set_score 方法可以直接定义在 class 中，但动态绑
# 定允许我们在程序运行的过程中动态给 class 加上功能，这在静态语言
# 中很难实现。


print('========','9 - 1 使用__slots__')

# 如果我们想要限制实例的属性怎么办？比如，只允许对 Student
# 实例添加 name 和 age 属性。

class Student_slots(object):
    __slots__ = ('name','age')# 用 tuple 定义允许绑定的属性名称



slot = Student_slots()

# slot.score = 100
# print(slot.score)#此时会提示没有score属性
# 使用__slots__要注意， __slots__定义的属性仅对当前类实例起作用，对
# 继承的子类是不起作用的

class monitor(Student_slots):
    __slots__ = ('height')

monName = monitor()

monName.name='班长'
monName.age=21
monName.height = 182
# monName.sex ='男'


# print(monName.sex) #由于没有sex属性，故报错
print(monName.height)
# 在子类中也定义__slots__，这样，子类实例允许定义的属性就是自
# 身的__slots__加上父类的__slots__。


for x in range(2,10):
    for y in range(2,x):
        if x%y==0:
            print(x,"/",y,"=",x/y)
            break
    else:
        print(x,"是质数")


