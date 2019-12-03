"""首先读取shapefile文件，然后对每个polygon的每个坐标点进行坐标变换，接着再重新构建一个个的shapefile
程序需要优化，几个方面：
1.把能放到循环外的都放到循环外处理
2.for循环用更贴近C的map等代替
3.查查有没有直接转换一组点坐标的方法
4.并行计算算法
5.把shapefile在arcgis上拆解后，多找几个电脑算
6.重新用arcgis弄
"""
import os
import time
import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon
from pyproj import CRS
from pyproj import Proj, transform


def trans_points(from_crs, to_crs, pxs, pys):
    """不要循环处理，放入到dataframe中可以极大地提高速度，那完全不是一个量级的
    :param
    pxs: 各点的x坐标组成的list的array
    pys: 各点的y坐标组成的list的array
    :return
    pxys_out: x和y两两值组成的list，可用于初始化一个polygon
    """
    df = pd.DataFrame({'x': pxs, 'y': pys})
    start = time.time()
    df['x2'], df['y2'] = transform(from_crs, to_crs, df['x'].tolist(), df['y'].tolist())
    end = time.time()
    print('%.7f' % (end - start))
    # 坐标转换完成后，将x2, y2数据取出，首先转为numpy数组，然后转置，然后每行一个坐标放入list中即可
    arr_x = df['x2'].values
    arr_y = df['y2'].values
    pxys_out = np.stack((arr_x, arr_y), 0).T
    return pxys_out


def trans_polygon(from_crs, to_crs, polygon_from):
    """转换多边形的各点坐标"""
    polygon_to = Polygon()
    # 多边形外边界的各点坐标list里面是tuple
    boundary = polygon_from.boundary
    boundary_type = boundary.geom_type
    print(boundary_type)
    if boundary_type == 'LineString':
        pxs = polygon_from.exterior.xy[0]
        pys = polygon_from.exterior.xy[1]
        pxys_out = trans_points(from_crs, to_crs, pxs, pys)
        polygon_to = Polygon(pxys_out)
    elif boundary_type == 'MultiLineString':
        # 如果polygon有内部边界，则还需要将内部边界各点坐标也进行转换，然后后面再将内外部边界一起给到一个新的polygon，注意内部边界有可能有多个
        exts_x = boundary[0].xy[0]
        exts_y = boundary[0].xy[1]
        pxys_ext = trans_points(from_crs, to_crs, exts_x, exts_y)

        pxys_ints = []
        for i in range(1, len(boundary)):
            ints_x = boundary[i].xy[0]
            ints_y = boundary[i].xy[1]
            pxys_int = trans_points(from_crs, to_crs, ints_x, ints_y)
            pxys_ints.append(pxys_int)

        polygon_to = Polygon(shell=pxys_ext, holes=pxys_ints)
    else:
        print("error!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    return polygon_to


def write_shpfile(geodata, output_folder):
    """根据geodataframe生成shpfile，用dataframe的id项做名称。"""
    # Create a output path for the data
    gage_id = geodata.iloc[0, :]['GAGE_ID']
    output_file = str(gage_id)
    output_fp = os.path.join(output_folder, output_file + '.shp')
    # Write those rows into a new file (the default output file format is Shapefile)
    geodata.to_file(output_fp)


def trans_shp_coord(input_folder, input_shp_file, output_folder,
                    output_crs_proj4_str='+proj=longlat +datum=WGS84 +no_defs'):
    """按照坐标系信息，转换shapefile，被转换坐标读取自shapefile，默认转换为WGS84经纬度坐标"""
    fp = os.path.join(input_folder, input_shp_file)
    data = gpd.read_file(fp)
    crs_proj4 = CRS(data.crs).to_proj4()
    crs_final = CRS.from_proj4(output_crs_proj4_str)
    all_columns = data.columns.values  # ndarray type
    new_datas = []
    start = time.time()
    for i in range(2, 3):  # data.shape[0]
        print("生成第 ", i, " 个流域的shapefile:")
        newdata = gpd.GeoDataFrame()
        for column in all_columns:
            # geodataframe读取shapefile之后几何属性名称就是geometry
            if column == 'geometry':
                # 首先转换坐标
                polygon_from = data.iloc[i, :]['geometry']
                polygon_to = trans_polygon(crs_proj4, crs_final, polygon_from)
                # 要赋值到newdata的i位置上，否则就成为geoseries了，无法导出到shapefile
                newdata.at[i, 'geometry'] = polygon_to
                print(type(newdata.at[i, 'geometry']))
            else:
                newdata.at[i, column] = data.iloc[i, :][column]
        print("转换该流域的坐标完成！")
        print(newdata)
        # 貌似必须转到wkt才能用来创建shapefile
        newdata.crs = crs_final.to_wkt()
        print("坐标系: ", newdata.crs)
        new_datas.append(newdata)
        write_shpfile(newdata, output_folder)
    end = time.time()
    print('计算耗时：', '%.7f' % (end - start))
    return new_datas


# Define path to folder，以r开头表示相对路径
input_folder = r"examples_data"
output_folder = r"examples_data/wgs84"

# Join folder path and filename
shp_file = "bas_nonref_CntlPlains.shp"

# output_folder = r"examples_data/wgs84lccsp2"
# crs_final_str = '+proj=lcc +lat_1=25 +lat_2=60 +lat_0=42.5 +lon_0=-100 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs'

new_datas = trans_shp_coord(input_folder, shp_file, output_folder)
