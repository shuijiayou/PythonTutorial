#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("====8 - 面向对象编程====")

# 面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数
# 的顺序执行。为了简化程序设计，面向过程把函数继续切分为子函数，
# 即把大块函数通过切割成小块函数来降低系统的复杂度。
# 而面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象
# 都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执
# 行就是一系列消息在各个对象之间传递。

std1 = {'name':'Michael','score':98}
std2 = {'name':'Bob','score':81}

def print_score(std):
    print('%s %s'%(std['name'],std['score']))

print_score(std1)

class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s - %s'%(self.name,self.score))
    def get_grade(self):
        if self.score>=90:
            return 'A'
        elif self.score>=60:
            return 'B'
        else:
            return 'C'


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

# 小结
# 数据封装、继承和多态是面向对象的三大特点，我们后面会详细讲解。

print('========8-1 类和实例')
# class 后面紧接着是类名，即 Student，类名通常是大写开头的单词，紧
# 接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后
# 面再讲，通常，如果没有合适的继承类，就使用 object 类，这是所有类
# 最终都会继承的类定义好了 Student 类，就可以根据 Student 类创建出 Student 的实例，创
# 建实例是通过类名+()实现的

# >>> bart = Student()
# >>> bart
# <__main__.Student object at 0x10a67a590>
# >>> Student
# <class '__main__.Student'>

# 通过定义一个特殊的__init__方法，在创建实例的时候，就把 name， score 等属性绑上去：

# class Student(object):
# def __init__(self, name, score):
# self.name = name

# 注意到__init__方法的第一个参数永远是 self，表示创建的实例本身，
# 因此，在__init__方法内部，就可以把各种属性绑定到 self，因为 self
# 就指向创建的实例本身。

# 了__init__方法，在创建实例的时候，就不能传入空的参数了，必须
# 传入与__init__方法匹配的参数，但 self 不需要传， Python 解释器自己
# 会把实例变量传进去
# >>> bart = Student('Bart Simpson', 59)
# >>> bart.name
# >>> 'Bart Simpson'
# >>> bart.score
# >>> 59
# 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数
# 永远是实例变量 self，并且，调用时，不用传递该参数。除此之外，类
# 的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变
# 参数、关键字参数和命名关键字参数。

print('【数据封装】')
# 面向对象编程的一个重要特点就是数据封装。

print(bart.get_grade())
# 小结
# 和静态语言不同， Python 允许对实例变量绑定任何数据，也就是说，对
# 于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名
# 称都可能不同：demo如下，

# bart = Student('Bart Simpson', 59)
# bart.age = 8
# print(bart.age)
# print(lisa.age)#会报错，Lisa不存在age属性

print('========8 - 2 访问限制 ')

# 在 Class 内部，可以有属性和方法，而外部代码可以通过直接调用实例
# 变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。
# 但是，从前面 Student 类的定义来看，外部代码还是可以自由地修改一
# 个实例的 name、 score 属性：

# >>> bart = Student('Bart Simpson', 98)
# >>> bart.score
# 98
# >>> bart.score = 59
# >>> bart.score
# 59

print(bart.score)
bart.score = 98
print('bart.score has changed:',bart.score)
bart.score=59
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线
# __，在 Python 中，实例的变量名如果以__开头，就变成了一个私有变量
# （ private），只有内部可以访问，外部不能访问，所以，我们把 Student
# 类改一改：

class PriStudent(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s %s' %(self.__name,self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score


# 改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问实
# 例变量.__name 和实例变量.__score 了：

priBart = PriStudent('Bart Simpon',59)
# print(priBart.__name)#此处报错，已注释
# 这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限
# 制的保护，代码更加健壮。

#获取__name和__score属性的值

print('通过get方式获取私有属性的值',priBart.get_name(),priBart.get_score())