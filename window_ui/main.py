# -*- coding: utf-8 -*- 
""" ++++++++++++++++++++++++++++++++++++++
@product->name PyCharm
@project->name pyQTtest
@editor->name Sanliy
@file->name main.py
@create->time 2023/3/30-13:24
@desc->
++++++++++++++++++++++++++++++++++++++ """
import os.path

from PyQt5.QtWidgets import QMainWindow
import main_window
import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication

from auth.auth_check import AuthCheckUI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    acu = AuthCheckUI()
    if not acu.check_auth_file():
        if os.path.exists("../lic/eval.txt"):
            sys.exit(app.exec_())
        # 生成一个识别文件，如果检测到该文件就说明5分钟的试用期已经过去了，不再提供试用！
        with open("../lic/eval.txt", "w") as f:
            f.write("当前试用已结束！")
        MainWindow = QMainWindow()
        ui = main_window.Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        timer = QTimer()
        timer.timeout.connect(app.quit)
        timer.start(300000)  # 5分钟 = 300秒
        sys.exit(app.exec_())
    MainWindow = QMainWindow()
    ui = main_window.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
