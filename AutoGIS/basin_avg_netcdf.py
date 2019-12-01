"""读取netcdf文件，计算给定的shapefile代表的范围内该netcdf文件的给定变量的流域平均值
算法需要优化：
1.判断区域那块，可以根据bound迅速地排除大部分不需要判断的点，只判断在bound内的点
2.其他的优化和shp_trans_coord下的差不多
"""
import numpy as np
from shapely.geometry import Point, Polygon
from netCDF4 import Dataset
import os
import geopandas as gpd


def create_mask(poly, lons, lats):
    """根据只有一个Polygon的shapefile和一个netcdf文件的所有坐标，生成该shapefile对应的mask。用xy坐标或经纬度都可以，先用经纬度测试下
       因为netcdf代表的空间太大，所以为了计算较快，直接生成索引比较合适，即取netcdf的变量中的合适点的index"""
    mask_index = []
    # 首先想办法减少循环的范围，然后在循环内使用map实现快速循环，现在思路是这样的：
    # 1.首先对poly的中心进行判断，利用二分法，尽快地找到索引号，经纬度分开查，这样一下数量就降下来了。
    # 2.然后再对poly用bound判断范围，再在这个范围内寻找即可。
    for i in range(lons.shape[0]):
        for j in range(lons.shape[1]):
            if is_point_in_boundary(lons[i][j], lats[i][j], poly):
                mask_index.append((i, j))
    return mask_index


def is_point_in_boundary(px, py, poly):
    """给定一个点的经纬度坐标，判断是否在多多边形边界内
    :param
    polygon--shapely.geometry.Polygon
    """
    point = Point(px, py)
    return point.within(poly)


def calc_avg(mask, netcdf_data, var_type):
    """有了mask之后，就可以直接取对应位置的数据了，mask是一个包含二维tuple的list"""
    # var_data是一个三维的数组，要看看var_data的时间变量是第几个维度，利用mask的数据搜索另外两维
    var_data = netcdf_data.variables[var_type][:]
    # 直接numpy指定位置处的数据求平均
    mask = np.array(mask)
    index = mask.T
    data_chosen = var_data[0][index[0], index[1]]
    data_mean = np.mean(data_chosen, axis=0)
    return data_mean


# 先读取一个netcdf文件，然后把shapefile选择一张，先测试下上面的程序。
# Define path to folder，以r开头表示相对路径
input_folder = r"examples_data"

# Join folder path and filename
netcdf_file = "daymet_v3_prcp_1980_na.nc4"

file_path = os.path.join(input_folder, netcdf_file)

data_netcdf = Dataset(file_path, 'r')  # reads the netCDF file

shp_file = os.path.join(input_folder, "03144816.shp")

# crs_final_str = '+proj=lcc +lat_1=25 +lat_2=60 +lat_0=42.5 +lon_0=-100 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs'
crs_final_str = '+proj=longlat +datum=WGS84 +no_defs'

# 先选择一个shpfile
new_shps = gpd.read_file(shp_file)

lons = data_netcdf.variables['lon'][:]
lats = data_netcdf.variables['lat'][:]
polygon = new_shps.at[0, 'geometry']
mask = create_mask(polygon, lons, lats)

var_types = ['prcp']
# var_types = ['tmax', 'tmin', 'prcp', 'srad', 'vp', 'swe', 'dayl']

for var_type in var_types:
    avg = calc_avg(mask, data_netcdf, var_type)
