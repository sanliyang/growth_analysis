# -*- coding: utf-8 -*- 
# @Time : 2023/3/28 15:38
# @Author : 施亚林 
# @File : hdf2tiff.py
import numpy as np

import typing

from osgeo import gdal, osr
import os

from osgeo.gdal import Dataset

os.environ['PROJ_LIB'] = "./share/proj4"
os.environ['GDAL_DATA'] = './share'


class HDF2TIFF:
    def __init__(self, hdf_path):
        self._hdf_datasets: typing.Union[Dataset, None] = None
        self._hdf_path = hdf_path
        self._hdf_sub_datasets = None

    def is_available(self) -> bool:
        return self._hdf_datasets is not None

    def open(self):  # sourcery skip: raise-specific-error
        self._hdf_datasets = gdal.Open(self._hdf_path)
        if self._hdf_datasets is None:
            raise Exception("文件[{0}]打开失败".format(self._hdf_path))

        self._hdf_sub_datasets = self._hdf_datasets.GetSubDatasets()

    def sub_dataset_count(self):
        return len(self._hdf_sub_datasets)

    def dataset_name_by_index(self, dataset_index: int):
        if dataset_index < self.sub_dataset_count():
            return self._hdf_sub_datasets.GetSubDatasets()[dataset_index].split(":")[-1]
        else:
            return None

    def dataset_by_index(self, dataset_index: int):
        if dataset_index < self.sub_dataset_count():
            return self._hdf_datasets.GetSubDatasets()[dataset_index][0]
        else:
            return None

    def dataset_by_name(self, dataset_name: str, fuzzy_search=False):
        for subdataset in self._hdf_sub_datasets:
            dset_name = subdataset[0].split(":")[-1]
            if fuzzy_search:
                if dset_name.lower().find(dataset_name.lower()):
                    return subdataset[0]
            elif dset_name.lower() == dataset_name.lower():
                return subdataset[0]
        return None

    def metadata(self):
        return self._hdf_datasets.GetMetadata()

    def __save_filename(self):
        filename = os.path.split(self._hdf_path)[1]
        filename = filename.replace(os.path.splitext(filename)[1], "")
        return filename

    def _single_sub_dataset_2_tiff(self, dataset_index: typing.Union[int, str], save_path: str):
        if isinstance(dataset_index, int):
            data = self.dataset_by_index(dataset_index)
        elif isinstance(dataset_index, str):
            data = self.dataset_by_name(dataset_index)
        else:
            raise Exception('获取子数据集[{0}]失败'.format(dataset_index))

        raster_data: Dataset = gdal.Open(data)

        tif_name = "{0}/{1}.tif".format(save_path, self.__save_filename())

        # gdal.Translate(
        #     tif_name,
        #     raster_data,
        #     format='GTiff'
        # )

        # gdal.Warp(tif_name, raster_data, dstSRS='EPSG:4326', dstNodata=np.nan, options=['DST_METHOD=NO_GEOTRANSFORM'])

        # 重投影
        # 定义源坐标参考系统和目标坐标参考系统
        src_srs = osr.SpatialReference()
        src_srs.ImportFromWkt(raster_data.GetProjection())
        tgt_srs = osr.SpatialReference()
        tgt_srs.ImportFromEPSG(4326)

        # 获取输入文件的投影和变换信息
        src_geotransform = raster_data.GetGeoTransform()

        # 创建 warped VRT
        warped_vrt = gdal.AutoCreateWarpedVRT(raster_data, None, tgt_srs.ExportToWkt(), gdal.GRA_Bilinear)

        # 获取输出图像的大小和变换信息
        cols = warped_vrt.RasterXSize
        rows = warped_vrt.RasterYSize
        tgt_geotransform = warped_vrt.GetGeoTransform()

        # 创建输出数据集
        driver = gdal.GetDriverByName("GTiff")
        output_dataset = driver.Create(tif_name, cols, rows, raster_data.RasterCount,
                                       raster_data.GetRasterBand(1).DataType)

        # 设置输出数据集的投影和变换信息
        output_dataset.SetGeoTransform(tgt_geotransform)
        output_dataset.SetProjection(tgt_srs.ExportToWkt())

        # 执行重投影
        gdal.ReprojectImage(raster_data, output_dataset, src_srs.ExportToWkt(), tgt_srs.ExportToWkt(),
                            gdal.GRA_Bilinear)

        # 关闭数据集
        raster_data = None
        output_dataset = None

    def convert_2_tiff(self, dataset_index: typing.Union[int, None, str], save_path: str):
        if dataset_index is not None:
            self._single_sub_dataset_2_tiff(dataset_index, save_path)
        else:
            for index in range(self.sub_dataset_count()):
                data = self.dataset_by_index(index)
                # 等待需求确定，再确定是否编写，多波段tif与HDF数据集对应的转换

    def close(self):
        self._hdf_datasets = None


if __name__ == '__main__':
    output_path = ""
    conver_obj = HDF2TIFF(r"D:\ss\hdf\MOD09GQ.A2023032.h26v05.061.2023034032441.hdf")
    conver_obj.open()
    nir = conver_obj.dataset_by_name('sur_refl_b02_1')
    r = conver_obj.dataset_by_name('sur_refl_b01_1')

    if nir is not None:
        nir: Dataset = gdal.Open(nir)
        print(nir.ReadAsArray())
    if r is not None:
        r = gdal.Open(r)
    if conver_obj.is_available():
        conver_obj.convert_2_tiff('sur_refl_b02_1', r"D:\工具")
        conver_obj.convert_2_tiff('sur_refl_b01_1', r"D:\工具")
    else:
        print('not available')
    conver_obj.close()
