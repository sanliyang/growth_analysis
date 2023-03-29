# -*- coding: utf-8 -*- 
""" ++++++++++++++++++++++++++++++++++++++
@product->name PyCharm
@project->name growth_analysis
@editor->name Sanliy
@file->name get_access_token.py
@create->time 2023/3/29-10:28
@desc->
++++++++++++++++++++++++++++++++++++++ """
import json

import requests


class GetAccessToken:

    def __init__(self):
        self.url = "https://ladsweb.modaps.eosdis.nasa.gov/search/"
        self.username = "xx"
        self.password = "xx"

    def login(self):
        ...

