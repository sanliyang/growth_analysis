# -*- coding: utf-8 -*- 
# @Time : 2023/3/28 15:38
# @Author : 施亚林 
# @File : hdf2tiff.py
import typing

from osgeo import gdal
import os

from osgeo.gdal import Dataset

os.environ['PROJ_LIB'] = r"D:\python_38_2022-9-13\python\Lib\site-packages\pyproj\proj_dir\share\proj"
os.environ['GDAL_DATA'] = r'D:\python_38_2022-9-13\python\Lib\site-packages\pyproj\proj_dir\share'


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

        tif_name = "{0}/{1}_{2}.tif".format(save_path, self.__save_filename(), dataset_index)

        gdal.Translate(
            tif_name,
            raster_data,
            format='GTiff'
        )

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
    conver_obj = HDF2TIFF(r"D:\ss\MOD09GQ.A2023032.h26v05.061.2023034032441.hdf")
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
