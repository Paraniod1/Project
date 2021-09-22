# -*- codeing = utf-8 -*-
# @Time : 2021/9/15 17:05
# @Author : chao
# @File : 练习.py
# @Software : PyCharm
# 一元二次方程系数求解

import math  # 引入数学函数

a, b, c = eval(input())  # 定义变量

d = b ** 2 - 4 * a * c

if d >= 0:  # 判断根号下是否大于等于0

    num = math.sqrt(d)

    x2 = (-b + num) / (2 * a)

    x1 = (-b - num) / (2 * a)

    print("x1=%0.2f" % x1)

    print("x2=%0.2f" % x2)

else:  # 如果根号下的数值小于零则无法求解，需要重新输入

    print("请重新输入")