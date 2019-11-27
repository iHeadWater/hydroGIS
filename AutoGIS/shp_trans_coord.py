"""首先读取shapefile文件，然后对每个polygon的每个坐标点进行坐标变换，接着再重新构建一个个的shapefile"""
import os
import geopandas as gpd
from shapely.geometry import Polygon
from pyproj import CRS
from pyproj import Transformer


def trans_point(from_crs, to_crs, xy_coord):
    """根据给定的crs，转换给定给的点坐标
    :param
    xy_coord-- tuple, length is 2
    """
    transformer = Transformer.from_crs(from_crs, to_crs, always_xy=True)
    x_coord = xy_coord[0]
    y_coord = xy_coord[1]
    x_out, y_out = transformer.transform(x_coord, y_coord)
    xy_out = (x_out, y_out)
    return xy_out


def trans_polygon(from_crs, to_crs, polygon_from):
    """转换多边形的各点坐标"""
    # 多边形外边界的各点坐标list里面是tuple
    pxys = list(polygon_from.exterior.coords)
    pxys_out = []
    # 循环处理各个坐标
    for pxy in pxys:
        xy_out = trans_point(from_crs, to_crs, pxy)
        pxys_out.append(xy_out)
    polygon_to = Polygon(pxys_out)
    return polygon_to


def trans_shp_coord(input_folder, input_shp_file, output_crs_proj4_str):
    """按照坐标系信息，转换shapefile，被转换坐标读取自shapefile"""
    fp = os.path.join(input_folder, input_shp_file)
    data = gpd.read_file(fp)
    crs_proj4 = CRS(data.crs).to_proj4()
    crs_final = CRS.from_proj4(output_crs_proj4_str)
    all_columns = data.columns.values  # ndarray type
    new_datas = []
    for i in range(data.shape[0]):
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

        print(newdata)
        # Set the GeoDataFrame's coordinate system to WGS84 (i.e. epsg code 4326)
        newdata.crs = crs_final
        print("PROJ.4: ", newdata.crs)
        new_datas.append(newdata)
    return new_datas


# Define path to folder，以r开头表示相对路径
input_folder = r"examples_data"

# Join folder path and filename
shp_file = "bas_nonref_CntlPlains.shp"

crs_final_str = '+proj=lcc +lat_1=25 +lat_2=60 +lat_0=42.5 +lon_0=-100 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs'

new_datas = trans_shp_coord(input_folder, shp_file, crs_final_str)
