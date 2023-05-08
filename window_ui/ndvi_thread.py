# -*- coding: utf-8 -*- 
""" ++++++++++++++++++++++++++++++++++++++
@product->name PyCharm
@project->name growth_analysis
@editor->name Sanliy
@file->name ndvi_thread.py
@create->time 2023/4/19-17:50
@desc->
++++++++++++++++++++++++++++++++++++++ """
from PyQt5.QtCore import QThread, pyqtSignal

import os
from analysis.ndvi_combination import NdviCombination

class NdviThread(QThread):

    def __init__(self):
        super().__init__()
        self.area = None
        self.start_date = None
        self.end_date = None

    my_str = pyqtSignal(str)  # 创建任务信号

    def set_params(self, start_date, end_date, area):
        self.start_date = start_date
        self.end_date = end_date
        self.area = area

    def run(self):
        """
        多线程功能函数
        :return:
        """
        hdf_path = os.path.join(
            os.path.dirname(
                os.path.dirname(__file__)
            ),
            "data",
            "download",
            f"{self.start_date}_{self.end_date}_{self.area}",
            "hdf"
        )

        nc = NdviCombination(hdf_path)
        nc.hdf_conversion_tif()
        nc.tif_conversion_ndvi()
        nc.ndvi_combination()
        self.my_str.emit("所有ndvi均已计算完成！")

