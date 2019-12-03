"""读取netcdf文件，计算给定的shapefile代表的范围内该netcdf文件的给定变量的流域平均值
算法需要优化：
1.判断区域那块，可以根据bound迅速地排除大部分不需要判断的点，只判断在bound内的点
2.其他的优化和shp_trans_coord下的差不多
"""
import time

import numpy as np
from shapely.geometry import Point, Polygon
from netCDF4 import Dataset
import os
import geopandas as gpd

from pyproj import CRS
from pyproj import transform


def nearest_point_index(crs_from, crs_to, lon, lat, xs, ys):
    # x和y是投影坐标，lon, lat需要先转换一下，注意x是代表经度投影，y是纬度投影
    x, y = transform(crs_from, crs_to, lon, lat)
    index_x = (np.abs(xs - x)).argmin()
    index_y = (np.abs(ys - y)).argmin()
    return [index_x, index_y]


def create_mask(poly, xs, ys, lons, lats, crs_from, crs_to):
    """根据只有一个Polygon的shapefile和一个netcdf文件的所有坐标，生成该shapefile对应的mask。用xy坐标或经纬度都可以，先用经纬度测试下
       因为netcdf代表的空间太大，所以为了计算较快，直接生成索引比较合适，即取netcdf的变量中的合适点的index"""
    mask_index = []
    # 首先想办法减少循环的范围，然后在循环内使用map实现快速循环，现在思路是这样的：
    # 每行选出一个最接近的index组成一个INDEX集合，首先读取bound的范围，转换到x和y上判断范围
    poly_bound = poly.bounds
    poly_bound_min_lat = poly_bound[1]
    poly_bound_min_lon = poly_bound[0]
    poly_bound_max_lat = poly_bound[3]
    poly_bound_max_lon = poly_bound[2]
    index_min = nearest_point_index(crs_from, crs_to, poly_bound_min_lon, poly_bound_min_lat, xs, ys)
    index_max = nearest_point_index(crs_from, crs_to, poly_bound_max_lon, poly_bound_max_lat, xs, ys)
    # 注意y是倒序的
    range_x = [index_min[0], index_max[0]]
    range_y = [index_max[1], index_min[1]]
    # 注意在nc文件中，lat和lon的坐标都是(y,x)range_y[1] + 1
    for i in range(range_y[0], range_y[1] + 1):
        for j in range(range_x[0], range_x[1] + 1):
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

    # var_data是一个三维的数组，var_data的时间变量是第1个维度，利用mask的数据搜索另外两维，一次性读取数据量太大，无法读入，因此要对时间循环，循环后直接根据索引取数据
    # 数据的索引花的时间太久，感觉必须要在下载数据时就先按照范围把数据下载好，然后再来生成mask，或者用matlab看看读取速度会不会较快
    mask = np.array(mask)
    index = mask.T

    def f_avg(i):
        data_day = netcdf_data.variables[var_type][i]
        data_chosen = data_day[index[0], index[1]]
        # 直接numpy指定位置处的数据求平均
        data_mean = np.mean(data_chosen, axis=0)
        return data_mean

    # 使用map循环
    all_mean_data = list(map(f_avg, range(365)))

    return all_mean_data


# 先读取一个netcdf文件，然后把shapefile选择一张，先测试下上面的程序。
# Define path to folder，以r开头表示相对路径
input_folder = r"examples_data"

# Join folder path and filename
netcdf_file = "daymet_v3_prcp_1980_na.nc4"
file_path = os.path.join(input_folder, netcdf_file)
data_netcdf = Dataset(file_path, 'r')  # reads the netCDF file
# 看看netcdf的格式具体是什么样的，便于后面判断坐标之间的空间关系
print(data_netcdf)
print(data_netcdf.variables.keys())  # get all variable names
temp_lat = data_netcdf.variables['lat']  # temperature variable
print(temp_lat)
temp_lon = data_netcdf.variables['lon']  # temperature variable
print(temp_lon)
for d in data_netcdf.dimensions.items():
    print(d)
x, y = data_netcdf.variables['x'], data_netcdf.variables['y']
print(x)
print(y)
# x，y是其他变量的坐标：lat(y,x), lon(y,x), prcp(time,y,x)。所以先看看x和y的数据的规律
x = data_netcdf.variables['x'][:]
y = data_netcdf.variables['y'][:]
# 判断x和y是否递增,x是递增的，y是递减的
lx = list(x)
ly = list(y)
print(all(ix < jx for ix, jx in zip(lx, lx[1:])))
print(all(iy > jy for iy, jy in zip(ly, ly[1:])))
lons = data_netcdf.variables['lon'][:]
lats = data_netcdf.variables['lat'][:]

shp_file = os.path.join(input_folder, "03144816.shp")
# 投影坐标系
crs_pro_str = '+proj=lcc +lat_1=25 +lat_2=60 +lat_0=42.5 +lon_0=-100 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs'
# 地理坐标系
crs_geo_str = '+proj=longlat +datum=WGS84 +no_defs'
crs_from = CRS.from_proj4(crs_geo_str)
crs_to = CRS.from_proj4(crs_pro_str)

# 先选择一个shpfile
new_shps = gpd.read_file(shp_file)
polygon = new_shps.at[0, 'geometry']
start = time.time()
mask = create_mask(polygon, x, y, lons, lats, crs_from, crs_to)
end = time.time()
print('生成mask耗时：', '%.7f' % (end - start))
print(np.array(mask))
var_types = ['prcp']
# var_types = ['tmax', 'tmin', 'prcp', 'srad', 'vp', 'swe', 'dayl']

for var_type in var_types:
    start = time.time()
    avg = calc_avg(mask, data_netcdf, var_type)
    end = time.time()
    print('计算耗时：', '%.7f' % (end - start))
    print('平均值：', avg)
