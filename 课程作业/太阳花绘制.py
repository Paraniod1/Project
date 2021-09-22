# -*- codeing = utf-8 -*-
# @Time : 2021/9/15 14:33
# @Author : chao
# @File : 太阳花绘制.py
# @Software : PyCharm
import turtle
turtle.color("red", "yellow")
turtle.begin_fill()
while True:
    turtle.speed(0)     # 设置绘画速度 0-最快，1-最慢 加快绘制时间
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.pos()) < 1:
        break
turtle.end_fill()
turtle.done()
