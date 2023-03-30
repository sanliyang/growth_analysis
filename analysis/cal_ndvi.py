# -*- coding: utf-8 -*- 
# @Time : 2023/3/29 17:59
# @Author : 施亚林 
# @File : cal_ndvi.py
from osgeo.gdal import Band

from base.c_constant import CConstant


class CalNDVI:
    Valid_Modis_Product_List = [CConstant.Name_Modis_Product_MOD09GQ]

    def __init__(
            self,
            band_nir: Band,
            band_red: Band,
            product_type,
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


    def process(self):
        data_band_nir = self._band_nir.ReadAsArray() * self._scale_factor
        data_band_red = self._band_red.ReadAsArray() * self._scale_factor
        return data_band_nir - data_band_red / data_band_red + data_band_nir
