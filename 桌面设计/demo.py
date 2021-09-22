# -*- codeing = utf-8 -*-
# @Time : 2021/8/12 17:06
# @Author : chao
# @File : demo.py
# @Software : PyCharm
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit, QMessageBox

def handleCalc():
    print('统计按钮被点击了')

app = QApplication([])

window = QMainWindow()
window.resize(500, 400)
window.move(300, 300)
window.setWindowTitle('薪资统计')

textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("请输入薪资表")
textEdit.move(10,25)
textEdit.resize(300,350)

button = QPushButton('统计', window)
button.move(380,80)
button.clicked.connect(handleCalc)

window.show()

app.exec_()