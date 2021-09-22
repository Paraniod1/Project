# -*- codeing = utf-8 -*-
# @Time : 2021/9/20 17:27
# @Author : chao
# @File : 逆序排列.py
# @Software : PyCharm

list1 = []
i = 10
while i > 0:
    num = input()
    list1.append(num)
    i = i-1
list1.reverse()
for item in list1:
    print(item, end=' ')