# -*- codeing = utf-8 -*-
# @Time : 2021/9/20 18:02
# @Author : chao
# @File : 输入三个字符并排序.py
# @Software : PyCharm
list1 = list(input().split())
list1.sort()
for item in list1:
    print(item, end=' ')