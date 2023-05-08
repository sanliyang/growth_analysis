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
        with open("./download/base/token.txt", 'r') as f:
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
    file_url_list = ['https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD09GQ/2023/100/MOD09GQ.A2023100.h22v03.061.2023102040359.hdf', 'https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD09GQ/2023/100/MOD09GQ.A2023100.h23v03.061.2023102034515.hdf', 'https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD09GQ/2023/100/MOD09GQ.A2023100.h24v03.061.2023102040732.hdf', 'https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD09GQ/2023/100/MOD09GQ.A2023100.h24v04.061.2023102034341.hdf', 'https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD09GQ/2023/100/MOD09GQ.A2023100.h25v03.061.2023102035307.hdf', 'https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD09GQ/2023/100/MOD09GQ.A2023100.h25v04.061.2023102044351.hdf', 'https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD09GQ/2023/100/MOD09GQ.A2023100.h25v05.061.2023102040148.hdf', 'https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD09GQ/2023/100/MOD09GQ.A2023100.h26v03.061.2023102041318.hdf', 'https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD09GQ/2023/100/MOD09GQ.A2023100.h26v04.061.2023102032451.hdf', 'https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD09GQ/2023/100/MOD09GQ.A2023100.h26v05.061.2023102035240.hdf', 'https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD09GQ/2023/100/MOD09GQ.A2023100.h26v06.061.2023102034707.hdf', 'https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD09GQ/2023/100/MOD09GQ.A2023100.h27v04.061.2023102034211.hdf', 'https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD09GQ/2023/100/MOD09GQ.A2023100.h27v05.061.2023102050757.hdf', 'https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD09GQ/2023/100/MOD09GQ.A2023100.h27v06.061.2023102053301.hdf', 'https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD09GQ/2023/100/MOD09GQ.A2023100.h28v04.061.2023102033501.hdf', 'https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD09GQ/2023/100/MOD09GQ.A2023100.h28v05.061.2023102035953.hdf', 'https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD09GQ/2023/100/MOD09GQ.A2023100.h28v06.061.2023102040734.hdf', 'https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD09GQ/2023/100/MOD09GQ.A2023100.h29v05.061.2023102040320.hdf', 'https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD09GQ/2023/100/MOD09GQ.A2023100.h29v06.061.2023102043950.hdf', 'https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD09GQ/2023/100/MOD09GQ.A2023100.h30v06.061.2023102034341.hdf']
    time_start_date = "2023-04-10"
    time_end_date = "2023-04-10"
    spatial_tuple = (96, 54, 136, 23)
    for file_url in file_url_list:
        dp.download_file(file_url, time_start_date, time_end_date, spatial_tuple)
