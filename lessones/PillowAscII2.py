# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image
import argparse



# 灰度值小（暗）的用列表开头的符号，灰度值大（亮）的用列表末尾的符号。
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


# 将256灰度映射到列表的70个字符上
def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]


if __name__ == '__main__':
    fp = open(u'/Users/yujinshui/Desktop/ww2.png', 'rb')
    im = Image.open(fp)
    # im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    WIDTH=int(im.size[0])
    HEIGHT=int(im.size[1])
    im.resize((WIDTH, HEIGHT), Image.NEAREST)  # 调整图片大小
    # print(u'Info:', im.size[0], ' ', im.size[1], ' ', count)


    txt = ""
    # 字符画打印
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'
    print(txt)

    #字符画输出到文件
    tmp = open('/Users/yujinshui/Desktop/out.txt', 'w')
    tmp.write(txt)
    tmp.close()