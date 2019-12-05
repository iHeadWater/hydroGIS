# Learn AutoGIS

[AutoGIS课程](https://automating-gis-processes.github.io/site/)的学习记录，翻译其中内容。

## Motivation

应用python到地理数据分析。学习如何使用python和各类GIS相关库程序处理并分析空间数据。

## 基本内容

- 读写空间数据文件
- 处理不同投影
- 几何操作与编码
- 分类数据
- 空间查询
- 简单空间分析
- 可视化数据

## why python for GIS

许多GIS软件包比如ArcGIS，QGIS，PostGIS等都提供了python接口，因此python+GIS是非常值得学习的，不过这个课程是没有使用第三方GIS软件的，原因有：

- 课程是免费的，而ArcGIS等是很贵的；
- 学习和理解地理处理运算；
- Python在分析大数据方面是有效的；
- Python灵活支持各类空间数据格式；
- 开源精神；
- 嵌入和链接第三方软件可以构建漂亮的webGIS应用（比如GeoDjango（前端） + PostGIS（后端））

## 完全python环境下的GIS工具类型

了解python都知道numpy可以用来进行数学运算，matplotlib可用于可视化数据，现在让我们了解不同GIS任务的python模块。

和ArcGIS这样成熟的商业软件相比，一个缺点就是开源的GIS工具都是由不同的开发者在不同的python库支持下开发的，这就意味着得熟悉许多不同的库及其文档，而在ArcGIS下，一切都在arcpy模块下。

以下给出一些关键模块及其连接，需要的时候可以查阅相关文档：

- 数据分析与可视化
    - [Numpy](http://www.numpy.org/) –> 科学计算基础库
    - [Pandas](http://pandas.pydata.org/) –> 高性能，使用方便的数据结构和数据分析工具
    - [Scipy](http://www.scipy.org/about.html) –> 数值计算工具集合，包括优化，统计等
    - [Matplotlib](http://matplotlib.org/) –> 基础绘图工具
    - [Bokeh](http://bokeh.pydata.org/en/latest/) –> web端交互可视化
    - [Plotly](https://plot.ly/python/) –> web端交互可视化 (商业的 - 教育版免费)
- GIS
    - [GDAL](http://www.gdal.org/) –> 处理矢量，栅格数据的基础包（许多模块都基于它构建）。用于raster processing.
    - [Geopandas](http://geopandas.org/#description) –> 使python处理空间数据变得简单，结合了pandas和shapely的能力
    - [Shapely](http://toblerity.org/shapely/manual.html) –> 处理和分析平面几何对象（基于广泛应用的GEOS）
    - [Fiona](https://pypi.python.org/pypi/Fiona) –> 读写空间数据 (类似geopandas).
    - [Pyproj](https://pypi.python.org/pypi/pyproj?) –> 制图变换和地学计算(基于[PROJ.4](http://trac.osgeo.org/proj)).
    - [Pysal](https://pysal.readthedocs.org/en/latest/) –> 空间分析函数库
    - [Geopy](http://geopy.readthedocs.io/en/latest/) –> 地理编码库，坐标和地址的互相转换
    - [Contextily](https://github.com/darribas/contextily) –> 为静态地图可视化增加背景图
    - [GeoViews](http://geo.holoviews.org/index.html) –> web端可交互地图
    - [Geoplot](https://github.com/ResidentMario/geoplot) –> 高级地理数据可视化库
    - [Dash](https://plot.ly/products/dash/) –> 分析型web应用框架.
    - [OSMnx](https://github.com/gboeing/osmnx) –> 从OpenStreetMap获取，构建，分析和可视化街道网络
    - [Networkx](https://networkx.github.io/documentation/networkx-1.10/overview.html) –> 网络分析和路径构建(比如 Dijkstra 以及 A* -算法), 见这篇[post](http://gis.stackexchange.com/questions/65056/is-it-possible-to-route-shapefiles-using-python-and-without-arcgis-qgis-or-pgr).
    - [Cartopy](http://scitools.org.uk/cartopy/docs/latest/index.html) –> 构建数据分析及可视化的地图
    - [Scipy.spatial](http://docs.scipy.org/doc/scipy/reference/spatial.html) –> 空间算法和数据结构
    - [Rtree](http://toblerity.org/rtree/) –> 快速空间数据查询的空间索引
    - [Rasterio](https://github.com/mapbox/rasterio) –> 简洁快速的地理空间栅格数据I/O
    - [RSGISLib](http://www.rsgislib.org/index.html#python-documentation) –> 遥感和GIS软件库
    
## 安装库

许多GIS包来自conda的一个特定channel，即conda-forge，开始先安装geopandas，后面再在需要的时候安装所需的。因为安装geopandas的时候会自动地安装一些基础GIS包，比如Shapely和fiona

### win10下安装

所以先执行下面的程序即可：

``` python
conda install geopandas -c conda-forge
```

在geopandas中绘图需要geoplot包，因此安装：

``` python
# Install geoplot
conda install -c conda-forge geoplot
# upgrade pyproj
conda update pyproj -c conda-forge
# install geojson
conda install -c conda-forge geojson
```

### Ubuntu 18.04下安装

在Ubuntu18.04下按照上述方式安装后，import geopandas报错了，可能是由于conda下安装的版本，fiona和geopandas的版本不匹配，因此直接用conda uninstall 将其卸载，并重新用pip install 安装了，再导入发现没有错误了。然后卸载的时候好像也把geoplot卸载了，所以也重新再用pip安装一次。总之使用下面的pip也可以轻松安装好geopandas，和geoplot

```python
#  如果用conda安装了，就把geopandas卸载了
conda uninstall geopandas
# 安装
pip install geopandas
pip install geoplot
```

安装pyproj，见pyproj文件夹下内容。可能已经安装，但是需要更新。

``` python
pip install --upgrade pyproj
```
