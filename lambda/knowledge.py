#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce


# lambda语句中，冒号前是参数，可以有多个，用逗号隔开，冒号右边的返回值。lambda语句构建的其实是一个函数对象。
def _not_divisible(n):
    bk = lambda x: x % n > 0
    return bk


print(_not_divisible(4))

lam = lambda x, y: x * y
print(lam(4, 5))

print(lambda: 'begin')  # <function <lambda> at 0x00B00A30>


# 2、无参数
# 如果没有参数，则lambda冒号前面就没有，如以上例子。

# 3、有参数
def add(x, y): return x + y


add2 = lambda x, y: x + y
print(add2(1, 2))  # 3
print(reduce(add2, (1, 2, 3, 4)))  # 10


def sum(x, y=10): return x + y


sum2 = lambda x, y=10: x + y
print(sum2(1))  # 11
print(sum2(1, 100))  # 101

# python获取系统日期
# http://www.runoob.com/python/python-date-time.html
import time

print("time=", time.time())
print("localtime=", time.localtime(time.time()))
print("asctime=", time.asctime(time.localtime(time.time())))
print("日期格式化：", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print ('将格式字符串转换为时间戳',time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

#python中时间日期格式化符号：
#
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身

import calendar

cal = calendar.month(2016, 1)
print("以下输出2016年1月份的日历:")
print (cal);

