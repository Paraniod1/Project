# -*- codeing = utf-8 -*-
# @Time : 2021/9/22 14:24
# @Author : chao
# @File : 圆周率的计算.py
# @Software : PyCharm
import random
import math
random.seed(123)
num = eval(input())
count = 0
for i in range(1, num+1):
    x, y = random.random(), random.random()
    res = math.sqrt(x**2 + y**2)
    if res <= 1:
        count = count + 1
pi = 4*(count/num)
print("{:.6f}".format(pi))