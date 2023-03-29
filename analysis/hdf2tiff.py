# -*- coding: utf-8 -*- 
# @Time : 2023/3/28 15:38
# @Author : 施亚林 
# @File : hdf2tiff.py
import typing

from osgeo import gdal
import os
import glob

from osgeo.gdal import Dataset


class HDF2TIFF:
    def __init__(self, hdf_path):
        self._hdf_datasets: typing.Union[Dataset, None] = None
        self._hdf_path = hdf_path
        self._hdf_sub_datasets = None

    def is_available(self) -> bool:
        return self._hdf_datasets is not None

    def open(self):
        self._hdf_datasets = gdal.Open(self._hdf_path)

    def sub_dataset_count(self):
        return len(self._hdf_datasets.GetSubDatasets())

    def dataset_by_index(self, dataset_index: int):
        return self._hdf_datasets.GetSubDatasets()[dataset_index][0]

    def metadata(self):
        return self._hdf_datasets.GetMetadata()

    def convert_2_tiff(self, dataset_index: typing.Union[int, None], save_path: str):
        if dataset_index is not None:
            data = self.dataset_by_index(dataset_index)
        else:
            pass
        raster_data: Dataset = gdal.Open(data)

        filename = os.path.split(self._hdf_path)[1]
        filename = filename.replace(os.path.splitext(filename)[1], "")

        tifname = "{0}/{1}.tif".format(save_path, filename)

        gdal.Warp(
            tifname,
            raster_data,
            format='GTiff'
        )

    def close(self):
        self._hdf_datasets = None


if __name__ == '__main__':
    conver_obj = HDF2TIFF(r"E:\AT21\csjc\data\hdf\MOD03.A2023082.0155.061.2023082112119.hdf")
    conver_obj.open()
    if conver_obj.is_available():
        conver_obj.convert_2_tiff(0, r"E:\AT21\csjc\data\tiff")
    else:
        print('not available')
    conver_obj.close()
