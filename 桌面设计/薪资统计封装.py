# -*- codeing = utf-8 -*-
# @Time : 2021/8/12 17:28
# @Author : chao
# @File : 薪资统计封装.py
# @Software : PyCharm


# 让用户输入一段文本包含：员工姓名、薪资、年龄。
# 该程序可以把薪资在 2万 以上、以下的人员名单分别打印出来。
# 当用户点击 统计 按钮时， 从界面控件 QPlainTextEdit 里面获取 用户输入的字符串内容，进行处理。

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox

class Stats():
    def __init__(self):
        # 创建窗口
        self.window = QMainWindow()
        # 窗口的大小
        self.window.resize(500, 400)
        # 窗口的坐标
        self.window.move(300, 310)
        # 标题
        self.window.setWindowTitle("薪资统计")

        # 窗口里文本编辑的部分    基于窗口
        self.textEidt = QPlainTextEdit(self.window)
        # 用户没输入数据时显示， 输入数据后覆盖
        self.textEidt.setPlaceholderText("请输入薪资表")
        self.textEidt.move(10, 25)
        self.textEidt.resize(300, 350)

        # 按键统计部分
        self.button = QPushButton("统计", self.window)
        self.button.move(380, 80)  # 该坐标基于 window控件
        # 将按键与程序连接起来 如果该键被按下 执行handleCalc函数
        self.button.clicked.connect(self.handleCalc)

    def handleCalc(self):
        info = self.textEidt.toPlainText()  # 接收数据
        # 名单
        hsalary = ''  # 高于2万
        lsalary = ''  # 低于2万
        # 以换行符作为分隔符来分割字符串，并返回数组
        for item in info.splitlines():  # 以换行符分割字符串
            # 去除首位空格
            if not item.strip():  # strip() 函数移除字符串头尾指定的字符（默认为空格或换行符）或字符序列  str.strip( '0' ); # 去除首尾字符 0
                continue  # 该方法只能删除开头或是结尾的字符，不能删除中间部分的字符
            # split() ：通过指定分隔符对字符串进行分割，并返回数组。默认情况下，分隔符为空格
            parts = item.split(' ')  # 以空格为界 分割  去掉列表中空格

            parts = [i for i in parts if i]  # 列表推导式 parts非空字符
            name, salary, age = parts
            if int(salary) >= 20000:
                hsalary += name + '\n'
            else:
                lsalary += name + '\n'

        # 弹出对话框
        QMessageBox.about(self.window,
                          '统计结果',
                          f'''薪资20000 以上的有：\n{hsalary}
                        \n薪资20000 以下的有：\n{lsalary}'''
                          )

# QApplication 提供了整个图形界面程序的底层管理功能  必须在任何界面控件对象创建前
app = QApplication([])
stats = Stats()
stats.window.show()
# 进入QApplication的事件处理循环，接收用户的输入事件（），并且分配给相应的对象去处理。
app.exec_()