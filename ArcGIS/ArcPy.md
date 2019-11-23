# ArcPy简介

参考[官网介绍](https://developers.arcgis.com/python/)

## ArcGIS简介

ArcGIS是一个创建管理分析和分析空间数据的平台，包括服务端组件，移动和桌面应用，以及开发工具。平台可以部署在本地，也可以在云端。

平台包括许多组件，可以通过ArcGIS REST API或共同的文件格式互相交互。了解平台之间的共同元素对构建成功的应用十分关键。

### ArcGIS Online和ArcGIS Enterprise

ArcGIS的核心是ArcGIS Online和ArcGIS Enterprise。平台提供主机GIS服务，也提供web UI和API的端口来发布，分享和管理内容，地图，应用和用户。可以使用交互端口或者访问REST服务。

- ArcGIS Online：导入数据，创建和管理内容，管理用户，创建组，分享内容。通过交互式地图，将人员、位置和数据连接起来。 使用智能数据驱动样式和直观分析工具。 与全世界或特定群组分享见解。收费500美元一年；
- MapViewer: 创建和定制二维地图，编辑数据，执行分析。ArcGIS Online配合的，个人感觉比较像ArcGIS Online的地图库，可以浏览此地图以及来自 Esri 和数千个组织的其他地图，并使用自己的数据丰富这些地图以创建新地图和地图图层；
- SceneViwer: 类似MapViewer，不过是创建和定制三维地图，创建slides；
- ArcGSI REST API:  通过API的形式提供地理空间，制图等服务。

### ArcGIS Desktop

ArcGIS Pro 和 ArcMap 是ArcGIS Desktop系列下的，允许用户结合ArcGIS Online和ArcGIS Enterprise发布和管理数据地图。他们都有很强大的分析功能，还可以结合很多扩展和脚本使用。

### ArcGIS Apps

Esri提供了一系列的apps，这些apps能和 ArcGIS Online和ArcGIS Enterprise一起提供特定的功能给特定的组织。这些apps包括：

- Collector for ArcGIS - 移动数据手机app；
- Navigator for ArcGIS - 高度定制的移动路径解决方案

等等。

### ArcGIS APIs 和 SDKs

当需要定制时，平台有全套的APIs和SDKs可以用来扩展和配置现有的ArcGIS应用或构建和配置定制app。那这里暂时只关注ArcGIS API for Python。

### ArcGIS for Developers Tools

登录ArcGIS for Developers Tools之后，可以访问dashborad和工具来管理应用，数据等。还可以通过dashborad访问其他arcgis应用。