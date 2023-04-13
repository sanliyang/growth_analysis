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


class NdviCombination:

    def __init__(self, hdf_path):
        self.hdf_path = hdf_path
        self.tif_nir = None
        self.tif_red = None

    def hdf_conversion_tif(self):
        tif_split = os.path.dirname(self.hdf_path)
        self.tif_nir = os.path.join(tif_split, "tif_nir")
        self.tif_red = os.path.join(tif_split, "tif_red")

        if os.path.exists(self.tif_nir):
            os.makedirs(self.tif_nir)

        if os.path.exists(self.tif_red):
            os.makedirs(self.tif_red)

        hdf_list = list(pathlib.Path(self.hdf_path).glob("*"))
        for hdf_file in hdf_list:
            conver_obj = HDF2TIFF(hdf_file)
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


        red_file = r"D:\工具\MOD09GQ.A2023032.h26v05.061.2023034032441_sur_refl_b01_1.tif"
        nir_file = r"D:\工具\MOD09GQ.A2023032.h26v05.061.2023034032441_sur_refl_b02_1.tif"
        output_path = ""

        na = NDVIAnalysis(nir_file, red_file, output_path)
        na.extract_ndvi_2_tif()

    def ndvi_combination(self):
        ...


if __name__ == '__main__':
    hdf_path = r"D:\growth\data\download\2023-03-10_2023-03-10\hdf"

    nc = NdviCombination(hdf_path)
    nc.hdf_conversion_tif()