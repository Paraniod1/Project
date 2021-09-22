# -*- codeing = utf-8 -*-
# @Time : 2021/9/20 19:25
# @Author : chao
# @File : 绩点计算.py
# @Software : PyCharm


score = {'A':4.0,'A-':3.7,'B+':3.3,'B':3.0,'B-':2.7,'C+':2.3,'C':2.0,'C-':1.5,'D':1.3,'D-':1.0,'F':0.0}
gpaSum,creditSum = 0,0
while True:
    grade = input()
    if grade == '-1':
        break
    else:
        credit = float(input())
        gpaSum = gpaSum + score[grade] * credit
        creditSum = creditSum + credit

gpaAve = gpaSum / creditSum
print('{:.2f}'.format(gpaAve))
