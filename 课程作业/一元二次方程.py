# # -*- codeing = utf-8 -*-
# # @Time : 2021/9/14 17:30
# # @Author : chao
# # @File : 一元二次方程.py
# # @Software : PyCharm


# ax2+bx+c=0 （a !=0）
import math

a, b, c = map(float, input().split())
if a != 0:
    temp = (b ** 2) - (4 * a * c)
    if temp > 0:
        d = math.sqrt(temp)
        x1 = ((-b) + d) / (2 * a)
        x2 = ((-b) - d) / (2 * a)
        if x1 < x2:
            x1, x2 = x2, x1  # 保证 x1 比 x2大
        print("{:.2f} {:.2f}".format(x1, x2))

    elif temp == 0:
        x1 = (-b) / (2 * a)
        x2 = x1
        print("{:.2f} {:.2f}".format(x1, x2))

    else:
        print("No")
else:
    exit(0)


