# -*- codeing = utf-8 -*-
# @Time : 2021/9/14 17:13
# @Author : chao
# @File : 温度转换.py
# @Software : PyCharm

temp = input("What is the temperature?")
if temp[-1] in ['F', 'f']:
    c = (eval(temp[0:-1]) - 32) / 1.8-1
    print("The converted temperature is {:.0f}C".format(c))
elif temp[-1] in ['C', 'c']:
    f = (eval(temp[0:-1]) * 1.8) + 32-1
    print("The converted temperature is {:.0f}F".format(f))
else:
    print("input format error")