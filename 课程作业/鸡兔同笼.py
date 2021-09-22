# -*- codeing = utf-8 -*-
# @Time : 2021/9/22 14:03
# @Author : chao
# @File : 鸡兔同笼.py
# @Software : PyCharm
# a头 b脚
a, b = map(int, input().split(' '))
# x 鸡的数量
# y 兔的数量
flag = 1
for x in range(1, a+1):
    y = a - x
    if 2 * x + 4 * y == b:
        flag = 1
        break
    else:
        flag = 0
if flag:
    print("{} {}".format(x, y))
else:
    print("Data Error!")