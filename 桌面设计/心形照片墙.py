# -*- codeing = utf-8 -*-
# @Time : 2021/8/13 20:48
# @Author : chao
# @File : 心形照片墙.py
# @Software : PyCharm

import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
import PyQt5.QtGui as qt

app = QApplication(sys.argv)

win = QWidget()
win.resize(760, 540)
win.move(0, 0)
layout = QGridLayout(win)

b = QLabel(win)
b.setPixmap(QPixmap("bg.png"))
b.setGeometry(0, 0, 820, 640)


def positionSet():
    bi = []
    for i in range(0, 54, 1):
        # b=QLabel(win)
        bi.append(QLabel(win))
        bi[i].setPixmap(QPixmap("new\\pic (" + str(i + 1) + ").jpg"))

    layout.addWidget(bi[0], 0, 3)
    layout.addWidget(bi[1], 0, 7)
    layout.addWidget(bi[2], 1, 2)
    layout.addWidget(bi[3], 1, 4)
    layout.addWidget(bi[4], 1, 6)
    layout.addWidget(bi[5], 1, 8)
    layout.addWidget(bi[6], 2, 1)
    layout.addWidget(bi[7], 2, 5)
    layout.addWidget(bi[8], 2, 9)
    layout.addWidget(bi[9], 3, 0)
    layout.addWidget(bi[10], 3, 10)
    layout.addWidget(bi[11], 4, 1)
    layout.addWidget(bi[12], 4, 9)
    layout.addWidget(bi[13], 5, 2)
    layout.addWidget(bi[14], 5, 8)
    layout.addWidget(bi[15], 6, 3)
    layout.addWidget(bi[16], 6, 7)
    layout.addWidget(bi[17], 7, 4)
    layout.addWidget(bi[18], 7, 5)
    layout.addWidget(bi[19], 7, 6)
    layout.addWidget(bi[20], 8, 5)
    layout.addWidget(bi[21], 6, 5)
    layout.addWidget(bi[22], 5, 5)
    layout.addWidget(bi[23], 3, 5)
    layout.addWidget(bi[24], 4, 5)
    layout.addWidget(bi[25], 4, 3)
    layout.addWidget(bi[26], 3, 2)
    layout.addWidget(bi[27], 4, 2)
    layout.addWidget(bi[28], 3, 4)
    layout.addWidget(bi[29], 3, 6)
    layout.addWidget(bi[30], 3, 7)
    layout.addWidget(bi[31], 3, 8)
    layout.addWidget(bi[32], 3, 9)
    layout.addWidget(bi[33], 2, 8)
    layout.addWidget(bi[35], 5, 7)
    layout.addWidget(bi[36], 2, 8)
    layout.addWidget(bi[33], 4, 7)
    layout.addWidget(bi[34], 4, 6)
    layout.addWidget(bi[35], 5, 7)
    layout.addWidget(bi[36], 5, 6)
    layout.addWidget(bi[37], 6, 6)
    layout.addWidget(bi[38], 6, 4)
    layout.addWidget(bi[39], 2, 3)
    layout.addWidget(bi[40], 5, 7)
    layout.addWidget(bi[41], 2, 8)
    layout.addWidget(bi[42], 2, 6)
    layout.addWidget(bi[43], 2, 7)
    layout.addWidget(bi[44], 1, 7)
    layout.addWidget(bi[45], 2, 4)
    layout.addWidget(bi[46], 5, 3)
    layout.addWidget(bi[47], 2, 2)
    layout.addWidget(bi[48], 3, 1)
    layout.addWidget(bi[49], 1, 3)
    layout.addWidget(bi[50], 3, 3)
    layout.addWidget(bi[51], 4, 8)
    layout.addWidget(bi[52], 4, 4)
    layout.addWidget(bi[53], 5, 4)


positionSet()
win.setWindowTitle('爱心墙')
win.setWindowIcon(qt.QIcon("0.png"))
win.show()

sys.exit(app.exec_())
