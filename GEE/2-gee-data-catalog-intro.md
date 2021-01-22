# GEE数据

google earth engine是谷歌开发的一个应用，凭借谷歌超强的服务器运算能力以及与 NASA 的合作关系,GEE 平台将 Landsat/Sentinel 等可以公开获取的遥
感图像数据存储在谷歌的磁盘阵列中,使得 GEE 用户可以方便的提取、调用和分析海量的遥感大数据资源。本文主要了解GEE的数据组成相关方面内容。先给出参考资料如下。

## 参考资料

1. [认识 Google Earth Engine](https://drive.google.com/file/d/1jj8rQmAaw_a2LuCWnhCZlvevZ3_eU8uM/view)
2. [Our latest additions to the Earth Engine Data Catalog](https://medium.com/google-earth/our-latest-additions-to-the-earth-engine-data-catalog-ded9c563f676)
3. [Google Earth Engine: Planetary-scale geospatial analysis for everyone](https://www.sciencedirect.com/science/article/pii/S0034425717302900)
4. [Earth Engine Data Catalog](https://developers.google.com/earth-engine/datasets)
5. [GEE 教程基础篇_Slides_v3](https://drive.google.com/file/d/1gbF1qO9lkz-LUghsZZSsVz51ZqpkGGkD/view)
6. [GEE 教程基础篇-v3](https://drive.google.com/file/d/1i0xGC1uH9YPukyJgA1FYRjRtn0keVFYo/view)

## GEE Data Catalog

GEEDC是一个超过600个数据集的在线库，共约29pb的数据量，并且还在以每个月约1pb的速度增加，数据集每6个小时都会自动更新。维护该数据集的目的是为了使GEE社区能够更好地访问数据，开展数据分析，科学观测分析了解我们的地球。

GEE用image容器来构建二维栅格数据的数据模型。每个band内的像素在data type，resolution和projection方面都是相同的，不过imgaes可以有任意数量的bands，一个image内的bands是不必有统一的数据类型或投影的。每个image都有元数据嘻嘻你存储诸如位置／获取时间等信息。

相关images，比如同一个传感器生成的所有images，被组织为一个“collection”，collection提供有filter和sorting等功能，使人能快速检索到自己想要的数据。

Images都由GEE预处理过以方便快速获取：

1. images在保持projection和resolution的基础上被切分为tiles，并存储在tile数据库中；
2. 为了快速可视化，GEE构建来金字塔可视化地图的体系，即有一批不同分辨率的tile存储在数据库中；

根据Data Catalog官方网站的介绍，数据集主要有如下内容，具体数据可参考文献[3]：

- Climate and Weather
    - Surface Temperature：land and sea surface temperature products derived from several spacecraft sensors, including MODIS, ASTER, and AVHRR, in addition to raw Landsat thermal data.
    - Climate：historical reanalysis data from NCEP/NCAR, gridded meteorological datasets like NLDAS-2, and GridMET, and climate model outputs like the University of Idaho MACAv2-METDATA and the NASA Earth Exchange’s Downscaled Climate Projections.
    - Atmospheric：atmospheric datasets such as ozone data from NASA's TOMS and OMI instruments and the MODIS Monthly Gridded Atmospheric Product.
    - Weather：including precipitation, temperature, humidity, and wind, and other variables. forecast data from GFS and the NCEP CFSv2, as well as sensor data from sources like the TRMM.
- Imagery
    - Landsat：image the entire Earth's surface at a 30-meter resolution about once every two weeks, including multispectral and thermal data.
    - Sentinel：all-weather radar images from Sentinel-1A and -1B, high-resolution optical images from Sentinel 2A and 2B, as well as ocean and land data suitable for environmental and climate monitoring from Sentinel 3.
    - MODIS：daily imagery, 16-day BRDF-adjusted surface reflectance, and derived products such as vegetation indices and snow cover.
    - High-Resolution Imagery： aerial image data of the US at one-meter resolution, including nearly complete coverage every several years since 2003.
- Geophysical
    - Terrain：several global DEMs such as SRTM data at 30-meter resolution, regional DEMs at higher resolutions, and derived products such as the WWF's HydroSHEDS hydrology database.
    - Land Cover：land cover classes such as forest, grassland, and water. global products such as NASA's MODIS-derived annual land cover maps and ESA's GlobCover, as well as higher-resolution national products such as the USGS National Land Cover Database.
    - Cropland：key to understanding global water consumption and agricultural production. the USDA NASS Cropland Data Layers, as well as layers from the GFSAD including cropland extent, crop dominance, and watering sources.
    - Other geophysical data：night-time imagery from the DMSP-OLS, which has collected imagery of night-time lights at approximately 1-kilometer resolution continuously since 1992.
    
简单补充下一些名词的全称：

|  简称  | 全称  | 中文 |
|  ----  | ----  | ---- |
| MODIS  | moderate resolution image spectroradiometer | 中分辨率成像光谱仪 |
| ASTER  | advanced spaceborne thermal emission and reflection radiometer | 先进星载热发射和反射辐射仪 |
| AVHRR  |  Advanced Very-High-Resolution Radiometer | － |
| Landsat  | － | 陆地卫星计划|
| NCEP  | National Centers for Environmental Prediction | － |
| NCAR  | National Center for Atmospheric Research | 国家大气研究中心|
| NLDAS  | North American Land Data Assimilation System | － |
| GridMET  | gridded surface meteorological data | － |
| MACAv2  | Multivariate Adaptive Constructed Analogs version 2 | － |
| NASA  |  National Aeronautics and Space Administration | 美国国家航空航天局|
| TOMS  | Total Ozone Mapping Spectrometer | 测绘臭氧总量分光计|
| OMI  | Ozone Monitoring Instrument | －|
| NOAA  | National Oceanic and Atmospheric Administration | 美国国家海洋和大气管理局|
| GFS  | Global Forecast System | －|
| CFS  | Climate Forecast System | －|
| TRMM  | Tropical Rainfall Measuring Mission | 热带降雨量测量任务|
| Sentinel  | － | 哨兵|
| BRDF  | Bi-directional Reflectance Distribution Function | －|
| SRTM  | Shuttle Radar Topography Mission | 航天飞机雷达地形测绘任务|
| WWF  | World Wildlife Fund | 世界自然基金会|
| HydroSHEDS  | Hydrological data and maps based on SHuttle Elevation Derivatives at multiple Scales | －|
| ESA  | European Space Agency | 欧洲空间局|
| USGS  | United States Geological Survey | 美国地质调查局|
| USDA  | United States Department of Agriculture | 美国农业部|
| GFSAD  | Global Food Security-Support Analysis Data | - |
| DMSP-OLS  | Defense Meteorological Satellite Program's Operational Linescan System | －|
| OLI  | Operational Land Imager | － |
| TIRS  | Thermal Infrared Sensor | － |
| ETM+  | Enhanced Thematic Mapper Plus | － |
| TM  | Thematic Mapper | － |
| FPAR | fraction of photosynthetically active radiation | － |
| ASTER L1 T radiance | The ASTER Level 1 Precision Terrain Corrected Registered At-Sensor Radiance | － |
| PROBA－V  | Project for On-Board Autonomy Vegetation| － |
| EO－1  | Earth Observing-1 | 地球观测卫星1号 |
| NAIP | National Agriculture Imagery Program | － |
| GMTED2010 | Global Multi-resolution Terrain Elevation Data 2010 | － |
| GTOPO30 | Global 30 Arc-Second Elevation | － |
| ETOP01 | 1 arc-minute global relief model  | － |
| UMD | University of Maryland | － |
| GLCF | Landsat Tree Cover Continuous Fields | － |
| JRC | Joint Research Centre | － |
| USDA NASS | National Agricultural Statistics Service | 美国国家农业统计局 |
| CHIRPS | Climate Hazards Group InfraRed Precipitation with Station data | － |
| NEX | NASA Earth Exchange | － |
| GPW | Gridded Population of the World | － |
| SAR | synthetic aperture radar  | 合成孔径雷达 |
| Sentinel 5P | Sentinel 5 Precursor  | - |
| SR | surface reflectance  | - |
| JAXA | Japan Aerospace Exploration Agency | 宇宙航空研究开发机构 |
| FAPAR | Fraction of Absorbed Photosynthetically Active Radiation  | - |
| CORINE  | The Coordination of Information on the Environment | - |
| GOES  | Geostationary Operational Environmental Satellite | - |

根据博客[2]，自2018年6月以来，增加的数据有：

- Sentinel 5P：每日8种空气污染物浓度；
- Sentinel 2 SR:mapping landscape的地表反射图像，已进行大气校正，可以用于change detection和时间序列分析；
- JAXA yearly SAR mosaics: 全球年度SAR mosaics，反映地表特征的结构和组成；
- Copernicus CORINE：欧洲land cover地图；
- Intertidal change:潮汐数据；
- Arctic and Antarctic DEMSs：海洋高程数据；
- USGS GAP／Landfire ecosystems:全美详细的vegetation和land cover分类；
- OpenLandMap data：一系列生态群落数据，包括基于MODIS的温度，降雨组成，土壤特性，FAPAR和potential vegetation type等数据。
- GOES－16和GOES－17：西半球火灾观测。
