# -*- coding: utf-8 -*- 
""" ++++++++++++++++++++++++++++++++++++++
@product->name PyCharm
@project->name growth_analysis
@editor->name Sanliy
@file->name ndvi_combination.py
@create->time 2023/4/13-15:58
@desc->
++++++++++++++++++++++++++++++++++++++ """
import os.path
import pathlib
from analysis.nadi_analysis import NDVIAnalysis
from osgeo import gdal
from osgeo.gdal import Dataset
from utils.hdf2tiff import HDF2TIFF
from signe_day_image_combine import SingeDayImageCombine


class NdviCombination:

    def __init__(self, hdf_path):
        self.hdf_path = hdf_path
        self.tif_nir = None
        self.tif_red = None
        self.ndvi_hash = None

    def hdf_conversion_tif(self):
        tif_split = os.path.dirname(self.hdf_path)
        self.tif_nir = os.path.join(tif_split, "tif_nir")
        self.tif_red = os.path.join(tif_split, "tif_red")

        if not os.path.exists(self.tif_nir):
            os.makedirs(self.tif_nir)

        if not os.path.exists(self.tif_red):
            os.makedirs(self.tif_red)

        hdf_list = list(pathlib.Path(self.hdf_path).glob("*"))
        for hdf_file in hdf_list:
            conver_obj = HDF2TIFF(hdf_file.__str__())
            conver_obj.open()
            nir = conver_obj.dataset_by_name('sur_refl_b02_1')
            r = conver_obj.dataset_by_name('sur_refl_b01_1')

            if nir is not None:
                nir: Dataset = gdal.Open(nir)
                print(nir.ReadAsArray())
            if r is not None:
                r = gdal.Open(r)
            if conver_obj.is_available():
                conver_obj.convert_2_tiff('sur_refl_b02_1', self.tif_nir)
                conver_obj.convert_2_tiff('sur_refl_b01_1', self.tif_red)
            else:
                print('not available')
            conver_obj.close()

    def tif_conversion_ndvi(self):

        red_file_list = list(pathlib.Path(self.tif_red).glob("*"))
        self.ndvi_hash = os.path.join(os.path.dirname(self.hdf_path), "ndvi_hash")
        if not os.path.exists(self.ndvi_hash):
            os.makedirs(self.ndvi_hash)

        for red_file in red_file_list:
            red_file_name_with_suffix = pathlib.Path(red_file).name
            nir_file = os.path.join(self.tif_nir, red_file_name_with_suffix)
            na = NDVIAnalysis(nir_file, red_file.__str__(), self.ndvi_hash)
            na.extract_ndvi_2_tif()

    def ndvi_combination(self):
        ndvi_hash_file_list = list(pathlib.Path(self.ndvi_hash).glob("*"))
        # 判断输出文件所在文件夹是否存在，同时需要对输出文件的名字进行确认
        root_path = os.path.dirname(self.hdf_path)
        root_path_name = pathlib.Path(root_path).name

        single_ndvi_path = os.path.join(root_path, "single_ndvi")
        if not os.path.exists(single_ndvi_path):
            os.makedirs(single_ndvi_path)

        single_ndvi_file_path_with_name = os.path.join(single_ndvi_path, root_path_name)
        single_ndvi_file_path_with_name_with_suffix = f"{single_ndvi_file_path_with_name}.tif"

        # todo 这里进行单天分批次进行计算并处理

        sdic = SingeDayImageCombine(ndvi_hash_file_list, single_ndvi_file_path_with_name_with_suffix)
        sdic.merge_tiff()


if __name__ == '__main__':
    hdf_path = r"D:\grow_anay\growth_analysis\data\download\2023-02-01_2023-02-15_(110, 31, 117, 37)\hdf"

    nc = NdviCombination(hdf_path)
    nc.hdf_conversion_tif()
    nc.tif_conversion_ndvi()
    nc.ndvi_combination()
