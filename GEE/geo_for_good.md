# Geo for good

Geo for Good User Summit是一个Google的会议，每年都会有，会对Google地球相关的内容进行讨论和培训。这里仅简单了解下从2019年与GEE相关的培训材料内容，以储备一些GEE的使用资料。

## 基础知识补充

首先，补充一些基本卫星的解释，以使后面的阅读顺利。

|简称|全称|中文|基本用途|
|-|-|-|-|
|Suomi NPP| Suomi National Polar-orbiting Partnership |索米国家极地轨道伙伴卫星| weather satellite  |
|Auro|-|-|studying the Earth's ozone layer, air quality and climate|
|ACRIMSAT| Active Cavity Radiometer Irradiance Monitor Satellite|－|Solar astronomy|
|SORCE|Solar Radiation and Climate Experiment|太阳辐射和气候实验| measures incoming X-ray, ultraviolet, visible, near-infrared, and total solar radiation|
|CALIPSO|Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations|－|monitor aerosols and clouds|
|CLOUDSAT|－|－|measure the altitude and properties of clouds for global warming|
|EO-1|Earth Observing-1|－| develop and validate a number of instrument and spacecraft bus breakthrough technologies|
|Terra|－|－|同时采集地球大气、陆地、海洋和太阳能量平衡等信息，studying the interactions among the Earth's atmosphere, lands, oceans, and radiant energy|
|Aqua|－|－|studying the precipitation, evaporation, and cycling of water|
|QuikSCAT|Quick Scatterometer|－|measure the surface wind speed and direction over the ice-free global oceans|
|OSTM/Jason-2 | Ocean Surface Topography Mission on the Jason-2 satellite|－| sea surface height measurements |
|Aquarius/SAC-D |－|－|demonstrate that accurate measurements of salinity could be made from space|
|OCO－2|Orbiting Carbon Observatory 2|在轨碳观测台2号||
|SMAP|Soil Moisture Active Passive|| maps global soil moisture and detects whether soils are frozen or thawed|
|NISTAR|||measures the outgoing radiation from the Earth|
|CYGNSS|Cyclone Global Navigation Satellite System||improving hurricane forecasting by better understanding the interactions between the sea and the air near the core of a storm|
|CATS| Cloud-Aerosol Transport System||measured atmospheric aerosols and clouds from the International Space Station (ISS)|
|MOS|Marine Observation Satellite|| for more effective natural resource utilization and for environmental protection|
|JERS-1|Japanese Earth Resources Satellite 1|日本地球资源卫星1号|survey of geological phenomena, land usage (agriculture, forestry), observation of coastal regions, geologic maps, environment, disaster monitoring, etc.|
|ADEOS|Advanced Earth Observing Satellite||observe Earth's environmental changes, focusing on global warming, depletion of the ozone layer, and deforestation|
|ALOS|Advanced Land Observation Satellite|| cartography and disaster monitoring of Asia and the Pacific |
|GOSat|Greenhouse Gases Observing Satellite|温室气体观测卫星|greenhouse-gas-monitoring|
|GCOM|Global Change Observation Mission||observation and utilization of global geophysical data such as precipitation, snow, water vapor, aerosol, for climate change prediction, water management, and food security|
|GCOM-W|GCOM-Water||observe the water cycle|
|GCOM-C|Global Change Observation Mission – Climate||monitor global climate change by observing the surface and atmosphere of Earth|
|GPM-DPR|Global Precipitation Measurement Dual-frequency Precipitation Radar|全球降雨測量| provides global precipitation maps to assist researchers in improving the forecasting of extreme events, studying global climate, and adding to current capabilities for using such satellite data to benefit society|
|EarthCARE|Earth Clouds, Aerosols and Radiation Explorer||devoted to the study of natural and anthropogenic climate change. This involves the observation of clouds, aerosols and radiation parameters|

一些在GEE中用到的RS或GIS基本概念：

