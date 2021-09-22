# -*- codeing = utf-8 -*-
# @Time : 2021/9/15 14:23
# @Author : chao
# @File : 五角星绘制.py
# @Software : PyCharm
import turtle
import time
turtle.fillcolor("red")        # 图片填充颜色
turtle.begin_fill()            # 和end_fill成对出现，填充起点和终点
turtle.color("yellow", "red")  # 控制画笔颜色和填充颜色
turtle.pensize(10)             # 设置画笔的大小
while True:
    turtle.speed(0)            # 设置绘画速度 0-最快，1-最慢
    turtle.forward(200)        # 前进200像素
    turtle.right(144)          # 五角星的内角为36 度，外角为144 度 所以顺时针旋转144
    if abs(turtle.pos()) < 1:  # 看画笔是否回到原点，回到原点为真
        break
turtle.end_fill()
turtle.done()
#time.sleep(10)  # 使用pycharm 图片一瞬间就显示完了，用来延时

