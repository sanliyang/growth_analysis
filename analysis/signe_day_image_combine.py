# -*- coding: utf-8 -*- 
# @Time : 2023/3/29 18:00
# @Author : 施亚林 
# @File : signe_day_image_combine.py
import os.path
from osgeo import gdal, osr
import numpy as np


class SingeDayImageCombine:

    def __init__(self, tif_file_list, single_tif_name_with_path):
        self.tif_file_list = tif_file_list
        self.single_tif_name_with_path = single_tif_name_with_path
        self.no_cut_image = os.path.join(os.path.dirname(self.single_tif_name_with_path),
                                         ("nocut" + os.path.basename(self.single_tif_name_with_path)))

    def merge_tiff(self):
        tif_file_set = []
        for tif_file in self.tif_file_list:
            tif_file_set.append(tif_file.__str__())

        gdal.Warp(self.no_cut_image, tif_file_set)

    def cut_tif(self):
        # 定义裁剪区域的四至坐标
        xmin, ymin, xmax, ymax = (96, 54, 136, 23)  # 例如，这里是以0,0为左上角，100,100为右下角的裁剪区域

        # 读取输入影像的信息
        ds = gdal.Open(self.no_cut_image)
        geo_transform = ds.GetGeoTransform()
        projection = ds.GetProjection()

        # 计算输出影像的大小
        ulx, uly = gdal.ApplyGeoTransform(geo_transform, xmin, ymax)
        lrx, lry = gdal.ApplyGeoTransform(geo_transform, xmax, ymin)
        x_res = int(round((lrx - ulx) / geo_transform[1]))
        y_res = int(round((uly - lry) / -geo_transform[5]))
        # 设置Warp参数
        warp_options = gdal.WarpOptions(cutlineDSName=None,
                                        outputBounds=[xmin, ymin, xmax, ymax],
                                        outputBoundsSRS=projection,
                                        xRes=geo_transform[1],
                                        yRes=-geo_transform[5],
                                        dstSRS=projection,
                                        resampleAlg=gdal.GRA_NearestNeighbour)
        # 执行裁剪
        gdal.Warp(self.single_tif_name_with_path, ds, options=warp_options)

        # 关闭数据集
        ds = None

        os.remove(self.no_cut_image)


if __name__ == '__main__':
    dataset = gdal.Open(
        "D:/grow_anay/growth_analysis/data/download/2023-02-01_2023-02-15_(110, 31, 117, "
        "37)/ndvi_hash/MOD09GQ.A2023032.h26v05.006.2023034025738.tif")
    input_data = dataset.GetRasterBand(1).ReadAsArray()
    print(input_data)
