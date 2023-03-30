# -*- coding: utf-8 -*- 
# @Time : 2023/3/29 17:59
# @Author : 施亚林 
# @File : nadi_analysis.py
from osgeo.gdal import Band

from base.c_constant import CConstant


class NDVIAnalysis:
    Valid_Modis_Product_List = [CConstant.Name_Modis_Product_MOD09GQ]

    def __init__(
            self,
            band_nir: Band,
            band_red: Band,
            product_type,
            x_size: int,
            y_size: int,
            scale_factor: float = None,
            force=False,
            **options
    ):

        if product_type not in self.Valid_Modis_Product_List and not force:
            raise TypeError('Modis[{0}]产品，不支持计算NDVI'.format(product_type))

        self._options = options
        self._product_type = product_type
        self._band_nir = band_nir
        self._band_red = band_red
        self._x_size = x_size
        self._y_size = y_size
        if scale_factor is None:
            self._scale_factor = getattr(CConstant, 'Modis_Scale_Factor_{0}'.format(self._product_type), 1)
        else:
            self._scale_factor = scale_factor

        # pixel_value
        self._p_val_valid_range_max = getattr(
            CConstant,
            'Modis_{0}_Valid_Range_Max'.format(self._product_type),
            self._options.get(CConstant.Name_Modis_Valid_Range_Max, None)
        )
        self._p_val_valid_range_min = getattr(
            CConstant,
            'Modis_{0}_Valid_Range_Min'.format(self._product_type),
            self._options.get(CConstant.Name_Modis_Valid_Range_Min, None)
        )

        self._fill_value = getattr(
            CConstant,
            'Modis_{0}_Fill_Value'.format(self._product_type),
            self._options.get(CConstant.Name_Modis_Fill_Value, None)
        )
        self._no_data = getattr(
            CConstant,
            'Modis_{0}_OutPut_NoData_Value'.format(self._product_type),
            self._options.get(CConstant.Modis_MOD09GQ_OutPut_NoData_Value, 0)
        )

    def convert_nodata(self, np_arr):
        """
        根据相应产品的成果NODATA值与官方的NODATA值进行转换
        :return:
        """
        np_arr[
            (np_arr < self._p_val_valid_range_min) |
            (np_arr > self._p_val_valid_range_max) |
            (np_arr == self._fill_value)
            ] = self._no_data

    def calculation(self, band_nir_np_array, band_red_np_array):
        """
        根据转换后NODATA值的近红外与红外波段对应numpy数组，计算出NDVI数据
        :return:
        """
        # todo 不同numpy数组满足指定条件元素的计算
        np_arr_band_nir_valid = band_nir_np_array[
            (band_nir_np_array >= self._p_val_valid_range_min) &
            (band_nir_np_array <= self._p_val_valid_range_max) &
            (band_nir_np_array != self._fill_value)
            ]

        np_arr_band_red_valid = band_red_np_array[
            (band_red_np_array >= self._p_val_valid_range_min) &
            (band_red_np_array <= self._p_val_valid_range_max) &
            (band_red_np_array != self._fill_value)
            ]

        a = (np_arr_band_nir_valid - np_arr_band_red_valid) / (np_arr_band_nir_valid + np_arr_band_red_valid)
        return a

    def process(self):
        # NDVI=（NIR-R）/（NIR+R）,NIR:近红外波段,R：红外波段

        np_arr_band_nir = self._band_nir.ReadAsArray(0, 0, self._x_size, self._y_size)
        np_app_band_red = self._band_red.ReadAsArray(0, 0, self._x_size, self._y_size)

        self.convert_nodata(np_arr_band_nir)
        self.convert_nodata(np_app_band_red)

        self.calculation(np_arr_band_nir, np_app_band_red)


if __name__ == '__main__':
    from osgeo import gdal

    data = gdal.Open(r"E:\AT21\csjc\data\tiff\MOD09GQ.A2023074.h26v04.061.2023076040141_sur_refl_b01_1.tif")
    x_size = data.RasterXSize
    y_size = data.RasterYSize
    band_r = data.GetRasterBand(1)

    obj = NDVIAnalysis(
        band_r,
        band_r,
        CConstant.Name_Modis_Product_MOD09GQ,
        x_size, y_size
    )
    obj.process()
