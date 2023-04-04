# -*- coding: utf-8 -*- 
""" ++++++++++++++++++++++++++++++++++++++
@product->name PyCharm
@project->name growth_analysis
@editor->name Sanliy
@file->name download_product.py
@create->time 2023/3/29-10:29
@desc->
++++++++++++++++++++++++++++++++++++++ """
import os.path

import requests


class DownloadProduct:
    def __init__(self):
        self.token = None
        self.headers = None

    def get_token(self):
        with open('D:/grow_anay/growth_analysis/download/base/token.txt', 'r') as f:
            self.token = f.read()

    def set_headers(self):
        self.headers = {
            "Authorization": "Bearer " + self.token
        }

    def download_file(self, file_url):
        print(file_url)
        file_path = "D:/工具"
        session = requests.Session()
        resp = session.get(url=file_url, headers=self.headers)
        file_size = resp.headers.get("Content-Length")
        print(file_size)
        file_name = file_url.split("/")[-1]
        file_name_with_path = os.path.join(file_path, file_name)

        with open(file_name_with_path, 'ab') as code:
            for chunk in resp.iter_content(chunk_size=1024):
                if chunk:
                    code.write(chunk)
                    code.flush()
        session.close()
        return file_name


if __name__ == '__main__':
    dp = DownloadProduct()
    dp.get_token()
    dp.set_headers()
    dp.download_file(
        "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD03/2023/032/MOD03.A2023032.0210.061.2023032150218.hdf")
