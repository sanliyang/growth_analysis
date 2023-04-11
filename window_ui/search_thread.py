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

from download.search_product import SearchProduct


class SearchThread(QThread):

    def __init__(self):
        super().__init__()
        self.start_date = None
        self.end_date = None
        self.spatial_tuple = tuple()
        self.product = None

    my_list = pyqtSignal(list)  # 创建任务信号

    def set_params(self, start_date, end_date, spatial_tuple, product, version):
        self.start_date = start_date
        self.end_date = end_date
        self.spatial_tuple = spatial_tuple
        self.product = product
        self.version = version

    def run(self):
        """
        多线程功能函数
        :return:
        """
        sp = SearchProduct(self.start_date, self.end_date, self.spatial_tuple, self.product, self.version)
        #  这里需要对qt进行多线程操作， 否则主页面会卡死
        download_url_list = sp.search_product()
        self.my_list.emit(download_url_list)