[电磁波谱](https://commons.wikimedia.org/wiki/File%3AElectromagnetic-Spectrum.svg)是要尽力记住的，被动遥感传感器测量的光学范围是：visible, near infrared, short-wave IR和thermal IR。

太阳能与materials的interaction与光的波长有关，光电磁波在从太阳到地球再到卫星传感器的过程中，太阳能的状态有：

- Transimitted: 折射通过；
- Absorbed: 被物体电子／分子吸收；
- Reflected: 反射，reflectance就是反射能量和入射能量之比，反射光的波长决定了物体的颜色；
- Scattered: 能量传播的方向被随机改变，Rayleigh and Mie散射是大气散射最重要的两种类型；
- Emitted: 能量先被吸收，然后再出射，并且通常是长波形式，物体会升温。

传感器可测量的电磁辐射是在特定范围内的，通常称之为bands。测量结果存储为数字图像，图像中每个像素有一个单位为digital number（DN）的离散值。分辨率主要有四种：时空两种自不必说，另两种是spectral resolution和radiometric resolution，前者是指光谱bands（两个波长值包含的范围）的数量和在电磁波谱中的位置，每一个band对应一个image；后者是指image的亮度级别数对应DNs的最大值，二进制表示，比如一个8 bit分辨率的图像有256级亮度。

传感器测量的是radiance，对应的是面向传感器一个给定方向的亮度，其通常也被定义为reflectance，即反射的能量与全部能量的比值。

每种物质都有spectral signature，即反射率与波长之间的关系，每种物质有一个单独的signature，因此可以用来分类物体。

图像的是三色图，通常表示为RGB（红绿蓝），“RGB=Br Bg Bb”，Br表示与红色对应的band number，Bg和Bb同理。

Radiance是一个给定方向上每个立体角离开单位表面积的能量通量。radiance是传感器测量的，和reflectance相关。以radiance得到的image可以通过太阳辐照度的归一化转为Top Of Atmosphere （TOA）Reflectance的图，以减少景之间的变化。

[Radiance vs. Reflectance](https://www.harrisgeospatial.com/Support/Self-Help-Tools/Help-Articles/Help-Articles-Detail/ArtMID/10220/ArticleID/19247/3377):

Radiance是直接由传感器直接测量的。当经过大气层时，大气层以两种相反的方式影响辐射，一是一些被大气层散射的光也会被传感器观测并被包含在目标物的radiance中，这称为“path radiance”；另外，大气层也会吸收光，会减少观测到的radiance，这称为“incident radiation”或“irradiation”。radiance的单位是watt。

Reflectance是离开目标的光量与照射在目标上的光量之比。如果所有离开目标的光都被获得来测量reflectance，那么这一结果称为hemispherical reflectance。

Reflectance是被观测物体的属性，而radiance则依赖光照强度／方向以及目标物的方位和位置。考虑大气效应和太阳光照的reflectance称为“apparent reflectance”，不同于真实的reflectance，不过人们也称之为reflectance。

[Digital Number, Radiance, and Reflectance](https://www.harrisgeospatial.com/Learn/Blogs/Blog-Details/ArtMID/10198/ArticleID/16278/Digital-Number-Radiance-and-Reflectance)

DN是像素值，表示的是没有率定位有物理意义的值前的像素值。

Radiance是来自一个area的radiation的量，为了从一个uncalibrated image中获得一个radiance image，需要根据图像的metadata来对DN image校正，比如ENVI中的Radiometric Calibration工具。radiance包括从表面反射的辐射、从邻近像素反弹的辐射和从像素区域上方的云反射的辐射，也受光源的影响。

通常，为了对image data进行分析，还需要将radiance images校正为reflectance images。有了反射images，根据物体的反射波谱特性，就可以进行物体分类等。所以image分析的第一步通常都是先将其转为一个reflectance image。Top of Atmosphere Reflectance是由一个高于大气层的传感器测量的，该值包括云何大气气溶胶等的反射。Surface reflectance是地球表面的反射，云和其他大气成分不影响地表反射波。通常地表反射images都是从率定的radiance images再推出的，方法有基于模型的大气校正等，比如在ENVI中有Atmospheric Correction模块。

总之，通常从数据提供者那里获得的是一个未率定的image，需要首先将其率定为radiance image，然后通过大气校正将其转化为surface reflectance image，到这之后，image才能用来提取有用的地表特征信息。

[Radiometric Calibration and Corrections](http://gsp.humboldt.edu/OLM/Courses/GSP_216_Online/lesson4-1/radiometric.html)

因为传感器测量的radiation不仅包括 reflected or emitted radiation ，还有the radiation scattered and emitted by the atmosphere。而大多数情况下，我们都仅对地表值感兴趣，因此，我们需要进行radiometric calibration and correction。

![image.png](attachment:image.png)

NDVI：根据vegetation反射强烈的近红外和吸收的红光计算得到的量化植被的指标。

## 2019

关于培训GEE的部分，每年情况类似，都是先介绍基础，然后给案例，比如2014年Google Earth Engine 101，201，301，302 分别介绍了GEE的情况，api及使用方法以及案例。2014－101主要介绍了GEE处理了大量数据，因为空间数据量很大，比如一张Landsat8图像（30m分辨率）有64M大，10个波段，12位分辨率，每天有600张这样的图，共40多年的数据。然后2014－102介绍了GEE的基本接口。基本的处理图像步骤，然后提出了一个场景：旧金山的park管理员，想看**where vegetation** has **changed** between **2000 and 2010 in** all the **big parks near subway stations**.接下来，逐步地实现这一应用场景。基本上是类似这样的组织结构。

因为每年情况类似，因此就只看最近2019年的即可，并且2019年的最全面。

因为示例中很多用的都是Landsat 8的imagecollection，因此这里简单补充下关于Landsat 8的基础内容，data catalog的说明，Landsat观测了1972至今的数据，现在其分辨率空间30m，时间2 weeks，包括multispectral和thermal的数据。USGS生成的数据每个卫星有三类：

- Tier 1：满足几何和辐射质量要求的数据；
- Tier 2：不满足Tier 1条件的数据
- RT：实时的还没有评价的数据。

在GEE中提供了T1，T2，T1－RT三种数据。T1－RT的数据是每日更新的，其被验证过后，会被移出到T1或者T2中。平常使用以T1为主。每种数据都有原始数据（Raw Images DN值这里表示的是scaled， calibrated at-sensor radiance）。对于每个包含T1数据的collection，还有TOA校正的数据。另外还有校正好的surface reflectance数据。

GEE提供了多种Landsat数据的处理方法，包括计算at-sensor radiance, top-of-atmosphere(TOA) reflectance, surface reflectance(SR), cloud score 和cloud－free 组成等的算法。这里暂不表。

[Earth Engine for non-coders](https://docs.google.com/presentation/d/10DTcBGPl0JeTEOJlSRNdj9dtGLwqq7HPLzegENygI-U/edit?ts=5d7ab7ac#slide=id.g62b98c5607_0_1181)

从有代码的练习开始：
Exercise #2: “Getting Comfortable”: Perform a classification in the Code Editor
Exercise #3: Use the Data Catalog
Exercise #4: Do raster analysis, e.g. NDVI
Exercise #5: Do vector analysis, e.g. Buffer
Exercise #6: Create your own background Map Style
Exercise #7: Export your image

这部分基本上就是让看一些示例。

[Earth Engine Overview](https://docs.google.com/presentation/d/1BaGOANsu5wxLpbcXpMc5zYcrfP1x8PbxjHXMpG6qYQ4/edit#slide=id.g60040e5540_0_0)

讲GEE的why what how where。

how：get an image--apply an algorithm to it;或者filter a collection--map an algorithm over a collection--reduce a collection-compute an aggregate

GEE允许通过已有的objects以有向无环图形式定义新的objects，允许用已有函数定制新函数。

[Exporting from Earth Engine into Earth](https://docs.google.com/presentation/d/1THVjND_Q2AoDEfxNyi34O1yuJpxTg8VRzdTMCN7Ad14/edit#slide=id.p)

可以将GEE中的分析结果导入到GE中展示。

[Make your own Earth Engine App](https://docs.google.com/presentation/d/1kqR3jD9UCZW9UtCEMwL-HVMkzHyBlYnpr_j_MU2vkhk/edit#slide=id.g6374cca658_0_0)

通过定义EE App可以分享工作的输出结果。

[Getting Field Data into Earth Engine for non-coders](https://docs.google.com/presentation/d/1tU33JWKtgx3x4-NTmP6hNBLeQkogkzLPLDBQCm93GvI/edit#slide=id.g5d4a909b46_1_18)

提供众包观测数据。注意下导入csv文件的方式。

Animations in Earth Engine

直接在控制台动态可视化结果。

[Earth Engine Apps Showcase ](https://docs.google.com/presentation/d/1Bl4WF6L_zEWYvOPM3lcyAdq6fFcbccuz4sB2Ei5ksLE/edit#slide=id.g609f2f2b60_0_476)

别人做的app展示。

[Learn Earth Engine Basics through Applied Examples (Night-time light, Agriculture)](https://docs.google.com/presentation/d/1XkV9fqIj8VHIdzWhkzcUOcVxPg63_qRaYckgWrBblYk/edit#slide=id.g60040e55a2_0_2267)

基本用法与示例。

- Understand how to pull out data and show it on the map:可以通过搜索确定自己导入的数据，用ee.Image即可导入，导入后，通过代码编辑器上面的Imports可以查看图像的具体信息，通过addLayer可以将数据添加到地图上。
- Understand how to filter image collections:在scripts中查找collections的filter函数。
- Display different band combinations with Landsat data:查看band信息，配置显示的属性，有的bands没有显示，不过在properties下有详细解释。
- Understand how to use charts over time for visualization:通过矢量图geometry来选择感兴趣的区域，用ee.Geometry.Polygon定义，参数是坐标点。然后可以用ui.Chart.image.series将结果输出到控制台，相关参数可以查看docs下的文档说明。矢量数据是table类型时，查看FeatureCollection的函数。
- Understand reducing via generating cloud free images：理解reduce计算，链式命令过滤collection，然后去云的操作都是reduce型的计算，包括sort，median
- Understand how to calculate NDVI: 过滤条件中可以用geometry定界filterBounds，计算NDVI用normalizedDifference，且只鞥你作用域Image类型数据，不能作用于ImageCollection。
- Understand how to scale a function over a collection：类似上一条，如果要让NDVI计算作用于collection，可以使用map运算，map执行NDVI计算函数。

一些建议：关注[user guide](https://developers.google.com/earth-engine/)，看一看[debugging guide](https://developers.google.com/earth-engine/debugging)，上[论坛](https://groups.google.com/forum/#!forum/google-earth-engine-developers)。

[Earth Engine Code Editor & Javascript](https://docs.google.com/presentation/d/1KCOcW1PtFUzC4R2g3pbovtO19C4VPtjRXJxCwkG1b5Q/edit#slide=id.g36d4e169fe_300_295)

介绍了一些GEE和JS的基本概念，然后讲了Reduce Region操作，这个系列在GEE Reader文件夹下的users/dag/ee101有示例。

[Earth Engine Datasets Tour & Data Upload](https://docs.google.com/presentation/d/1ODCtpBYLTNCFkFhTMBHmyVBU41XfYzv8WUN7c0dwizc/view#slide=id.g5d4a909b46_1_18)

浏览了整个数据集的情况并对上传数据做了介绍，数据是日更的，栅格数据访问方式一致，向量数据访问方式一致，catalog所有数据都有详细的介绍文档。

- Sentinel－1 GRD 世界上唯一公开的SAR数据集，可用于crop和flood monitoring，5天的revisit cycle；
- Sentinel 2 L2(SR)和L1(TOA)精度可达10m，6天revisit；
- L4-L8 SR和TOA，L1－L5 MSS，30m，16天revisit；
- MODIS每日500m精度数据；
- 各类气象气候数据集；

[Earth Engine Big Data Structures: Images and Features](https://docs.google.com/presentation/d/1Ksax77YPEvmseush73-6GueGA765KHBNcxuJDE9154k/edit#slide=id.g47635a9183_0_4)

介绍GEE中的主要数据结构－－image和feature。
每个image：Bands+Properties，每个band有自己的Projection，Projection有CRS坐标参考系，Scale投影分辨率，CRS Transform从二维像素坐标转为二维投影坐标。

并介绍了GEE是如何接受上传并ingest images的？如何存储的？如何获取images？如何在images上计算的？

GEE在接收原始数据后，会做切割，并生成金字塔，存储到tile数据库，并且有不同的投影形式。在计算时，GEE会既爱那个tiles处理到输出所需的projection和scale上，比如GEE接口界面的地图，这点使用者无需担心。

EE images是容器，image中的像素可以被masked。masking的pixels是可以透明的。masked的像素可以不被包含在计算或可视化中的。Image Properties是一个字典型数据。

一个band内的pixels必须有相同的pixel数据类型，分辨率和投影。Images可以有许多bands。每个band都有它自己的图像金字塔，可平行计算。

EE三个bands，依次RGB，像素值决定了颜色的强度。

Band运算：数学运算，Relational，Conditional，Boolean

Image运算：卷积，gradient运算等，还有Reduce运算。其实在GEE中入门级使用最重要的就是Image/ImageCollection/Feature/FeatureCollection和Map及Reduce运算的搭配使用。因此这里Reduce计算，要重点看下。Reduce bands是能对所有bands的同位置pixels进行reduce的。ReduceNeighborhood是可以对kernel进行计算的，同一个band，一个像素为中心的kernel内的reduce。

然后是Image的INtermission。

EE Features也是容器，可以包裹Geometry，List of Properties，或者a row in a table with a geometry column。
Geometry可以是球面的也可以是平面的，Geometry也有一系列的运算。大多数的feature运算就是Geometric运算，这里还是重点关注下redeuce运算--reduceRegion。该方法可以计算ee.Image一个region内的pixels值的统计值。该算法的输出是每个band都有一个结果，所有bands结果构成一个dictionary。

[Earth Engine Collections and map()](https://docs.google.com/presentation/d/1i7TtrIN5gl0QXVt39vhLNCtMDSdLxDGJDrHumVbRZaA/edit?ts=5d7fe054#slide=id.g5d4a909b46_1_18)

重点介绍了collection和map运算。

每个image都有bands（像素组成的二维阵列，有name，投影，scale）和properties（包括日期，id等），feature可以包括geometry，list of properties
或者a row in a table with a geometry column。

相同的image或feature可以组成collection－－imagecollection和featurecollection。

所有的images和collections都可以根据其独特的ID导入。

可以对collection进行的运算常见的有(ImageCollection和FeatureCollection均可)：

- Peek at the first value: collection_name.first()
- Filter the Collection: collection_name.filter(),可以从time／space／metadata等多个方面filter--collection_name.filterDate()，collection_name.filterBounds()，collection_name.filterMetadata()
- Map a function over the Collection: 作用一个函数到所有元素，不再需要循环，借助google的并行计算快速实现。

还可以map作用于一个ImageCollection，然后生成一个FeatureCollection。

[Earth Engine Reducers](https://docs.google.com/presentation/d/1xXpHC7UkdIWA6KCwbCNaPR3IJ7MLO0ps9C8rj2Mi_KU/edit)

这里主要介绍了Reducers，其基本思想是“combine a bunch of values"，这是一个很灵活的工具，因为可以独立于值如何组合的方式来选择值得来源和去向，即可以选择下图左侧任意的算法与任一个reducer搭配。

![image.png](attachment:image.png)

一些例子：
ImageCollection.reduce()和ee.Reducer.median()组合。ImageCollection.reduce() 使用一组images生成一个image，这个输出的image的每个像素就是输入的各个images对应的像素的reduce结果，reduce具体的动作就是median。

ImageCollection.reduce()作用到single-band的图像上时，生成的也是一个singe-band的输出。此外，ImageCollection.reduce()还可以作用于multi-band的images，这时候ImageCollection.reduce()会自动地分别独立地将reducer作用于各个band上。

Reducers可以有多输入多输出：

- median, min, sum, etc: single input, single output
- minMax, percentiles([20, 50, 80]): single input, multiple output
- Linear regression: multi-input, multi-output

上述单输入可能容易混淆概念，因为reduce本来就是对 a bunch of values操作的，所以特别解释下，这里的意思是reducers计算的时候输入的值是一个一个的输入，不是比如像二维的一次输入两个值。

Image.reduceRegion()和前面提到的imagecollection的reduce不同，其不是作用于不同image对应像素，而是将一个image作为输入，对其reduceRegion()的参数代表的范围内的所有pixels做reduce，然后配合一个reducer即可做对应的计算。

许多reducers是"weighted"，算法自动地用像素的mask作为权重来执行reducer算法。在region边界上的像素是怎么处理的呢？GEE会估计像素有多少在region内，然后用这个比例作为权重。没有权重的reducer考虑边界上的pixel在不在region内是看该pixel在region内有没有超过50%。

Image.reduceRegions()可以同时作用在多个regions上reduce。它的作用主体是一个image，输入的regions是一个完整的feature collection， 对应each input feature的输出是the results of reducing the image over the pixels enclosed by that feature.

[Earth Engine Tables & Joins](https://docs.google.com/presentation/d/1Ld88M7_H6qEETVffNWZcB1ox3n6Cm0kCPPot4LjTS1g/edit#slide=id.g5d4a909b46_1_18)

关于table的处理有：filters, joins, groups, and more

为了引入join，提出一个例子，一个Table是ecoregions，一个是power stations，现在想要将两者关联来看看哪些ecoregions和stations有空间上的intersect。

可以使用join。join有多种：simple join，Inverted join等；

还有可以使用filter来控制join：Geometry，Ordering，Equality等。

最后返回的结果是字典数据。

[Earth Engine Import/Export](https://docs.google.com/presentation/d/19Tf_-tNG7TpGTsNptNLm0HoIPSAIg92Ph4_nV9PQdHk/edit#slide=id.g61134ab380_0_0)

这部分主要讲了数据的输入输出，从data catalog导入数据，以及导入自己的数据，还有如果将结果导出。

导入部分比较简单，可以很好地通过图形界面操作完成，这里重点关注下导出部分。

Export Table：You can export a **FeatureCollection** as **CSV, SHP (shapefile), GeoJSON, KML, or KMZ** using **Export.table**.

也就是说通过Export.table命令可以轻松实现导出FeatureCollection数据，不过对于导出数据，GEE有一些大小上的限制，最大1亿的features，最大1000列属性，每行的geometry最大100000个向量，每个string值最大100000个字符。

导出方式如下：

``` Javascript
// Export a table to Earth Engine table asset
Export.table.toAsset({
  collection: features,
  description:'exportToTableAssetExample',
  assetId: 'exampleAssetId',
});
```

执行代码之后，在Code Editor右侧的Tasks一栏下会有对应的导出任务，选择run即可执行。可以选择导出到Drive/Cloud Storage/EE Asset三者中任一个，通常情况下，个人觉得可以选择EE Asset。