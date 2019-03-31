# 第二章 字符串
message = " Hello python world! "
print(message)
# title以首字母大写的方式显示每个单词
print(message.title())
print(message.upper() + " = " + message.lower())
# 制表符或空格
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# 2.3.4 删除空白
# 末尾没有空白， 可使用方法rstrip(),剔除字符串开头的空白 lstrip(),剔除字符串两端的空白 strip()
msg = " space "
print(msg.rstrip())
print("剔除两端空白:" + msg.strip() + "!")

# 2.3.5 使用字符串时避免语法错误
message = 'One of Python\'s strengths is its diverse community.'
print(message)
# 2.4.1 整数
# Python使用两个乘号表示乘方运算

print(8 ** 2)

print(0.1 + 0.2)
print(3 / 2)

# 3.1 列表是什么
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[-2])#返回倒数第二个值

message = "我的第一辆自行车："+bicycles[0].title()
print(message)

#3.1 练习
names = ['张三','李四','王五','周六','小明']
for x in names:
    print(x,"早上好~")

#3.2 修改、添加和删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0]='ducati'
print(motorcycles)
#末尾添加元素
motorcycles.append('pada')
print(motorcycles)

#指定位置添加元素,指定新元素的索引和值
motorcycles.insert(1,'new data')
print(motorcycles)

#删除指定位置的元素
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print("honda已经删除 新的结果："+str(motorcycles))


# 有时候， 你要将元素从列表中删除， 并接着使用它的值。
# 例如， 你可能需要获取刚被射杀的外星人的 x 和 y 坐标，
# 以便在相应的位置显示爆炸效果； 在Web应用程序中， 你可能
# 要将用户从活跃成员列表中删除， 并将其加入到非活跃成员列表中。
# 方法pop() 可删除列表末尾的元素， 并让你能够接着使用它。
# 术语弹出 （ pop） 源自这样的类比： 列表就像一个栈，
# 而删除列表末尾的元素相当于弹出栈顶元素。
motorcycles = ['honda', 'yamaha', 'suzuki']
pop_motorcycles = motorcycles.pop(1)#pop()默认删除末尾的元素
print(motorcycles)
print(pop_motorcycles)



