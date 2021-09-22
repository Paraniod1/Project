# -*- codeing = utf-8 -*-
# @Time : 2021/9/14 17:23
# @Author : chao
# @File : 统计字母个数.py
# @Software : PyCharm
str = input()
low = 0
high = 0
decm = 0
for item in str:
    if item.isupper():
        high += 1
    elif item.islower():
        low += 1
    elif item.isdigit():
        decm += 1
print(high)
print(low)
print(decm)

