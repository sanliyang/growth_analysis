# -*- coding: utf-8 -*- 
""" ++++++++++++++++++++++++++++++++++++++
@product->name PyCharm
@project->name growth_analysis
@editor->name Sanliy
@file->name search_product.py
@create->time 2023/3/29-10:29
@desc->
++++++++++++++++++++++++++++++++++++++ """
import json

import requests


class SearchProduct:

    def __init__(self, time_start_date, time_end_date, spatial_tuple, product):
        self.token = None
        self.search_url = "https://ladsweb.modaps.eosdis.nasa.gov/api/v1/products/excludeBrowse=true"
        self.base_url = "https://ladsweb.modaps.eosdis.nasa.gov/api/v1/files"
        self.download_base_url = "https://ladsweb.modaps.eosdis.nasa.gov"
        self.time_start_date = time_start_date
        self.time_end_date = time_end_date
        self.spatial_tuple = spatial_tuple
        self.product = product

    def search_product(self):
        print("开始检索喽...")
        download_url = []
        session = requests.Session()
        rp = session.get(url=self.search_url)
        print("1")
        if rp.status_code == 200:
            rp_list = json.loads(rp.text)
            for rp in rp_list:
                print("2")
                esdt = rp['ESDT']
                # esdt = rp["MODIS:TERRA"]
                print(esdt)
                print(self.product)
                if esdt == self.product:
                    col = rp['collections'][0]
                    search_end_url = f'/product={self.product}&collection={col}' \
                                     f'&dateRanges={self.time_start_date}..{self.time_end_date}&areaOfInterest' \
                                     f'=x{self.spatial_tuple[0]}y{self.spatial_tuple[1]},x{self.spatial_tuple[2]}y' \
                                     f'{self.spatial_tuple[3]}&dayCoverage=true&dnboundCoverage=true'
                    print(search_end_url)
                    search_url = self.base_url + search_end_url
                    rp_d = session.get(search_url)
                    if rp_d.text is not None:
                        rps_d_dict = json.loads(rp_d.text)
                        if len(rps_d_dict) != 0:
                            for rp_d_dict in rps_d_dict.values():
                                fileurl = rp_d_dict['fileURL']
                                down_url = self.download_base_url + fileurl
                                download_url.append(down_url)
        session.close()

        print(download_url)
        return download_url


if __name__ == '__main__':
    time_start_date = "2023-02-01"
    time_end_date = "2023-02-15"
    spatial_tuple = (110, 31, 117, 37)
    product = 'MOD35_L2'
    sp = SearchProduct(time_start_date, time_end_date, spatial_tuple, product)
    sp.search_product()
