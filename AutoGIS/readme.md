# Learn AutoGIS

本文件夹内容主要基于[AutoGIS课程](https://autogis-site.readthedocs.io/en/latest/)，翻译整理其中一部分, 并补充关于GDAL基础 和 更多栅格计算的内容；此外还有一些关于空间统计分析的补充。

本文参考了以下资料：

- [PD-11 - Python for GIS](https://gistbok.ucgis.org/bok-topics/python-gis)
- [EuroSciPy 2017: GeoPandas - geospatial data in Python made easy](https://www.youtube.com/watch?v=bWsA2R707BM)

## Motivation

应用python到地理数据分析。学习如何使用python和各类GIS相关库程序处理并分析空间数据。

## 主要内容

本文件夹主要包括以下内容, 各部分尚不完善, 仍在不断补充完善中...

1. 矢量数据类型介绍
2. 读写空间数据
3. GIS矢量数据空间分析
4. 可视化GIS数据
5. GIS公开数据获取
6. python + QGIS简介
7. 栅格数据简介
8. 加速GIS计算
9. My GIS Gallery
10. 空间统计分析

## why python for GIS

Python 是地理空间编程和应用开发中很流行的语言; Python在分析大数据方面是有效的；Python灵活支持各类空间数据格式

许多GIS软件比如ArcGIS，QGIS，PostGIS等都提供了python接口。

ArcGIS已经把Python作为核心脚本语言，它的ArcPy包提供了对地理处理工具，函数，类和模块的接口。一个arcpy函数定义了一些特定功能。ArcGIS的python脚本可以还可以在ArcGIS外使用。

在QGIS中，有多种方式使用Python作为一种脚本语言。通过QGIS的图像用户接口（GUI），用Python 控制台来提供交互式shell用以运行脚本。Python还用来开发processing 框架作为QGIS的一部分。这是一个地理处理环境，可用于从QGIS内部运行本地或外部/第三方算法。

除了桌面GIS工具。Python还用于开发其他独立的地理空间应用程序。主要示例与PySAL项目相关，包括：GeoDaSpace，用于空间回归分析的软件包；CAST：时空犯罪分析；和STARS（区域系统的时空分析）。这些软件包是使用Python开发的，并将高级地理空间功能包装在GUI中。

和ArcGIS这样成熟的商业软件相比，开源的GIS工具一个缺点就是它们都是由不同的开发者在不同的python库支持下开发的，这就意味着不得不熟悉许多不同的库及其文档，以下是常见的 Python 地理空间 development stack（a group of software programs that work together to achieve a specific result or to carry out a particular analytical task）。

|Layer|Package|Description|WWW|
|-|-|-|-|
|Spatial Data IO| gdal|Interface to Geospatial data abstraction library|https://pypi.python.org/pypi/GDAL/ (link is external)|
|| fiona|API to OGR (Vector) layer of GDAL| http://toblerity.org/fiona/ (link is external)|
|| rasterio|Reading and writing geospatial raster data|https://github.com/mapbox/rasterio (link is external)|
|Geoprocessing| shapely|Deterministic spatial analysis|http://toblerity.org/shapely (link is external)|
|| rasterstats|Summarizing rasters using vector geometries|https://github.com/perrygeo/python-rasterstats (link is external)|
|| geopandas|Pandas-like spatial operations on geometric types|http://geopandas.org (link is external)|
|| pyproj|PROJ4 Interface for cartographic transformations|https://github.com/jswhit/pyproj (link is external)|
|Geovisualization| basemap|Plotting 2D data on maps|https://github.com/matplotlib/basemap (link is external)|
||cartopy|Cartographic tools| http://scitools.org.uk/cartopy (link is external)|
||folium|Visualization via interactive Leaflet maps| https://github.com/python-visualization/folium (link is external)|
||bokeh|Interactive visualization library browsers| https://github.com/bokeh (link is external)|
||datashader|Big data visualization graphics pipeline|https://github.com/bokeh/datashader (link is external)|
|Spatial Statistical Analysis|PySAL|Spatial data analysis| http://pysal.org (link is external)|
||pykriging|Geostatistics| http://pykriging.com/ (link is external)|
|Spatial Modeling|mesa|Agent based modeling| https://github.com/projectmesa (link is external)|
||spint|Spatial interaction modeling|https://github.com/pysal/pysal/tree/master/pysal/contrib/spint (link is external)|
||clusterpy|Spatially constrained clustering|http://www.rise-group.org/zonificando-la-ciudad-por-perfil-de-clientes-copy/ (link is external)|
|Web and Distributed|OWSlib|Client programming interface to OGC web service|https://geopython.github.io/OWSLib/ (link is external)|
||Stetl|Streaming ETL for geospatial data| http://www.stetl.org/en/latest/|

## 完全python环境下的GIS工具类型

了解python都知道numpy可以用来进行数学运算，matplotlib可用于可视化数据，现在按功能归纳不同GIS任务的python模块如下。

### 空间数据输入/输出

所有空间分析均始于读取地理空间数据。空间数据分析的主要特征之一是丰富的空间数据格式。这对地理空间开发人员构成了重大挑战，因为根本找不到 one-size-fits-all 的软件包。

实现文件输入（和输出）的方法是包装现有的C库，这些C库已被广泛用于地理空间目的。主要的库是Geospatial Data Abstraction Library（GDAL），该库为translators提供了读写栅格和矢量空间数据的功能。在Python stack中，已经开发了针对这些组件的两个不同的库。Fiona专注于OGR（矢量）功能，而rasterio提供了类似的包装程序来包装GDAL的栅格功能。这样可以通过依赖于numpy N-D数组的Python API读取和写入诸如GeoTIFF之类的格式，从而实现高效的计算。

### 地理处理

一旦将地理空间数据读入内存，便可以进行各种几何运算和操作以进行后续处理。对于矢量数据，地理处理采取set theoretic operations and manipulation of planar features的形式。软件包Shapely封装了geos库，用于在矢量对象上进行buffering, intersection, dilation, differencing以及其他类型的空间运算符。rasterstats软件包提供了栅格r focal, zonal, and summarization的功能。Rasterstats还可以支持使用矢量几何查询栅格。例如，开发人员可以根据点矢量对象从存储在TIF文件中的DEM中找到对应高程，或者生成多边形对象范围内高程的摘要统计信息（即区域内的高程的均值，最大值，std） 。

为了适当地协调和集成来自不同格式和来源的数据，可通过pyproj包提供在不同坐标参考系统之间转换的功能。pyproj是一个Cython包装器，它为PROJ.4库提供Python接口，用于制图转换和大地测量计算。

### 地理可视化和制图

Python中地理空间数据的可视化和制图起源于在basemap中实现的global scale mapping。Basemap本身并没有实现实际的绘制，而是依靠Proj4.C将坐标转换为特定的地图投影，然后使用matplotlib（Python中的主要可视化库）在投影坐标下对轮廓，图像或矢量对象进行实际绘制。Basemap是在海洋学和气象学的支持下起源的，随着时间的推移，其功能已经演变为支持其他学科，从生物学到地质学和地球物理学。不过现在开发已经转到cartopy. 

cartopy是一个软件包，旨在轻松绘制地图以进行数据分析和可视化。它采用面向对象的方法来定义地图投影，并通过matplotlib为可视化提供了简单直观的界面。cartopy既依靠PROJ.4的投影功能，又依靠Shapely来读取shapefile。Cartopy最初是为支持气象研究而创建的，但现在已扩展为支持广泛的科学领域中的地图绘制。

除了cartopy与matplotlib交互用于可视化，还有一些Python的制图软件以Web浏览器作为平台来可视化。Folium是其中最早的一种，它为leaflet javascript库提供了Python接口，用于基于Web的交互式映射。Folium  还包括Vincent / Vega框架的增强功能，以将增强的标记和绘图引入地理空间可视化。Folium可与许多流行的tileset服务有接口，包括OpenStreetMap，Mapbox和Stamen，并支持GeoJSON和TopoJSON空间数据格式。

尽管不是专门为地图和地理可视化而设计的，但有两个Python可视化软件包仍应留意。一是Boken，它与Folium相似，因为它针对现代Web浏览器进行可视化。它通过D3.js库的样式实现此目的，以进行数据驱动的可视化，并着重于大型数据集的高性能交互性。[Datashader](https://github.com/bokeh/datashader )是Bokeh的一个组件，它实现了图形管道，用于通过分箱，聚合和转换来呈现大量数据集的表示形式。

### 空间统计分析

PySAL是用于空间数据空间分析功能的库。它由涵盖探索性空间数据分析的模块组成，还提供了用于空间回归，时空分析，区域化，地图分类和大量地理计算模块的功能。PySAL已添加了与许多其他软件包（Shapely，geopandas，cartopy等）接口的模块。

PySAL主要关注向量空间格式，并涵盖对与多边形，点和网络关联的属性的统计分析。地统计数据分析与地球科学中经常遇到统计分析，使用诸如克里金法和各种空间插值方法将诸如温度，降水，空气质量。这项工作大部分的目的是基于手头过程的一组观测位置的离散集合来生成连续位置的预测。在Python Stack中，地统计学是迄今为止尚未开发的一个领域，一个例子是pykriging。

### 其他

关于空间建模, 基于Web的空间分析, Open Geospatial Consortium规范等 还涉及 一系列开源工具, 但是这里暂时用不到, 所以就不学习记录了.

Python和相关的GIS软件生态系统非常活跃，并且正在不断发展。为了提高自己的熟练度，重要的是要跟上这些发展，以便通过利用语言本身和更广泛的生态系统中的软件包来使工作流保持最新状态。尽管对未来的预测总是充满挑战，但已经看到了一些事态发展的趋势。

1. 首先是越来越强调Python与其他语言之间互操作性的重要性。诸如RPy之类的软件包允许在Python和R之间建立双向接口，以便开发人员可以在同一工作流程中利用每种语言的优势。这也有助于扩大GIScience编程stack的范围。
2. 与之相关的一个领域是一组工具，这些工具通过包装用较低级语言（例如C，C ++和Fortran）编写的外部库来扩展Python。Cython，numba和swig提供了针对Python代码库中的瓶颈的方法，这些瓶颈将被计算效率更高的库所取代。
3. 在过去的十年中，并行和分布式高性能计算取得了显着进步，请参见https://wiki.python.org/moin/ParallelProcessing 。其中一个值得一提的示例包是Dask
4. 开放科学的兴起。强调需要提高透明度，可再现性和复制性，开放科学运动正在引领新型开发范例，例如Docker容器，conda环境和笔记本查看器，它们可以共享代码段甚至完整的工作流程以重现分析结果特定科学论文的基础。熟悉这些工具对于Python GIS开发将变得越来越重要。

开放科学在开放政府和开放数据运动中也具有相似之处，它们推动了政府收集数据的透明性，共享和重用。这些促进了合作项目的开展，使学术研究人员，政府和行业聚集在一起，以针对社会和环境问题的时尚计算解决方案为目标。鉴于其中许多项目涉及地理空间数据和分析，具有Python GIS能力的科学家工程师可以在这些工作中发挥核心作用。
