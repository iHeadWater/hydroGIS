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

这里主要给出conda环境下的安装，也尝试了直接使用pip的安装方式，个人建议以conda为主，并且安装到独立虚拟环境中较好。

### conda environment安装

许多GIS包来自conda的一个特定channel－－conda-forge。一开始先安装geopandas即可，后面再在需要的时候安装所需，这是因为安装geopandas的时候会自动地安装一些基础GIS包，比如Shapely和fiona。

安装geopandas只要执行下面的程序即可：

``` Shell
# 虚拟环境中安装
conda create --prefix ./envs python=3.7
# 激活虚拟环境，xxx表示文件夹的前缀：
conda activate xxx\hydroGIS\envs
# 如果需要独立的jupyter lab，安装：
conda install -c conda-forge jupyterlab
conda install geopandas -c conda-forge
# 在geopandas中绘图需要geoplot包
conda install -c conda-forge geoplot
conda install -c conda-forge mplleaflet
conda install -c conda-forge folium
conda install -c conda-forge osmnx
```

最后导出环境文件：

```Shell
conda env export > environment.yml
```

### pip安装

pip的安装是一开始在Ubuntu18.04下尝试在base环境下安装的，不建议使用。用pip install 可以直接安好geopandas，geoplot等。也可以使用pipenv安装，如果使用了pipenv指定虚拟环境，就还是用pipenv安装较好。

```Shell
pip install geopandas
pip install geoplot
```

一点补充：

如果本来就已经安装了pyproj，可能需要更新。

``` Shell
pip install --upgrade pyproj
```

如果在代码中需要使用到rtree库，比如调用overlay函数或者sjoin函数等空间分析函数，如果没有安装rtree，那么在ubuntu下允许这些空间分析函数会报错。所以需要手动补充安装一些库。根据参考：[Overly Function from GeoPandas Not Working
](https://stackoverflow.com/questions/53546775/overly-function-from-geopandas-not-working)所说，因为rtree是C library libspatialindex的wrapper。因此，需要先安装好 libspatialindex C library. 再安装rtree python库。具体代码如下：

```Shell
sudo apt-get update
sudo apt-get install libspatialindex-dev
```

```Shell
pip install rtree
```

安装 mplleaflet 库：

```Shell
pip install mplleaflet
```