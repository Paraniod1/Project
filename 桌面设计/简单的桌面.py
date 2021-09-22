# -*- codeing = utf-8 -*-
# @Time : 2021/8/12 14:39
# @Author : chao
# @File : 简单的桌面.py
# @Software : PyCharm
import sys
# 必须使用两个类：QApplication和QWidget。都在PyQt5.QtWidgets。
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    # 创建 QApplication 的实例
    app = QApplication(sys.argv)
    # 创建一个窗口
    win = QWidget()
    # 设置窗口的大小
    win.resize(450, 450)
    # 设置窗口在屏幕的坐标
    win.move(500, 500)
    # 设置窗口的标题
    win.setWindowTitle("我的第一个桌面应用")
    # 显示窗口
    win.show()

    # 进入程序的主循环， 并通过exit()函数确保主循环安全结束
    sys.exit(app.exec_())


