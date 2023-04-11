# -*- coding: utf-8 -*- 
# @Time : 2023/3/29 18:00
# @Author : 施亚林 
# @File : signe_day_image_combine.py
from osgeo import gdal


class SingeDayImageCombine:

    def merge_tiff(self):
        # 打开所有要合并的TIFF文件
        files_to_merge = ["image1.tiff", "image2.tiff", "image3.tiff"]
        src_files_to_mosaic = []
        for file in files_to_merge:
            src = gdal.Open(file)
            src_files_to_mosaic.append(src)

        # 获取输入TIFF文件的基础信息
        src_proj = src_files_to_mosaic[0].GetProjection()
        src_geotrans = src_files_to_mosaic[0].GetGeoTransform()
        x_min = src_geotrans[0]
        y_max = src_geotrans[3]
        x_max = x_min + src_files_to_mosaic[0].RasterXSize * src_geotrans[1]
        y_min = y_max + src_files_to_mosaic[0].RasterYSize * src_geotrans[5]

        # 计算输出TIFF文件的大小
        pixel_size = src_geotrans[1]
        target_ds = gdal.GetDriverByName('GTiff').Create("merged.tiff", int((x_max - x_min) / pixel_size),
                                                         int((y_max - y_min) / pixel_size), len(src_files_to_mosaic),
                                                         gdal.GDT_Float32)

        # 将所有输入TIFF文件写入输出TIFF文件中
        for i in range(len(src_files_to_mosaic)):
            gdal.Warp(target_ds, src_files_to_mosaic[i], dstSRS=src_proj, format="VRT",
                      outputBounds=[x_min, y_min, x_max, y_max], srcNodata=0, dstNodata=0, multithread=True)

        # 关闭文件
        target_ds = None
