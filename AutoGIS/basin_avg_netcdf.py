"""读取netcdf文件，计算给定的shapefile代表的范围内该netcdf文件的给定变量的流域平均值"""
import numpy as np
from shapely.geometry import Point, Polygon
from netCDF4 import Dataset


def read_netcdf(file_path):
    """读取netcdf，返回坐标"""
    data_netcdf = Dataset(file_path, 'r')  # reads the netCDF file
    return data_netcdf.dimensions['x'], data_netcdf.dimensions['y']


def create_mask(poly, xs, ys):
    """根据只有一个Polygon的shapefile和一个netcdf文件的所有坐标，生成该shapefile对应的mask。用xy坐标或经纬度都可以，先用xy测试下
       因为netcdf代表的空间太大，所以为了计算较快，直接生成索引比较合适，即取netcdf的变量中的合适点的index"""
    mask_index = []
    for i in len(xs):
        if (is_point_in_boundary(xs[i], ys[i], poly)):
            mask_index.append(i)
    return mask_index


def is_point_in_boundary(px, py, poly):
    """给定一个点的经纬度坐标，判断是否在多多边形边界内
    :param
    polygon--shapely.geometry.Polygon
    """
    point = Point(px, py)
    return point.within(poly)


def calc_avg(mask, daymet_ds):
    """有了mask之后，就可以直接取对应位置的数据了"""
    average_precipitation = 0
    tmax = daymet_ds.variables['tmax'][:]
    # 直接numpy指定位置处的数据求平均
    tmax_chosen = tmax[mask]
    tmax_JJA_mean_comp = np.mean(tmax_chosen, axis=0, keepdims=True)
    return tmax_JJA_mean_comp
