# -*- coding: utf-8 -*-
import os
import time

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from window_ui.download_thread import DownloadThread
from window_ui.search_thread import SearchThread


class Ui_MainWindow(object):

    def __init__(self):
        self.start_date = None
        self.end_date = None
        self.spatial_tuple = tuple()
        self.version = None
        self.product = None
        self.download_url = list()
        self.thread_num = 6
        # 放在__init__(self):下，主窗口类实例，初始化时加载
        self.my_thread1 = DownloadThread()
        self.my_thread1.my_str.connect(self.get_sin_out_download)

        self.my_thread2 = SearchThread()
        self.my_thread2.my_list.connect(self.get_sin_out_search)

        self.flag = 1

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QIcon('../image/main.ico'))
        MainWindow.resize(1251, 864)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(187, 60, 104, 41))
        self.textEdit.setObjectName("textEdit")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(230, 230, 31, 20))
        self.label_5.setObjectName("label_5")
        self.textEdit_6 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_6.setGeometry(QtCore.QRect(187, 180, 104, 41))
        self.textEdit_6.setObjectName("textEdit_6")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 220, 51))
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 690, 371, 61))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(230, 30, 31, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(90, 90, 41, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(350, 170, 41, 20))
        self.label_4.setObjectName("label_4")
        self.textEdit_5 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_5.setGeometry(QtCore.QRect(287, 120, 104, 41))
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(10, 420, 81, 21))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(10, 470, 81, 21))
        self.label_14.setObjectName("label_14")
        self.textEdit_7 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_7.setGeometry(QtCore.QRect(77, 120, 104, 41))
        self.textEdit_7.setObjectName("textEdit_7")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_2.setGeometry(QtCore.QRect(520, 50, 571, 701))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_3.setGeometry(QtCore.QRect(170, 410, 211, 31))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_4.setGeometry(QtCore.QRect(170, 470, 211, 31))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab)
        self.pushButton_6.setGeometry(QtCore.QRect(60, 540, 371, 61))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 620, 371, 61))
        self.pushButton_2.setMinimumSize(QtCore.QSize(159, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(170, 360, 321, 31))
        self.comboBox.setEditable(False)
        self.comboBox.setMaxVisibleItems(7)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(12, 362, 111, 31))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(12, 304, 111, 31))
        self.label_9.setObjectName("label_9")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(12, 256, 111, 31))
        self.label_6.setObjectName("label_6")
        self.dateEdit = QtWidgets.QDateEdit(self.tab)
        self.dateEdit.setGeometry(QtCore.QRect(170, 260, 211, 31))
        self.dateEdit.setDate(QtCore.QDate(2023, 1, 1))
        self.dateEdit.setObjectName("dateEdit")

        # 设置可以弹出日历
        self.dateEdit.setCalendarPopup(True)

        self.dateEdit_4 = QtWidgets.QDateEdit(self.tab)
        self.dateEdit_4.setGeometry(QtCore.QRect(170, 310, 211, 31))
        self.dateEdit_4.setDate(QtCore.QDate(2023, 1, 1))
        self.dateEdit_4.setObjectName("dateEdit_4")

        # 设置可以弹出日历
        self.dateEdit_4.setCalendarPopup(True)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser.setGeometry(QtCore.QRect(180, 80, 781, 581))
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_6.clicked.connect(lambda: self.start_search_thread())
        # self.pushButton_2.clicked.connect(self.download_files)
        self.pushButton_2.clicked.connect(lambda: self.stop_download_task())

    def start_download_thread(self):
        """
        启动线程
        :return:
        """
        try:
            if self.download_url:
                # self.textBrowser_3.setText(str(len(self.download_url)))
                self.textBrowser_2.setPlainText("")
                self.textBrowser_2.insertPlainText("正在开始下载数据...\n")
                self.my_thread1.set_file_url(self.download_url, self.start_date, self.end_date)
                self.my_thread1.start()
                # self.textBrowser_2.insertPlainText("所有下载均已完成，请查收！\n")
            else:
                self.textBrowser_2.setPlainText("暂无可下载的数据")
        except Exception as error:
            print(error)

    def stop_download_thread(self):
        """
        启动线程
        :return:
        """
        try:
            if self.download_url:
                # self.textBrowser_3.setText(str(len(self.download_url)))
                self.textBrowser_2.setPlainText("")
                self.textBrowser_2.insertPlainText("正在开始下载数据...\n")
                self.my_thread1.set_file_url(self.download_url, self.start_date, self.end_date)
                self.my_thread1.start()
                # self.textBrowser_2.insertPlainText("所有下载均已完成，请查收！\n")
            else:
                self.textBrowser_2.setPlainText("暂无可下载的数据")
        except Exception as error:
            print(error)

    def start_search_thread(self):
        """
        启动线程
        :return:
        """
        try:
            self.get_search_params()

            self.my_thread2.set_params(self.start_date, self.end_date, self.spatial_tuple, self.product, self.version)
            self.my_thread2.start()

        except Exception as error:
            print(error)

    def get_search_params(self):
        self.start_date = self.dateEdit.date().toString('yyyy-MM-dd')
        self.end_date = self.dateEdit_4.date().toString('yyyy-MM-dd')
        self.spatial_tuple = (
            int(self.textEdit_7.toPlainText()),
            int(self.textEdit.toPlainText()),
            int(self.textEdit_5.toPlainText()),
            int(self.textEdit_6.toPlainText())
        )

        self.product = ["MOD03", "MOD09GQ", "MOD35_L2"]

        if self.comboBox.currentText() == "MOD03（61）、MOD09GQ（6）、MOD35_L2（61）":
            self.version = 1
        else:
            self.version = 0

        print(self.start_date)
        print(self.end_date)
        print(self.spatial_tuple)
        print(self.version)
        print(self.product)

    def get_sin_out_download(self, out_str):
        """
        :param out_str:
        :return:
        """
        self.textBrowser_2.insertPlainText(f"[{out_str}]下载完成！\n")
        self.textBrowser_4.setPlainText(str(self.flag))
        self.flag += 1

    def get_sin_out_search(self, out_str):
        """
        :param out_str:
        :return:
        """
        self.download_url = out_str
        # 在进行检索展示之前需要先清空textbrowser 避免上次的检索结果对本次检索结果造成影响
        self.textBrowser_3.setPlainText("")
        self.textBrowser_2.setPlainText("")
        # 这里需要将检索到的数据展示到右侧的 textbrow 中 以遍用户进行查看
        self.textBrowser_2.insertPlainText(f"已经检索到了[{len(self.download_url)}]景数据..." + "\n")
        self.textBrowser_3.setPlainText(str(len(self.download_url)))
        for download_url in self.download_url:
            self.textBrowser_2.insertPlainText(os.path.basename(download_url) + "\n")
            print(os.path.basename(download_url))
            # 实时页面刷新， 防止textbrowser中的信息加载不出来
            QApplication.processEvents()
        if self.download_url:
            # 这里给个时间暂停模块，方便用户可以观察到检索到的数据
            time.sleep(2)
            # 检索完毕执行下载模块
            self.start_download_thread()

    def stop_download_task(self):
        ...

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "长势监测软件-绿色免安装版"))
        self.label_5.setText(_translate("MainWindow", "下"))
        self.label.setText(_translate("MainWindow", "监测坐标范围（十进制度）"))
        self.pushButton_5.setText(_translate("MainWindow", "3.生成 NDVI 数据"))
        self.label_2.setText(_translate("MainWindow", "上"))
        self.label_3.setText(_translate("MainWindow", "左"))
        self.label_4.setText(_translate("MainWindow", "右"))
        self.label_13.setText(_translate("MainWindow", "总个数："))
        self.label_14.setText(_translate("MainWindow", "已下载："))
        self.pushButton_6.setText(_translate("MainWindow", "1.下载数据"))
        self.pushButton_2.setText(_translate("MainWindow", "2.暂停下载"))
        self.comboBox.setCurrentText(_translate("MainWindow", "MOD03（61）、MOD09GQ（6）、MOD35_L2（61）"))
        self.comboBox.setItemText(0, _translate("MainWindow", "MOD03（61）、MOD09GQ（6）、MOD35_L2（61）"))
        self.comboBox.setItemText(1, _translate("MainWindow", "MOD03（61）、MOD09GQ（61）、MOD35_L2（61）"))
        self.label_7.setText(_translate("MainWindow", "所需数据版本："))
        self.label_9.setText(_translate("MainWindow", "终止日期："))
        self.label_6.setText(_translate("MainWindow", "起始日期："))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "yyyy-M-d"))
        self.dateEdit_4.setDisplayFormat(_translate("MainWindow", "yyyy-M-d"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "数据处理"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">二十一世纪空间技术应用有限公司</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:700;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:700;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:700;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">产品名称：长势监测软件</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">  产品类型：exe可执行程序</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "软件信息"))
