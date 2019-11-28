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
    polygon_to = Polygon()
    # 多边形外边界的各点坐标list里面是tuple
    boundary = polygon_from.boundary
    if len(boundary) == 1:
        pxys = list(polygon_from.exterior.coords)
        pxys_out = []
        # 循环处理各个坐标
        for pxy in pxys:
            xy_out = trans_point(from_crs, to_crs, pxy)
            pxys_out.append(xy_out)
        polygon_to = Polygon(pxys_out)
    elif len(boundary) >= 2:
        # 如果polygon有内部边界，则还需要将内部边界各点坐标也进行转换，然后后面再将内外部边界一起给到一个新的polygon，注意内部边界有可能有多个
        exts = boundary[0].xy
        pxys_ext = []
        for px_ext, py_ext in zip(exts[0], exts[1]):
            pxy_ext = (px_ext, py_ext)
            xy_ext = trans_point(from_crs, to_crs, pxy_ext)
            pxys_ext.append(xy_ext)
        pxys_ints = []
        for i in range(1, len(boundary)):
            ints = boundary[i].xy
            pxys_int = []
            for px_int, py_int in zip(ints[0], ints[1]):
                pxy_int = (px_int, py_int)
                xy_int = trans_point(from_crs, to_crs, pxy_int)
                pxys_int.append(xy_int)
            pxys_ints.append(pxys_int)
        polygon_to = Polygon(shell=pxys_ext, holes=pxys_ints)
    else:
        print("error")

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
    for i in range(1, data.shape[0]):
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
    return new_datas


# Define path to folder，以r开头表示相对路径
input_folder = r"examples_data"
output_folder = r"examples_data/wgs84"

# Join folder path and filename
shp_file = "bas_nonref_CntlPlains.shp"

# output_folder = r"examples_data/wgs84lccsp2"
# crs_final_str = '+proj=lcc +lat_1=25 +lat_2=60 +lat_0=42.5 +lon_0=-100 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs'

new_datas = trans_shp_coord(input_folder, shp_file, output_folder)
