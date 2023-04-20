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
        with open(r"D:\grow_anay\growth_analysis\download\base\token.txt", 'r') as f:
            self.token = f.read()

    def set_headers(self):
        self.headers = {
            "Authorization": "Bearer " + self.token
        }

    def download_file(self, file_url, start_date, end_date, area):
        print(file_url)
        file_path = os.path.join(
            os.path.dirname(
                os.path.dirname(__file__)
            ),
            "data",
            "download",
            f"{start_date}_{end_date}_{area}",
            "hdf"
        )
        if not os.path.exists(file_path):
            os.makedirs(file_path)
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


if __name__ == '__main__':
    dp = DownloadProduct()
    dp.get_token()
    dp.set_headers()
    file_url_list = [
            'https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD35_L2/2023/033/MOD35_L2.A2023033.0250.061.2023033131723.hdf'
        ]
    time_start_date = "2023-02-01"
    time_end_date = "2023-02-15"
    spatial_tuple = (110, 31, 117, 37)
    for file_url in file_url_list:
        dp.download_file(file_url, time_start_date, time_end_date, spatial_tuple)
