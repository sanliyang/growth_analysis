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

    def __init__(self):
        self.token = None
        self.search_url = "https://ladsweb.modaps.eosdis.nasa.gov/api/v1/products/excludeBrowse=true"
        self.base_url = "https://ladsweb.modaps.eosdis.nasa.gov/api/v1/files"
        self.time_start_date = "2023-02-01"
        self.time_end_date = "2023-02-15"
        self.spatial_tuple = (110, 31, 117, 37)
        self.product = 'MOD35_L2'

    def search_product(self):
        time_start_date = "2023-02-01"
        time_end_date = "2023-02-15"
        spatial_tuple = (110, 31, 117, 37)
        product = 'MOD35_L2'
        session = requests.Session()
        rp = session.get(url=self.search_url)
        if rp.status_code == 200:
            rp_list = json.loads(rp.text)
            for rp in rp_list:
                esdt = rp['ESDT']
                if esdt == product:
                    col = rp['collections'][0]
                    search_end_url = f'/product={product}&collection={col}' \
                                     f'&dateRanges={time_start_date}..{time_end_date}&areaOfInterest' \
                                     f'=x{spatial_tuple[0]}y{spatial_tuple[1]},x{spatial_tuple[2]}y{spatial_tuple[3]}' \
                                     f'&dayCoverage=true&dnboundCoverage=true'
                    search_url = self.base_url + search_end_url

                    print(search_url)

                    rp_d = session.get(search_url)
                    if rp_d.text is not None:
                        rps_d_dict = json.loads(rp_d.text)
                        if len(rps_d_dict) != 0:
                            for rp_d_dict in rps_d_dict.values():
                                fileurl = rp_d_dict['fileURL']
                                down_url = 'https://ladsweb.modaps.eosdis.nasa.gov' + fileurl
                                print(down_url)
        session.close()


if __name__ == '__main__':
    sp = SearchProduct()
    sp.search_product()
