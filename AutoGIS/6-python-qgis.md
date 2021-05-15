# lesson 7

本章主要介绍如何在QGIS中使用Python -- PyQGIS。

## QGIS 简介

在介绍Python in QGIS之前，首先了解下QGIS。这部分主要参考了 [QGIS简体中文操作手册](https://malagis.com/qgis-handbook-index.html)

QGIS（之前也叫Quantum GIS）是一个开源的桌面GIS软件，它提供了数据的显示、编辑和分析功能。 QGIS以C++写成，它的GUI使用了Qt库。QGIS允许集成使用C++ 或Python写成的插件。

QGIS是一个多平台的应用，可以在多种操作系统上运行，包括Mac OS X、Linux、UNIX和Windows。 相较于商业化GIS，QGIS的文件体积更小，需要的内存和处理能力也更少。因此它可以在旧的硬件上或CPU运算能力被限制的环境下运行。


首先，安装QGIS，直接去[官网](http://www.qgis.org/)

可以使用 OSGeo4W 下载QGIS相关软件。下载OSGeo4W然后安装，默认安装即可。如果想要安装QGIS 长期维护的非最新版本，可以使用advanced安装，然后选择qgis-ltr-full。

然后，打开安装好的QGIS。可以看到图形界面和ArcGIS还是有一些相似的地方，后面具体用到了再逐步补充。

## Python in QGIS

现在讨论QGIS（简称PyQGIS）中Python的基本功能。python在它的生态系统中有重要作用，许多原装的插件和一些数据提供模块都是用python写的，并且所有的函数接口和库都有python api。另外，只需花费很少的精力就可以编写QGIS扩展，并将其无缝集成到其用户界面中，还可以使用QGIS的组件（例如地图窗口或数据后端）创建独立的应用程序，或在QGIS中运行自定义脚本。更多内容可以参考：[PyQGIS Developer Cookbook](https://docs.qgis.org/3.4/en/docs/pyqgis_developer_cookbook/intro.html)

下面简单了解如何从集成的Python控制台运行代码，然后编写一个简单的Python脚本，最后将该脚本的功能应用于自己的插件。

首先，新建一个项目，然后导入数据，直接使用WFS服务导入图层： Layer > Add layer > Add WFS layer

在导入数据之前，首先将坐标设置为本例子所需的  ETRS89/GK25FIN (EPSG:3879)，点击右下角的EPSG：4326，将这个默认的坐标系改为自己所需的。

点击之后弹出的窗口里，在Filter中输入EPSG:3879即可找到。选中之后，点击apply即可。

然后导入图层。本例所需的URL：  http://kartta.hel.fi/ws/geoserver/avoindata/wfs ，点击新建链接，Name可以输入自己想要的，然后贴入上述URL即可。然后点击Connect链接到该服务。如果弹出错误，忽略即可。然后在给出的列表中，选择Metro railway lines (Seutukartta_liikenne_metro_rata)作为本例使用的数据，点击add即可发现QGIS窗口已经显示出图形了。

可以保存项目到本文件夹下，这里是lesson7.qgz。

下面就看看如何在控制台中运行QGIS python程序。Plugins > Python console 或者快捷键 Ctrl+Alt+P 进入控制台。输入以下代码可看结果：

```Python
# Get active layer:
>>> layer = iface.activeLayer()

# Let's see what we got
>>> print(type(layer))
<class 'qgis._core.QgsVectorLayer'>

>>> print(layer.sourceName())
Seutukartta_liikenne_metro_rata

>>> print(layer.featureCount())
3
```

暂时先到这里，更多关于QGIS的内容，可以参考的资料有：

- Anita Graser’s beginner-friendly [PyQGIS 101: Introduction to QGIS Python programming for non-programmers](https://anitagraser.com/pyqgis-101-introduction-to-qgis-python-programming-for-non-programmers/)
- [PyQGIS Developer Cookbook](https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/) with compehensive tutorials

本repo也专门为QGIS的学习设置了一个文件夹，更多内容参考那里。