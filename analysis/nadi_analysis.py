# -*- coding: utf-8 -*- 
# @Time : 2023/3/29 17:59
# @Author : 施亚林 
# @File : nadi_analysis.py
import numpy as np
from base.c_constant import CConstant
from osgeo import gdal
import os

os.environ['PROJ_LIB'] = r"D:\grow_anay\python\Lib\site-packages\pyproj\proj_dir\share\proj"
os.environ['GDAL_DATA'] = r'D:\grow_anay\python\Lib\site-packages\pyproj\proj_dir\share'


class NDVIAnalysis(CConstant):

    def __init__(self, nir_file, red_file, output_path):
        self.nir_file = nir_file
        self.red_file = red_file
        self.output_path = output_path

    def extract_ndvi_2_tif(self):
        # 读取Tiff影像数据
        image_ds = gdal.Open(self.red_file)
        image = np.array(image_ds.GetRasterBand(1).ReadAsArray())

        image_ds1 = gdal.Open(self.nir_file)
        image1 = np.array(image_ds.GetRasterBand(1).ReadAsArray())

        # 获取红波段和近红外波段
        red = image_ds.GetRasterBand(1).ReadAsArray().astype(np.float32)
        nir = image_ds1.GetRasterBand(1).ReadAsArray().astype(np.float32)

        # 移除无效值和填充值
        valid_pixels = np.logical_and(red > 0, nir > 0)
        ndvi = np.zeros_like(red)
        ndvi[valid_pixels] = (nir[valid_pixels] - red[valid_pixels]) / (nir[valid_pixels] + red[valid_pixels])
        ndvi = ndvi * self.Modis_Scale_Factor_MOD09GQ

        # 将NDVI保存为Tiff影像
        driver = gdal.GetDriverByName("GTiff")
        file_name = os.path.basename(self.red_file).split("_")[0]
        # output_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "single_ndvi")
        output_file = os.path.join(self.output_path, f"{file_name}")
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)
        output_ds = driver.Create(output_file, image_ds.RasterXSize, image_ds.RasterYSize, 1, gdal.GDT_Float32)
        output_ds.SetProjection(image_ds.GetProjection())
        output_ds.SetGeoTransform(image_ds.GetGeoTransform())
        output_band = output_ds.GetRasterBand(1)

        # 设置无效值和填充值
        # output_band.SetNoDataValue(0)
        # output_band.Fill(0)

        # 将NDVI写入Tiff影像
        output_band.WriteArray(ndvi)
        output_ds.FlushCache()

        # 释放资源
        output_band = None
        output_ds = None
        image_ds = None
        image_ds1 = None


if __name__ == '__main__':
    red_file = r"D:\工具\MOD09GQ.A2023032.h26v05.061.2023034032441_sur_refl_b01_1.tif"
    nir_file = r"D:\工具\MOD09GQ.A2023032.h26v05.061.2023034032441_sur_refl_b02_1.tif"

    na = NDVIAnalysis(nir_file, red_file, "aaa")
    na.extract_ndvi_2_tif()
