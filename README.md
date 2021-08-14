# hydroGIS

Practices for gis in hydrology 

水文水资源的科研和工程实践中一定缺不了GIS工具的使用，熟悉一些常用GIS工具十分有必要，这里记录平时一些实践备查。GIS相关资源可参考：[awesome-gis](https://github.com/sshuair/awesome-gis)。

结合awesome-gis可知，GIS工具类型繁多，有成套的GIS软件（ArcGIS, QGIS），遥感软件（ENVI），有成熟的3D应用、地图服务、GIS云计算（Google earth engine）等，也有基础的工具，如PostGIS数据库，leafletweb前端可视化工具等，还有最基本的地理空间计算库：比如python下的[Shapely](https://github.com/Toblerity/Shapely)、[Fiona](http://github.com/toblerity/fiona/)、[GeoPandas](https://github.com/geopandas/geopandas)、[Pyproj](https://github.com/pyproj4/pyproj)、[Cesium](https://github.com/AnalyticalGraphicsInc/cesium)等。

本repo不会去都尝试涉及，而是主要关注的和水文水资源相关的GIS运算，因此，安排内容大致如下：

- ArcGIS：每个涉及到GIS的人都会知道这个软件，不过我没钱买正版工具，所以就主要了解下ArcGIS的基本概念和简单用法，不做过多记录
- AutoGIS：主要参考[Automating GIS-processes](https://github.com/Automating-GIS-processes/site)，了解Python GIS 常用的开源库，并给一些实例，方便简单的GIS计算
- GEE：google earth engine是非常好用的工具，在科学上网的条件下能高效地处理大多数的GIS计算，这里主要记录一些GEE python接口，尤其是[geemap](https://github.com/giswqs/geemap)的使用。
- QGIS：基本可以认为是免费版的ArcGIS，因为是开源的，所以不会像商业软件那样做的非常详尽，但是应对水文专业GIS应用还是足够的。

environment.yml里记录了win10下AutoGIS和GEE文件夹下内容所需的python环境, 参考了：https://github.com/earthlab/earth-analytics-python-env/blob/main/environment.yml 。在项目根目录下打开终端，执行以下语句即可安装环境, 安装时间会比较长, 请耐心等待：

```Shell
conda env create -f environment.yml
```

这个安装很慢，请你忍一下；如果忍不了，可以试试mamba：

```Shell
conda create -n hydroGIS python=3.8
conda activate hydroGIS
conda install geopandas
conda install mamba -c conda-forge
mamba install geemap xarray_leaflet geopy contextily osmnx rasterstats xarray-spatial pointpats pykrige pykriging jupyterlab jupyter_contrib_nbextensions -c conda-forge
```

目前内容主要集中在AutoGIS里，后期会根据自己GIS的使用情况逐步更新。
