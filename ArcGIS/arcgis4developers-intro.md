# ArcGIS for Developers简介

参考[官网介绍](https://developers.arcgis.com/).

首先需要一个arcgis for developers的帐号，如果有学校账户最好，如果没有的话就需要自己购买，可以先试用一个月，如果觉得有用可以再购买一个学生版本的。

接下来按照网站的导航栏一一记录。

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

## Graphics and Data

使用ArcGIS APIs和SDKs，从展示和定制图形和数据开始。然后根据下面的各个教程去尝试即可。这里简单记录下教程的思路：

大部分GIS教程教学总是从矢量图开始介绍，这里也不例外。先介绍了点线面是如何创建以及如何add到layer上展示的，接口很多，可以使用javascript实验下。

接着是导入数据，这里是以ArcGIS Online为例进行了介绍。前提是要有一个ArcGIS帐号，可以使用ArcGIS Online，然后就可以上传不同格式的文件到ArcGIS Online上了。

然后是在ArcGIS Online上创建矢量图并通过利用Javascript API来在web端展示。

其余暂略。

水文上更常用的是ArcGIS的空间分析功能，因此再浏览下几个空间分析的教程。

Buffer and intersect geometry等几个使用REST API的示例，均需要安装Postman来进行测试应用，需要的配置也较多。

直接使用ArcGIS Online的Find and extract data等示例感觉上更像是一个在线版的弱版ArcGIS Pro。

对于相对较复杂的空间分析应用，比如示例Run a geoprocessing task and python script，则需要基于ArcGIS Pro扩展，扩展的工具是ArcGIS Pro SDK for .NET，使用它，结合微软VS Studio，可以构建Pro的插件应用供给别人使用。所以还是要基于ArcGIS Pro来完成相应的基本工作。

总结以上，可以知道，ArcGIS Online和ArcGIS for Developers是相对独立于ArcGIS Desktop和ArcGIS Pro的一套基于云端的ArcGIS应用，其优点在于任意平台下均可使用，但其提供的接口比较繁杂，根据示例的粗略浏览，可以了解到如果构建一个完整的gis应用还是需要多种工具配合使用的，其设计的出发点还是如名称所示，是面向基于ArcGIS的二次开发者的，因此个人认为如果是更多的使用ArcGIS的一些分析计算功能，而不需要再给第三方提供服务，那么这一套学习的必要性不是很大，并且一般的GIS应用不是特别需要大量的复杂多样的空间计算，因此可以使用开源工具完成，如果真的需要ArcGIS的云端服务，那可以再回来学习。