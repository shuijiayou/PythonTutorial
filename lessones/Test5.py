#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("====7 - 模块====")
# 以内建的 sys 模块为例，编写一个 hello 的模块
'a Test module' # 任何模块代码的第一个字符串都被视为模块的文档注释；
__author__='code' # 使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello,world')
    elif len(args)==2:
        print('Hello,%s!'%args[1])
    else:
        print('Too many arguments')

    if __name__=='__main__':
        test()

# 导入 sys 模块后，我们就有了变量 sys 指向该模块，利用 sys 这个变量，
# 就可以访问 sys 模块的所有功能。
# sys 模块有一个 argv 变量，用 list 存储了命令行的所有参数。 argv 至少
# 有一个元素，因为第一个参数永远是该.py 文件的名称，例如：
# 运行 python3 hello.py 获得的 sys.argv 就是['hello.py']；
# 运行 python3 hello.py Michael 获得的 sys.argv 就是['hello.py',
# 'Michael]。
# 最后，注意到这两行代码：
# if __name__=='__main__':
# test()
# 当我们在命令行运行 hello 模块文件时， Python 解释器把一个特殊变量
# __name__置为__main__，而如果在其他地方导入该 hello 模块时， if 判断
# 将失败，因此，这种 if 测试可以让一个模块通过命令行运行时执行一
# 些额外的代码，最常见的就是运行测试。


# 正常的函数和变量名是公开的（ public），可以被直接引用，比如： abc，
# x123， PI 等；
# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，
# 比如上面的__author__， __name__就是特殊变量， hello 模块定义的文档
# 注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变
# 量名；

# 类似_xxx 和__xxx 这样的函数或变量就是非公开的（ private），不应该被
# 直接引用，比如_abc， __abc 等；
# 之所以我们说， private 函数和变量“不应该”被直接引用，而不是“不能”
# 被直接引用，是因为 Python 并没有一种方法可以完全限制访问 private
# 函数或变量，但是，从编程习惯上不应该引用 private 函数或变量。
from PIL import Image
print("========7-2 安装第三方模块====")

im = Image.open('/Users/yujinshui/Desktop/个人处理/1451033541380.jpg')
print("获取的图片信息",im.format,im.size,im.mode)
#如何将宽高比等比缩放
width,height = im.size

print("图片压缩操作")
im.thumbnail((width/10,height/10))

print("压缩后的图片宽度：",width/10,'高度：',height/10)
im.save('/Users/yujinshui/Desktop/个人处理/thumb.jpg','jpeg')
print("图片压缩成功")

print(sys.path)







































