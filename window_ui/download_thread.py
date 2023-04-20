# -*- coding: utf-8 -*- 
""" ++++++++++++++++++++++++++++++++++++++
@product->name PyCharm
@project->name growth_analysis
@editor->name Sanliy
@file->name download_thread.py
@create->time 2023/4/3-13:31
@desc->
++++++++++++++++++++++++++++++++++++++ """
from PyQt5.QtCore import QThread, pyqtSignal

from download.download_product import DownloadProduct


class DownloadThread(QThread):

    def __init__(self):
        super().__init__()
        self.area = None
        self.status = 0
        self.file_url_list = list()
        self.start_date = None
        self.end_date = None

    my_str = pyqtSignal(list)  # 创建任务信号

    def set_file_url(self, file_url_list, start_date, end_date, area):
        self.file_url_list = file_url_list
        self.start_date = start_date
        self.end_date = end_date
        self.area = area

    def run(self):
        """
        多线程功能函数
        :return:
        """

        while len(self.file_url_list) > 0:
            print(self.file_url_list)
            print(self.status)
            if self.status == 4:
                break
            file_url = self.file_url_list[0]
            self.my_str.emit([file_url, 1])
            dp = DownloadProduct()
            dp.get_token()
            dp.set_headers()
            dp.download_file(file_url, self.start_date, self.end_date, self.area)
            self.file_url_list.remove(file_url)
            self.my_str.emit([file_url, 0])
        self.my_str.emit(["done", 10])

    def stop(self):
        self.status = 4

    def resume(self):
        self.status = 0
