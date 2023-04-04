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
        self.file_url_list = None

    my_str = pyqtSignal(str)  # 创建任务信号

    def set_file_url(self, file_url_list):
        self.file_url_list = file_url_list

    def run(self):
        """
        多线程功能函数
        :return:
        """
        dp = DownloadProduct()
        dp.get_token()
        dp.set_headers()
        while len(self.file_url_list) > 0:
            file_url = self.file_url_list.pop(0)
            dp.download_file(file_url)
            self.my_str.emit(file_url.split("/")[-1])
