# -*- coding: utf-8 -*- 
# @Time : 2023/3/29 18:00
# @Author : 施亚林 
# @File : signe_day_image_combine.py
from osgeo import gdal
import numpy as np


class SingeDayImageCombine:

    def __init__(self, tif_file_list, single_tif_name_with_path):
        self.tif_file_list = tif_file_list
        self.single_tif_name_with_path = single_tif_name_with_path

    def merge_tiff(self):

        # 打开第一个文件获取基本信息
        first_file = gdal.Open(self.tif_file_list[0].__str__())
        geotransform = first_file.GetGeoTransform()
        projection = first_file.GetProjection()
        cols = first_file.RasterXSize
        rows = first_file.RasterYSize
        bands = first_file.RasterCount

        # 创建输出文件
        driver = gdal.GetDriverByName('GTiff')
        output_file = driver.Create(self.single_tif_name_with_path, cols, rows, bands, gdal.GDT_Float32)
        output_file.SetGeoTransform(geotransform)
        output_file.SetProjection(projection)

        # 逐个读取输入文件中的数据，并将其写入输出文件
        for i in range(bands):
            band_data = np.zeros((rows, cols))
            for j, input_file in enumerate(self.tif_file_list):
                try:
                    dataset = gdal.Open(input_file.__str__())
                    input_data = dataset.GetRasterBand(i + 1).ReadAsArray()
                except Exception as e:
                    print(e)
                band_data += input_data
            output_file.GetRasterBand(i + 1).WriteArray(band_data)

        # 完成后清理和关闭文件
        output_file.FlushCache()
        output_file = None


if __name__ == '__main__':
    dataset = gdal.Open("D:/grow_anay/growth_analysis/data/download/2023-02-01_2023-02-15_(110, 31, 117, 37)/ndvi_hash/MOD09GQ.A2023032.h26v05.006.2023034025738.tif")
    input_data = dataset.GetRasterBand(1).ReadAsArray()
    print(input_data)
