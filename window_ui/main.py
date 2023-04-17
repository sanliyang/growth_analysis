# -*- coding: utf-8 -*- 
""" ++++++++++++++++++++++++++++++++++++++
@product->name PyCharm
@project->name pyQTtest
@editor->name Sanliy
@file->name main.py
@create->time 2023/3/30-13:24
@desc->
++++++++++++++++++++++++++++++++++++++ """
import sys
import os.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import os.path

from PyQt5.QtWidgets import QMainWindow, QMessageBox
from window_ui.main_window import Ui_MainWindow
# from . import main_window
import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication
from auth.auth_check import AuthCheckUI

app = QApplication(sys.argv)

if os.path.exists(os.path.join(os.path.dirname(__file__), "lic", "eval.txt")):
    msg_box = QMessageBox()
    msg_box.setText(
        '试用已结束，软件将关闭！如想继续使用，请联系管理员获取授权')
    msg_box.setWindowTitle('试用结束')
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.exec_()
    sys.exit()
else:
    acu = AuthCheckUI()
    if not acu.check_auth_file():
        # 生成一个识别文件，如果检测到该文件就说明5分钟的试用期已经过去了，不再提供试用！
        with open(os.path.join(os.path.dirname(__file__), "lic", "eval.txt"), "w", encoding="utf8") as f:
            f.write("当前试用已结束！")
        MainWindow = QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        timer = QTimer()
        timer.timeout.connect(app.quit)
        timer.start(300000)  # 5分钟 =
        sys.exit(app.exec_())
    else:
        MainWindow = QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
# 测试新分支