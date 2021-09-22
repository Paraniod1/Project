# -*- codeing = utf-8 -*-
# @Time : 2021/8/11 20:12
# @Author : chao
# @File : xlwttest.py
# @Software : PyCharm

import xlwt
workbook = xlwt.Workbook(encoding = 'utf-8')          # 创建workbook对象,也就是一个文件
worksheet = workbook.add_sheet('sheet1')              # 创建工作表
# worksheet.write(0, 0, '1321')                     # 往表中传参数，前两个参数是行，列，最后一个为内容
# workbook.save('Student.xls')                          # 保存表为Student.xls
for i in range(1, 10):
    for j in range(1, 10):
        if i >= j:
            worksheet.write(i-1, j-1, "{}*{}={}".format(j, i, i*j))
workbook.save('Student.xls')                          # 保存表为Student.xls