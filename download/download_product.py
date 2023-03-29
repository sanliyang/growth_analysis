# -*- coding: utf-8 -*- 
""" ++++++++++++++++++++++++++++++++++++++
@product->name PyCharm
@project->name growth_analysis
@editor->name Sanliy
@file->name download_product.py
@create->time 2023/3/29-10:29
@desc->
++++++++++++++++++++++++++++++++++++++ """


class DownloadProduct:
    def __init__(self):
        self.token = None

    def get_token(self):
        with open('./base/token.txt', 'r') as f:
            self.token = f.read()
