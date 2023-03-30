# -*- coding: utf-8 -*- 
# @Time : 2023/3/29 17:52
# @Author : 施亚林 
# @File : c_constant.py
class CConstant:
    """
    常用常量类
    """

    # MODIS 产品名称
    Name_Modis_Product_MOD09GQ = 'MOD09GQ'
    Name_Modis_Product_MOD03 = 'MOD03'
    Name_Modis_Product_MOD35_L2 = 'MOD35_L2'
    Name_Modis_Valid_Range_Max = 'Modis_Valid_Range_Max'
    Name_Modis_Valid_Range_Min = 'Modis_Valid_Range_Min'
    Name_Modis_Fill_Value = 'Modis_Fill_Value'

    # MODIS MOD09GQ参数
    Modis_Scale_Factor_MOD09GQ = 0.0001  # 比例因子
    Modis_MOD09GQ_Valid_Range_Max = 16000  # 像元最大有效值
    Modis_MOD09GQ_Valid_Range_Min = -100  # 像元最小有效值
    Modis_MOD09GQ_Fill_Value = -28672  # 栅格填充值
    Modis_MOD09GQ_OutPut_NoData_Value = 0  # MOD09GQ 计算为NDVI时的nodata值
