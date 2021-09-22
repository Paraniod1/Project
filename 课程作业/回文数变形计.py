# -*- codeing = utf-8 -*-
# @Time : 2021/9/20 18:06
# @Author : chao
# @File : 回文数变形计.py
# @Software : PyCharm
n = input()     # n= 12
i = 1
# print(n[:])     # 12
# print(n[::-1])  # 21
while i < 7:
    a = eval(n[:]) + eval(n[::-1])
    # print(a)
    a = str(a)
    if a[:] == a[::-1]:
        print(i)
        break
    elif i < 7:
        n = a
    i = i + 1
if i == 7:
    print(0)


