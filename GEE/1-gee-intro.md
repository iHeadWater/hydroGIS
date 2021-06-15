# GEE简单介绍

GEE 因为是google下面的，所以国内访问是被墙的，需要科学上网，可以向学校申请，或者自己搜索[相关方法](https://github.com/OuyangWenyu/elks/blob/master/common-sense/else/vpn.md)。

## GEE API综述

GEE的基本架构论文中有概述，简单来说就是通过JS或python调用客户端代码库代码发送REST请求到后端，GEE的服务器会进行相关计算，简单认识即可，这里重点是获取GEE的数据和分析，因此从GEE的API学习开始。相关代码参考GEE上的存档。

### 数据结构

从JS对应的GEE常见数据类型开始，有：ee.String/ee.Number/ee.Array/ee.Date/ee.Dictionary/ee.List，对应这些数据结构的增删改查操作可以参考资料[5]中给的实例代码。

地图Map，Map包内的函数基本上都是地图的基本属性操作。

矢量数据包括Geometry／Feature／FeatureCollection，是GIS中的基本数据类型，GEE有丰富的矢量数据操作，比如地图显示／空间计算等，Feature相当于Geometry+属性值。

栅格数据类型主要是Image和ImageCollection。栅格是二维矩阵形式表示空间地物或现象分布的数据组织方式，每个像元包含一个信息以及一些记录空间位置等的属性信息。

高程数据(Terrain)：GEE上的DEM数据大概有20多种，最常用的主要是SRTM数据。常用的关于高程计算相关方法都在ee.Terrain下，比如计算方位aspect，计算坡度slope等。

### 流程控制

GEE中for循环式尽量不要用，因为其运算慢，应尽可能利用mapreduce进行计算。

使用GEE内部自带的map、iterate等实现循环,可以使用循环的数据主要是字典和集合。还有一个evaluate方法，该方法是一个异步的方法。在异步回调的方法中，可以将数据转换为本地client可操作方式。

条件判断方面，ee.Algorithms.If(condition, trueCase, falseCase)。

### 基本运算

根据文献介绍，GEE的函数库主要功能有：

- 数值运算：像素或feature级的运算，算术／逻辑／数据类型转换等；
- 数组矩阵运算：像素或feature级的运算，element-wise运算／矩阵各类运算等；
- 机器学习：像素或feature级的运算，监督分类／回归和非监督分类等算法；
- 图像像素运算：谱运算／data masking／可视化／定位等；
- 核运算：image tile级运算，包括卷积／地形／纹理等，以及各类核；
- 图像运算：band操作，元数据属性，边缘检测等运算；
- Reducers：操作对象与运算环境相关，是aggregate data over time（imageCollection.reduce()）,space(image.reduceRegion()),bands(image.reduce()),arrays等数据结构的方式，aggregate的方式有minimum,maximum,mean,median,standard deviation等；
- 几何运算：feature级运算，包括measurements等运算；
- table/collection运算：流运算，包括filer／sorting等运算；
- vector/raster运算：空间插值／栅格化／向量化等。

#### 影像去云

影像去云实际中使用主要涉及两种影像－－Landsat和Sentinel－2影像。这两种影像在分类识别，地物分析，水体处理等方面比较常用。GEE本身提供来一部分云识别算法，一般使用GEE自带云识别算法或影像自带的QA波段识别云就可以满足要求。GEE中影像去云主要有两种方式，一种是使用算法计算云量分数，另外一种是直接使用影像的QA波段。

- [] 待补充

#### Filter

顾名思义，筛选运算可以方便查找需要的各种数据。在ee.List, ee.FeatureCollection, ee.ImageCollection中都有，过滤条件常用的有：

- 空间过滤：ee.Filter.bounds、ee.Filter.intersects等；
- 时间过滤：ee.Filter.date、ee.Filter.dayOfYear等；
- 属性过滤：ee.Filter.eq、ee.Filter.lt等；
- 两个集合通过字段过滤，通常结合join使用：ee.Filter.equals等；
- 多个filter结合使用：ee.Filter.and、ee.Filter.or等。

#### Join

Join类似SQL中的Join运算，Join通过利用Filter中的筛选条件，提取两个不同集合中满足条件的所有元素，即有集合A和集合B,然后通过一定条件筛选和联合条件取得满足条件的集合C。

Join最为常用的一种用法是处理缺失数据，比如取得一个时间序列范围内的影像数据，经过去云处理后会缺失部分数据，一种是直接使用有缺失的数据，另一种是重建相关数据，这时最为关键的就是使用join来筛选数据。

#### Reducer

使用GEE很重要的功能，最常用的功能就是各种统计计算，GEE中使用各种计算功能使用的类方法就是ee.Reducer，这个核心掌握了，GEE的基本计算功能就掌握了。

从ee.Reducer中可以看到，包含的主要功能有：统计数量，计算均值，计算极值，统计频率，计算线性变换等。

总结起来，计算类型上主要有：

1. 空间计算：比如image中的RediceRegion等，面向单波段的影像计算，计算结果是字典，可以通过key取出具体数值。
2. 波段计算：一张影像中的多个波段，计算这些波段的各种值，面向多波段的影像计算。
3. 时间计算：比如FeatureCollection，ImageCollection中的reduce等。

利用combine可以对同一个属性进行多种不同的计算。

group可以进行分组统计。

#### 数据导出

在GEE中数据导出可以有以下几种方式,

- getDownloadURL：生成URL然后下载相关数据，生成小返回简单测试可以使用；
- getVideoThumbURL：生成GIF动画；
- Export：这种事到处数据的主要方式，可以导出到Google Assets/Google Drive/Google Cloud Storage三个地方；
- Chart：chart图表的数据可以通过CSV下载下来。

GEE可以直接导出的数据包括：FeatureCollection和Image。ImageCollection不支持直接导出，可以转换后再导出。

对Export展开说明，GEE可以到处的资源有：

- 影像image
- 地图瓦片map
- 矢量文件table
- 视频video

#### UI编程

ui.Chart:图表是GEE展示统计结果直观的手段,通过图表我们可以做各种数据统计。GEE使用的chart就是Google Chart，所以相关文档可以直接查询[Google Charts](https://developers.google.com/chart/interactive/docs/)。

GEE主要有三种数据的图表：array数据的图表，feature数据的图表，image数据的图表。

## How GEE works

要更好的应用GEE，还是有必要了解一些GEE基本的工作原理。GEE不同于任何一个GIS工具，其是一个云平台，更好的了解基本工作原理能弄清楚一些可能会碰到的显得很奇怪的behaviour:

### Client vs. Server

使用GEE要区分好client的JS对象和服务端的earth engine对象。

Javascript的objects就是正常的JS对象，不过要操作服务端的对象需要在脚本中对JS对象做些处理，比如要把一个JavaScript的string要送到EE服务端计算，需要将其包入一个EE的string对象中，包含其的容器就是proxy object，不过print函数还是可以直接给出其内容的。

在EE中，尽量面向server端写程序，因为client是不知道server段的objects的。所有的ee.Thing初始化的都是server对象，所有ee.Thing的method都是server 函数，没有ee的就是client的。client的变server的需要容器。尽量避免混合使用client和server的对象和方法。

比如for循环，要更多地去运用GEE云平台的map运算代替，对于if，在EE中有相应的语法。

混合使用客户端和服务端的objects不是效率好的方式，因此尽量用ee开头的对象进行操作。

### Deferred Execution

了解指令是如何被送到Google处理以及google是如何讲结果返回到web浏览器显示的。

客户端的代码首先被client库转为JSON对象，然后才被发给Google，然后等待回应。每个对象或者代表一组获得某个输出的运算，或者代表一个要展示在客户端的image。

比如addLayer运算，当发送请求后，只有显示的那个tiles才被返回，当pan或者zoom的时候，其他的tiles会被懒加载出来，这里有并行计算，所以显示图像的顺序是不定的。

### Scale

scale就是指**像素分辨率**，分析的scale由输出决定的，不是输入。当请求结果或image等时，GEE会根据最后的输出指定的scale来决定作为输入要使用的图像金字塔的合适级别。

GEE中的图像都会有多个scales，组成像素金字塔。金字塔策略决定了在金字塔的给定一层每个像素是如何从更低的下一层的2*2像素block的聚合计算的。

一个图像的最底层的分辨率也就是最高的分辨率是根据数据提供者提供的为准的，接受到数据之后，GEE就会生成更高级的，也就是像素低的图像来组成金字塔，2*2变1，这样一层层地生产金字塔，直到最后生产到最高级的256*256像素tile。

所以再回头理解这小节开始的那段话，意思就是根据最后输出的需求，会从金字塔中抽取最合适的tile来显示。

### Projections

GEE的设计使得我们可以很少去关注投影，和scale类似，projection也是由pull端决定的。inputs是在output的投影下被requested的。output可能有由一个函数参数（比如crs）决定，或者Code Editor中的Map决定（Code Editor有一个maps墨卡托投影），或者用一个reproject()调用。当在Code Editor上展示images时，inputs都会被请求maps mercator。

在GEE中，投影由Coordinate REference System（CRS或许多方法中的crs参数）指定的。可以通过调用projection（）函数到image上，来查看image的projection。

只有当输出ambiguous时，GEE才会要求指定projection或者scale。ambiguity出现的情况可来自组合不同投影下的数据集时。一个是输入images的composite或mosaic的image会有默认的投影：WGS84 with 1-degree scale。

可以通过reproject()方法指定operation的projection。reprojection会导致输入按照reproject的投影被请求。要尽量避免使用reprojection，除非必须用。比如最终的输出和reprojection的不同，最后还会导致输出的reprojection。

### Debugging

GEE的debug涉及客户端和服务端，比较麻烦，所以调试不太方便，因此有一些特别的debug策略给出。

基本上，GEE的coder Editor会给出错误的提示，其他的debug主要靠输出来校核，用好print()和Map.addLayer()

有几个比较麻烦的错误，这里也记录下，因为比较容易遇到的：

#### User memory limit exceeded

GEE处理算法都是并行的，把输入切分，然后每个输入分别运行，最后再汇总结果，因此，所有输入都必须适应内存条件，比如不能把所有完整的image collection放入到一个tile中。

其他的可以参考GEE的官方文档的[debugging](https://developers.google.com/earth-engine/debugging)的Best Practices

## 常用API介绍

先主要围绕Map，reduce计算和image，feature，imagecollection和featurecollection记录，其他部分后面用到的再逐步记录。

### Image

#### Visualization

在GEE中，可视化是很重要的一个环节，主要就是Map.addLayer()如何使用的问题。如果没有任何额外的参数，那么默认的Code Editor会分配RGB三个颜色给到前三个bands。默认的stretch则会考虑band的数据类型，比如floats会被stretched到[0,1]，16位数据会被stretched到可能值的全部范围，这样可能是不合适的，因此在可视化的时候，要学会如何配置参数。

Map.addLayer()的参数有：

|  参数  | 描述  | 类型 |
|  ----  | ----  | ---- |
| bands  | 逗号分隔的三个band的名称，分别对应RGB三色 | list |
| min  | 被映射到0的值（也就是说被映射到RGB三色的最小值的那个值，这样图像才知道如何显示） | number or list of three numbers, 每个band都有一个 |
| max  | Value(s) to map to 255 | number or list of three numbers, one for each band |
| gain  | 每个像素值都乘以的那个值 | number or list of three numbers, one for each band|
| bias  | 每个DN都被加的那个数 | number or list of three numbers, one for each band|
| gamma  | Gamma correction factor(s) | number or list of three numbers, one for each band|
| palette  | List of CSS-style color strings (只有单波段的image才能用) | comma-separated list of hex strings|
| opacity  | The opacity of the layer (0.0 is fully transparent and 1.0 is fully opaque) | number|
| format  | Either "jpg" or "png" | string|

#### Morphological Operations

Image中的Morphological Operations类似于reduceNeighborhood()，可以输入一个kernel的inputs做reduce运算。

### ImageCollection

#### Visualization

当一个多波段的image被加载到Map中时，GEE默认选择前三个波段并按照RGB来显示，并根据data type将数据stretching到合适的范围。对于ImageCollection的可视化和Image是有类似的，因为它只是同时显示很多image而已，所有image共用一套可视化参数而已。

问题是如果有重叠的image，会怎么办呢？

#### Mapping over an ImageCollection

Mapping over an ImageCollection是比较重要的一个运算：imageCollection.map()。map()函数的唯一参数是一个函数，这个函数也是只有一个参数：ee.Image，这个函数有一些限制，不能print，不能使用函数外的变量，也不能用JS的if和for，如果想要使用条件判断，可以在函数内使用ee.Algorithms.If()执行条件判断，不过尽量用filter先把要判断的判断好，效率会更高。

#### Reducing an ImageCollection

Reducing an ImageCollection是composite images in an ImageCollection的运算。它会组合collection中所有的images为一个image，比如images的最值／均值等。images的每个band各自计算。比如collection.median();等价于collection.reduce(ee.Reducer.median());

Compositing是指利用聚合函数将空间上重叠的images组合成一个image的过程；Mosaicking是指空间上拼接image数据集来生产一个空间上连续的image。这俩者的操作都是直接通过ImageCollection调用相关的函数实现的，没有显示地说明。比如：

``` Javascript
var composite = naip2004_2012.max();
var mosaic = naip2012.mosaic();
```

mosaic在处理有重叠的图像时，会根据images在collection中的上下位置来组合重叠的部分，可以通过使用image masks来控制一次mosaic中的pxiels。

做迭代运算时，map就不行了，这时候要使用iterate()函数。比如想从一个时间序列上计算时间t时的累计值，那么就需要递归地从0到t计算。iterate的使用方式是imageCollection.iterate()。

iterate的使用也是首先构造一个函数，函数可以传入外部参数的值以帮助运算。一般是对collection中的元素去做迭代，因此参数是image或feature。注意iterate也是有局限的，它不能修改函数外变量的状态，不能print，不能用JS的if和for，任何喜爱那个要迭代入下一步的信息都必须在函数的返回值中。如果要用If，可以使用ee.Algorithms.If()。

### Geometry, Feature, FeatureCollection

Feature在GEE中是由GeoJSON定义的。Feature是一个有Geometry属性的对象，还有一个properties属性以字典结构存储一些属性值。FeatureCollection是features的集合。

GEE有多种table数据集，可以通过提供table ID给FeatureCollection的构造函数来加载table数据集。

可以直接使用Map.addLayer()将Geometry, Feature, FeatureCollection显示到Map上，默认显示黑线和半透明的黑色填充。

Mapping over a FeatureCollection和ImageCollection的类似。

Reducing a FeatureCollection也有些自己特别的reduce计算。比如可以通过featureCollection.reduceColumns()聚合FeatureCollection的属性值，比如有一个属性A，使用.reduceColumns()运算可以对A下的所有数据reduce，然后配合Reducer可进行计算。reduceColumns()返回值是一个dictionary。

### Reducer

#### ImageCollection Reductions

Consider the example of needing to **take the median over a time series of images** represented by an ImageCollection. 

![image.png](attachment:image.png)

对一个多波段的ImageCollection，进行reduce计算后，返回的还是一个多波段的image。比如对于Reducer为median的一次reduce计算， each pixel of which is the median of all unmasked pixels in the ImageCollection **at that pixel location**. 也就是说，reducer在每个band上都重复了一次。

#### Image Reductions

Image Reductions是针对Image内的各个band去计算的，ImageCollection的reduce是对不同images的同一个band去算的。

#### statistics of an Image Region

统计一个Image的Region时用reduceRegion。region由一个Geometry表示。输出的是这个区域的所有pixels的统计值。region参数是一个Feature geometry。最后输出的结果是一个Dictionary。

给reduction提供的参数常见的有： 

- the reducer (ee.Reducer.mean())
- the geometry (region.geometry())
- the scale (30 meters)
- maxPixels for the maximum number of pixels to input to the reducer

在reduceRegion()中，scale是必须要指定的，因为在复杂的处理流中，可能包括来自有不同scales的不同数据源的数据，如果不指定，输出的scale是不能无异议的由输入决定。scale默认1 degree，这可能不能产生满足要求的结果。

有两种方式来设置scale值，一种是指定scale参数值，一种是指定CRS和CRS transform。CRS即Coordinate Reference System，坐标系统，由相关权威机构比如EPSG或SR－ORG定义，由"机构:code"唯一标识，比如EPSG:4326。CRS transform是CRS的转换方式，由一系列仿射变换参数定义。

通常指定scale就足够了，GEE会首先栅格化region，然后决定哪些像素被送入reducer。如果scale没有带CRS指定，region会按照image本来的投影scaled到特定的resolution来进行栅格化。如果CRS和scale都指定了，那么region就会基于指定值进行栅格化。

关于Pixels in the region，在指定的scale和projection前提下，region中的pixels按照以下规则确定：

- Unweighted reducers: 比如ee.Reducer.count()，ee.Reducer.mean().unweighted()，regions边界上的像素的中心在region中且image的mask不为0，那么该像素就在region内；
- Weighted reducers:比如ee.Reducer.mean()，如果像素至少有0.5%在region内，且image的mask不为0，那么该像素就在region内，像素的权重是iamge's mask的最小值和被region覆盖的像素部分占像素的比例。

maxPixels参数需要指定，以使计算成功，因为有可能出现region内像素太多的情况而导致报错：

``` Javascript
Dictionary (Error)
  Image.reduceRegion: Too many pixels in the region. Found 527001545, but only 10000000 allowed.
```

有几种方式来避免上述类似的错误: 
- increase maxPixels, 
- as in the example, increase the scale,
- set bestEffort to true, which automatically computes a new (larger) scale such that maxPixels is not exceeded.

If you do not specify maxPixels, the default value is used.

#### Statistics of Image Regions

为了在FeatureCollection中的多个regions中得到image统计值，可以使用image.reduceRegions()来一次性reduce多个regions。输入给reduceRegions()的是一个Image和一个FeatureCollection，输出则是另一个FeatureCollection，其值是每个Feature上都有设置properties。

#### Statistics of FeatureCollection Columns

reduce在FeatureCollection中的features的properties，要使用featureCollection.reduceColumns()。reduceColumns是对所有feature同一列的值一起reduce。

#### Grouped Reductions and Zonal Statistics

通过使用reducer.group()可以对Image或FeatureCollection中的每个zone做统计。比如：

``` Javascript
reduceColumns({
    selectors: ['pop10', 'housing10', 'statefp10'],
    reducer: ee.Reducer.sum().repeat(2).group({
      groupField: 2,
      groupName: 'state-code',
    })
```

groupField指定selectors中按哪一个去group，这部分个人感觉和sql语句有些类似了。repeat(2)表示sum运算执行两次，也就是在'pop10', 'housing10'上各执行一次。

### Join

Joins是基于由ee.Filter指定的条件用来从不同的collections(e.g. ImageCollection or FeatureCollection，即ImageCollections之间可以join，FeatureCollections之间也可以join) 结合elements。这部分也和sql的join有一些相似的地方。

join的基本方式：

``` Javascript
// Create the join.
var simpleJoin = ee.Join.simple();

// Apply the join.
var simpleJoined = simpleJoin.apply(collections1, collections2, filter);
```

其基本作用是 finding the common elements among different collections or filtering one collection by another.

最后返回的还是collections。

### Array

ee.Array可以表示任意维度的向量。不过Array的计算相对较慢，因此，如果问题能不用Array解决，尽量就不要使用Array。
