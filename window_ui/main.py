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
from PyQt5.QtWidgets import QApplication, QMainWindow

import main_window


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = main_window.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
